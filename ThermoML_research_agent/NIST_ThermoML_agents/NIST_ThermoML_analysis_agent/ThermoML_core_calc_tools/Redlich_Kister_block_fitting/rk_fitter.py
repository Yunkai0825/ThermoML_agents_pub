"""
Redlich-Kister polynomial fitting.
====================================
Fits binary excess property data to the Redlich-Kister expansion:

    Y^E(x1) = x1 * x2 * Σ_{k=0}^{n} A_k * (x1 - x2)^k

where x2 = 1 - x1.  The fitting uses least-squares regression with
automatic order selection (BIC-based) up to RK_MAX_ORDER.

Supports fitting multiple properties in a single call (multi-property)
and fitting a property under both mixing rules simultaneously
(activation-energy vs free-energy ideal baselines).

Public API
----------
- fit_redlich_kister(x1, y_excess, max_order=5) → dict
- eval_redlich_kister(x1, coeffs) → np.ndarray
- auto_fit_redlich_kister(x1, y_excess) → dict   (BIC-based order selection)
- fit_multi_property(x1, excess_dict, max_order=5) → dict
"""

from __future__ import annotations

import logging
from typing import Dict, List, Optional, Tuple

import numpy as np
from numpy.linalg import lstsq

log = logging.getLogger("RK-FIT")


def eval_redlich_kister(
    x1: np.ndarray,
    coeffs: List[float] | np.ndarray,
) -> np.ndarray:
    """Evaluate the RK polynomial at given compositions.

    Parameters
    ----------
    x1 : ndarray
        Mole fractions of component 1.
    coeffs : list of float
        RK coefficients [A0, A1, ..., An].

    Returns
    -------
    ndarray
        Y^E values at each x1.
    """
    x1 = np.asarray(x1, dtype=float)
    x2 = 1.0 - x1
    y = np.zeros_like(x1)
    diff = x1 - x2
    for k, ak in enumerate(coeffs):
        y += ak * diff**k
    return x1 * x2 * y


def fit_redlich_kister(
    x1: np.ndarray | List[float],
    y_excess: np.ndarray | List[float],
    *,
    max_order: int = 5,
) -> dict:
    """Fit RK coefficients to excess property data at a fixed order.

    Parameters
    ----------
    x1 : array-like
        Mole fractions of component 1 (excluding pure endpoints 0, 1).
    y_excess : array-like
        Excess property values (same length as x1).
    max_order : int
        Polynomial order (number of coefficients = max_order + 1).

    Returns
    -------
    dict
        {
            "coeffs": [A0, A1, ..., An],
            "order": n,
            "r_squared": float,
            "rmse": float,
            "n_points": int,
            "y_fitted": [...],
            "residuals": [...],
        }
    """
    x1 = np.asarray(x1, dtype=float)
    y_excess = np.asarray(y_excess, dtype=float)

    if len(x1) < max_order + 1:
        return {
            "error": f"Need at least {max_order + 1} data points, got {len(x1)}",
        }

    x2 = 1.0 - x1
    diff = x1 - x2

    # Build design matrix: each column = x1 * x2 * (x1-x2)^k
    A_mat = np.column_stack([
        x1 * x2 * diff**k for k in range(max_order + 1)
    ])

    # Least-squares solve
    coeffs, residuals, rank, sv = lstsq(A_mat, y_excess, rcond=None)

    y_fitted = A_mat @ coeffs
    resid = y_excess - y_fitted
    ss_res = np.sum(resid**2)
    ss_tot = np.sum((y_excess - np.mean(y_excess))**2)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    rmse = float(np.sqrt(ss_res / len(x1)))

    # Coefficient standard errors from the least-squares covariance:
    # cov = s^2 (X^T X)^-1 with s^2 = ss_res / (n - k).  Needs >=1 dof.
    n_pts, k_params = len(x1), max_order + 1
    coeff_se: list[float] | None = None
    insignificant: list[int] = []
    dof = n_pts - k_params
    if dof >= 1:
        try:
            s2 = ss_res / dof
            cov = s2 * np.linalg.inv(A_mat.T @ A_mat)
            se = np.sqrt(np.maximum(np.diag(cov), 0.0))
            coeff_se = [round(float(v), 6) for v in se]
            insignificant = [
                k for k, (a, s) in enumerate(zip(coeffs, se))
                if s > 0 and abs(a) / s < 2.0
            ]
        except np.linalg.LinAlgError:
            coeff_se = None

    out = {
        "coeffs": coeffs.tolist(),
        "order": max_order,
        "r_squared": round(float(r2), 6),
        "rmse": rmse,
        "n_points": n_pts,
        "y_fitted": y_fitted.tolist(),
        "residuals": resid.tolist(),
        "dof": int(dof),
    }
    if coeff_se is not None:
        out["coeff_std_errors"] = coeff_se
        if insignificant:
            out["insignificant_coeffs"] = insignificant
    return out


def auto_fit_redlich_kister(
    x1: np.ndarray | List[float],
    y_excess: np.ndarray | List[float],
    *,
    max_order: int = 5,
    noise_floor: Optional[float] = None,
) -> dict:
    """Fit RK with automatic order selection (information criterion).

    Degrees-of-freedom guard: candidate orders always leave at least one
    residual dof (order ≤ n−2), which removes the k=n "perfect fit"
    trap.  For sparse data (n < 8) the small-sample-corrected AICc is
    used and candidates are further restricted to n−k−1 ≥ 1 (order
    ≤ n−3, ≥2 residual dof); otherwise BIC.

    Parameters
    ----------
    noise_floor : float, optional
        Measurement resolution of y (same units).  When given, the
        criterion's mse is floored at ``noise_floor**2`` so fits of
        heavily rounded data cannot win on artificial perfection.

    Returns
    -------
    dict
        Same as fit_redlich_kister(), plus:
            "bic": float (value of the SELECTED criterion),
            "criterion": "bic" | "aicc",
            "all_orders": [{order, bic, aicc, r2, rmse}, ...],
            "selected_order": int,
            "sparse_data_note": str (only when n < 5),
    """
    x1 = np.asarray(x1, dtype=float)
    y_excess = np.asarray(y_excess, dtype=float)
    n = len(x1)

    if n < 3:
        return {"error": f"Need at least 3 data points, got {n}"}

    use_aicc = n < 8
    # dof floor: BIC regime order <= n-2 (>=1 dof); AICc regime order
    # <= n-3 (>=2 dof, keeps the correction term finite).
    order_cap = min(max_order, n - 3 if use_aicc else n - 2)
    order_cap = max(order_cap, 0)

    results_by_order = []
    best_crit = float("inf")
    best_order = 0

    for order in range(0, order_cap + 1):
        res = fit_redlich_kister(x1, y_excess, max_order=order)
        if "error" in res:
            continue

        k_params = order + 1
        ss_res = sum(r**2 for r in res["residuals"])
        mse = ss_res / n if n > 0 else 1e-10
        if noise_floor is not None and noise_floor > 0:
            mse = max(mse, noise_floor**2)
        if mse <= 0:
            mse = 1e-30
        bic = n * np.log(mse) + k_params * np.log(n)
        aicc = float("inf")
        if n - k_params - 1 >= 1:
            aicc = (n * np.log(mse) + 2 * k_params
                    + 2 * k_params * (k_params + 1) / (n - k_params - 1))

        crit = aicc if use_aicc else bic

        results_by_order.append({
            "order": order,
            "bic": round(float(bic), 3),
            "aicc": round(float(aicc), 3) if np.isfinite(aicc) else None,
            "r_squared": res["r_squared"],
            "rmse": res["rmse"],
        })

        if crit < best_crit:
            best_crit = crit
            best_order = order

    # Refit at best order
    best_fit = fit_redlich_kister(x1, y_excess, max_order=best_order)
    best_fit["bic"] = round(float(best_crit), 3)
    best_fit["criterion"] = "aicc" if use_aicc else "bic"
    best_fit["all_orders"] = results_by_order
    best_fit["selected_order"] = best_order
    if n < 5:
        best_fit["sparse_data_note"] = (
            f"Only {n} mixture points — RK order capped at {order_cap} "
            f"(AICc, ≥2 residual dof); treat coefficients as provisional."
        )

    return best_fit


def fit_multi_property(
    x1: np.ndarray | List[float],
    excess_dict: Dict[str, np.ndarray | List[float]],
    *,
    max_order: int = 5,
) -> Dict[str, dict]:
    """Fit RK polynomials for multiple excess properties on the same x grid.

    Useful when a single block contains, e.g., both density and viscosity
    data, or when fitting both activation-energy and free-energy excess
    simultaneously.

    Parameters
    ----------
    x1 : array-like
        Mole fractions (same for all properties).
    excess_dict : dict
        {property_label: y_excess_array}.
        Label examples: "density_linear", "viscosity_arrhenius",
        "viscosity_linear" (for dual-baseline analysis).
    max_order : int
        Max RK polynomial order for BIC selection.

    Returns
    -------
    dict
        {property_label: auto_fit_result, ...}
        Each value is the dict returned by auto_fit_redlich_kister.
    """
    x1 = np.asarray(x1, dtype=float)
    results: Dict[str, dict] = {}
    for label, y_exc in excess_dict.items():
        y_exc = np.asarray(y_exc, dtype=float)
        res = auto_fit_redlich_kister(x1, y_exc, max_order=max_order)
        results[label] = res
    return results
