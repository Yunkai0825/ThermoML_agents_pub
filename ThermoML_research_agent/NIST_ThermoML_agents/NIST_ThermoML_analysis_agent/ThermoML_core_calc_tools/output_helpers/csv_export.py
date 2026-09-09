"""
csv_export — Save fitting & baseline results as CSV files.
===========================================================
Each function writes a tidy CSV with headers.  All paths are returned
so callers can log where the files landed.
"""

from __future__ import annotations

import csv
import io
import os
from typing import Any, Dict, List, Optional, Sequence

import numpy as np


def _write_csv(path: str, columns: List[str], rows: List[List[Any]]) -> str:
    """Write rows to *path*, creating parent dirs as needed.  Returns path."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(columns)
        w.writerows(rows)
    return path


def _fmt(v, decimals=8):
    if v is None or (isinstance(v, float) and np.isnan(v)):
        return ""
    if isinstance(v, float):
        return f"{v:.{decimals}f}"
    return str(v)


# ------------------------------------------------------------------
#  save_fit_csv — Redlich-Kister fit result
# ------------------------------------------------------------------

def save_fit_csv(
    path: str,
    x_mix: np.ndarray | List[float],
    y_excess: np.ndarray | List[float],
    y_fitted: np.ndarray | List[float],
    residuals: np.ndarray | List[float],
    rk_coeffs: List[float],
    rk_order: int,
    r_squared: float,
    rmse: float,
    *,
    x_label: str = "x1",
    y_label: str = "Y_excess",
    metadata: Optional[Dict[str, Any]] = None,
) -> str:
    """Save RK fit data + summary CSV.

    Writes two files:
      - ``<path>``            — per-point data  (x, Y_excess, Y_fitted, residual)
      - ``<path>_summary``    — coefficients, R², RMSE, metadata

    Returns path of the per-point file.
    """
    x = np.asarray(x_mix, dtype=float)
    ye = np.asarray(y_excess, dtype=float)
    yf = np.asarray(y_fitted, dtype=float)
    res = np.asarray(residuals, dtype=float)

    # Per-point data
    cols = [x_label, y_label, f"{y_label}_fitted", "residual"]
    rows = [[_fmt(x[i]), _fmt(ye[i]), _fmt(yf[i]), _fmt(res[i])] for i in range(len(x))]
    _write_csv(path, cols, rows)

    # Summary sidecar (short suffix to stay within Windows MAX_PATH)
    base, ext = os.path.splitext(path)
    summ_path = f"{base}_summ{ext}"
    summ_cols = ["key", "value"]
    summ_rows = [
        ["rk_order", str(rk_order)],
        ["r_squared", _fmt(r_squared, 8)],
        ["rmse", _fmt(rmse, 8)],
        ["n_points", str(len(x))],
    ]
    for k, ak in enumerate(rk_coeffs):
        summ_rows.append([f"A{k}", _fmt(ak, 10)])
    if metadata:
        for mk, mv in metadata.items():
            summ_rows.append([mk, str(mv)])
    _write_csv(summ_path, summ_cols, summ_rows)

    return path


# ------------------------------------------------------------------
#  save_excess_csv — excess property data (before fitting)
# ------------------------------------------------------------------

def save_excess_csv(
    path: str,
    x: np.ndarray | List[float],
    y_exp: np.ndarray | List[float],
    y_ideal: np.ndarray | List[float],
    y_excess: np.ndarray | List[float],
    *,
    x_label: str = "x1",
    y_label: str = "Y",
    mixing_rule: str = "linear",
) -> str:
    """Save excess-property CSV: x, Y_exp, Y_ideal, Y_excess."""
    x = np.asarray(x, dtype=float)
    ye = np.asarray(y_exp, dtype=float)
    yi = np.asarray(y_ideal, dtype=float)
    yx = np.asarray(y_excess, dtype=float)

    cols = [x_label, f"{y_label}_exp", f"{y_label}_ideal_{mixing_rule}", f"{y_label}_excess"]
    rows = [[_fmt(x[i]), _fmt(ye[i]), _fmt(yi[i]), _fmt(yx[i])] for i in range(len(x))]
    return _write_csv(path, cols, rows)


# ------------------------------------------------------------------
#  save_baseline_csv — ideal baseline data
# ------------------------------------------------------------------

def save_baseline_csv(
    path: str,
    x: np.ndarray | List[float],
    y_exp: np.ndarray | List[float],
    y_ideal: np.ndarray | List[float],
    *,
    x_label: str = "x1",
    y_label: str = "Y",
) -> str:
    """Save baseline CSV: x, Y_exp, Y_ideal."""
    x = np.asarray(x, dtype=float)
    ye = np.asarray(y_exp, dtype=float)
    yi = np.asarray(y_ideal, dtype=float)

    cols = [x_label, f"{y_label}_exp", f"{y_label}_ideal"]
    rows = [[_fmt(x[i]), _fmt(ye[i]), _fmt(yi[i])] for i in range(len(x))]
    return _write_csv(path, cols, rows)
