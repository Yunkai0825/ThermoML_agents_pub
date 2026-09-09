"""
Non-ideality calculator for molar volume and viscosity.

Given a data block (columns + rows), identifies the independent variable
(typically mole fraction) and dependent properties (molar volume, viscosity),
then computes deviation from ideal mixing and classifies the non-ideality.

Sign convention
---------------
- Molar volume:  attractive = V_E < 0 (contraction)
- Viscosity:     attractive = Δη > 0  (increase from ideal — stronger interactions)
"""

from __future__ import annotations

import math
import logging
import re
from dataclasses import dataclass, field
from typing import Optional

log = logging.getLogger("nonideality")


# ── Pattern matching for column identification ────────────────────────────

_MOLE_FRAC_PATTERNS = [
    re.compile(r"mole\s*frac", re.I),
    re.compile(r"x\s*\d*", re.I),
    re.compile(r"Mole fraction", re.I),
]

_VOLUME_PATTERNS = [
    re.compile(r"molar\s*vol", re.I),
    re.compile(r"density", re.I),
    re.compile(r"V\s*m", re.I),
    re.compile(r"specific\s*vol", re.I),
]

_VISCOSITY_PATTERNS = [
    re.compile(r"viscos", re.I),
    re.compile(r"η", re.I),
    re.compile(r"eta", re.I),
]


def _match_any(text: str, patterns: list[re.Pattern]) -> bool:
    return any(p.search(text) for p in patterns)


def _is_mole_fraction(col_name: str) -> bool:
    return _match_any(col_name, _MOLE_FRAC_PATTERNS)


def _is_volume(col_name: str) -> bool:
    return _match_any(col_name, _VOLUME_PATTERNS)


def _is_viscosity(col_name: str) -> bool:
    return _match_any(col_name, _VISCOSITY_PATTERNS)


# ── Data structures ───────────────────────────────────────────────────────

@dataclass
class DeviationPoint:
    x: float               # mole fraction
    measured: float         # measured value
    ideal: float            # ideal mixing value
    deviation: float        # measured - ideal (for volume: V_E; for viscosity: Δη)


@dataclass
class FitResult:
    """Result of a Redlich-Kister polynomial fit to excess/deviation data."""
    coefficients: list[float]   # A0, A1, A2, ...
    order: int
    rmse: float
    r_squared: float


@dataclass
class PropertyAnalysis:
    """Analysis result for one property (volume or viscosity)."""
    property_name: str
    column_index: int
    x_column_index: int
    x_column_name: str
    pure1_value: float       # value at x=0
    pure2_value: float       # value at x=1
    points: list[DeviationPoint]
    fit: Optional[FitResult]
    classification: str      # "attractive", "repulsive", "mixed", "ideal"
    is_density: bool = False # True if the raw column is density (inverted to vol)


@dataclass
class AnalysisResult:
    """Complete analysis of a data block."""
    success: bool
    error: str = ""
    x_column: str = ""
    properties_analyzed: list[PropertyAnalysis] = field(default_factory=list)
    system_class: str = ""   # combined classification label


# ── Ideal mixing models ──────────────────────────────────────────────────

def ideal_volume(x: float, v1: float, v2: float) -> float:
    """Linear (Raoult's law) ideal molar volume: V_id = x*V2 + (1-x)*V1."""
    return (1 - x) * v1 + x * v2


def ideal_viscosity_log(x: float, eta1: float, eta2: float) -> float:
    """Logarithmic ideal viscosity (Arrhenius): ln(η_id) = x*ln(η2) + (1-x)*ln(η1)."""
    if eta1 <= 0 or eta2 <= 0:
        return (1 - x) * eta1 + x * eta2  # fallback to linear
    return math.exp((1 - x) * math.log(eta1) + x * math.log(eta2))


# ── Redlich-Kister fit ───────────────────────────────────────────────────

def _redlich_kister_basis(x: float, order: int) -> list[float]:
    """Return [x(1-x), x(1-x)(1-2x), x(1-x)(1-2x)^2, ...] up to order."""
    x1x = x * (1 - x)
    t = 1 - 2 * x
    basis = []
    t_power = 1.0
    for _ in range(order):
        basis.append(x1x * t_power)
        t_power *= t
    return basis


def fit_redlich_kister(x_vals: list[float], dev_vals: list[float],
                       max_order: int = 5) -> FitResult:
    """Least-squares Redlich-Kister fit of deviation data.

    Y_E = x(1-x) * Σ A_k (1-2x)^k

    Uses normal equations (A^T A c = A^T b) — no numpy required.
    Tries orders 1..max_order, picks the one with best adjusted R².
    """
    n = len(x_vals)
    if n < 3:
        return FitResult(coefficients=[], order=0, rmse=0.0, r_squared=0.0)

    y_mean = sum(dev_vals) / n
    ss_tot = sum((y - y_mean) ** 2 for y in dev_vals)
    if ss_tot < 1e-30:
        return FitResult(coefficients=[0.0], order=1, rmse=0.0, r_squared=1.0)

    best: Optional[FitResult] = None

    for order in range(1, min(max_order + 1, n)):
        # Build A matrix (n x order) and b vector
        A = [_redlich_kister_basis(x, order) for x in x_vals]
        b = list(dev_vals)

        # Normal equations: (A^T A) c = A^T b
        AtA = [[0.0] * order for _ in range(order)]
        Atb = [0.0] * order
        for i in range(n):
            for j in range(order):
                Atb[j] += A[i][j] * b[i]
                for k in range(order):
                    AtA[j][k] += A[i][j] * A[i][k]

        # Solve via Gaussian elimination
        coeffs = _solve_linear(AtA, Atb)
        if coeffs is None:
            continue

        # Compute residuals
        ss_res = 0.0
        for i in range(n):
            pred = sum(coeffs[j] * A[i][j] for j in range(order))
            ss_res += (b[i] - pred) ** 2

        rmse = math.sqrt(ss_res / n)
        r2 = 1.0 - ss_res / ss_tot

        # Adjusted R² for model selection
        if n - order - 1 > 0:
            r2_adj = 1.0 - (1.0 - r2) * (n - 1) / (n - order - 1)
        else:
            r2_adj = r2

        cand = FitResult(coefficients=coeffs, order=order, rmse=rmse, r_squared=r2)
        if best is None or r2_adj > (1.0 - (1.0 - best.r_squared) * (n - 1) / max(n - best.order - 1, 1)):
            best = cand

    return best or FitResult(coefficients=[], order=0, rmse=0.0, r_squared=0.0)


def _solve_linear(A: list[list[float]], b: list[float]) -> Optional[list[float]]:
    """Solve Ax=b via Gaussian elimination with partial pivoting."""
    n = len(b)
    # Augmented matrix
    M = [row[:] + [b[i]] for i, row in enumerate(A)]

    for col in range(n):
        # Partial pivoting
        max_row = col
        for row in range(col + 1, n):
            if abs(M[row][col]) > abs(M[max_row][col]):
                max_row = row
        M[col], M[max_row] = M[max_row], M[col]

        if abs(M[col][col]) < 1e-15:
            return None

        for row in range(col + 1, n):
            factor = M[row][col] / M[col][col]
            for j in range(col, n + 1):
                M[row][j] -= factor * M[col][j]

    # Back substitution
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = M[i][n]
        for j in range(i + 1, n):
            s -= M[i][j] * x[j]
        x[i] = s / M[i][i]

    return x


# ── Classification ────────────────────────────────────────────────────────

def classify_deviation(points: list[DeviationPoint], prop_type: str) -> str:
    """Classify non-ideality.

    For volume: deviation = V_E = V_meas - V_ideal
        attractive = V_E < 0 (molecules pack tighter)
        repulsive  = V_E > 0 (molecules repel)

    For viscosity: deviation = Δη = η_meas - η_ideal
        attractive = Δη > 0 (stronger interactions, higher viscosity)
        repulsive  = Δη < 0 (weaker interactions, lower viscosity)
    """
    interior = [p for p in points if 0.05 < p.x < 0.95]
    if not interior:
        return "insufficient_data"

    deviations = [p.deviation for p in interior]
    pos = sum(1 for d in deviations if d > 0)
    neg = sum(1 for d in deviations if d < 0)
    total = len(deviations)

    # Threshold: 80% dominance to classify
    if prop_type == "volume":
        if neg / total >= 0.8:
            return "attractive"
        elif pos / total >= 0.8:
            return "repulsive"
        else:
            return "mixed"
    elif prop_type == "viscosity":
        if pos / total >= 0.8:
            return "attractive"
        elif neg / total >= 0.8:
            return "repulsive"
        else:
            return "mixed"
    return "unknown"


# ── Main analysis entry point ─────────────────────────────────────────

def _parse_float(val) -> Optional[float]:
    """Try to parse a float from a cell value."""
    if val is None or val == '':
        return None
    try:
        return float(val)
    except (ValueError, TypeError) as exc:
        log.debug("Failed to parse float value %r: %s", val, exc)
        return None


def analyze_block(columns: list[dict], rows: list[list],
                  pure1_idx: int = 0, pure2_idx: int = -1) -> AnalysisResult:
    """Analyze a data block for non-ideality.

    Parameters
    ----------
    columns : list of dict
        Column definitions: [{"name": str, "type": str}, ...].
    rows : list of list
        Data rows (parallel to columns).
    pure1_idx, pure2_idx : int
        Row indices for pure-component-1 (x≈0) and pure-component-2 (x≈1).
        Defaults to first and last rows.

    Returns
    -------
    AnalysisResult with analysis for each detected property.
    """
    if not columns or not rows:
        return AnalysisResult(success=False, error="No data provided.")

    # Step 1: identify mole-fraction column
    x_col = None
    for i, col in enumerate(columns):
        name = col.get("name", "")
        if col.get("type") == "uncertainty":
            continue
        if _is_mole_fraction(name):
            x_col = i
            break

    if x_col is None:
        return AnalysisResult(success=False, error="No mole fraction column found.")

    # Step 2: identify property columns
    prop_cols = []
    for i, col in enumerate(columns):
        if i == x_col or col.get("type") == "uncertainty":
            continue
        name = col.get("name", "")
        if _is_volume(name):
            is_density = bool(re.search(r"density", name, re.I))
            prop_cols.append((i, "volume", name, is_density))
        elif _is_viscosity(name):
            prop_cols.append((i, "viscosity", name, False))

    if not prop_cols:
        return AnalysisResult(
            success=False,
            error="No molar volume or viscosity columns detected. "
                  "Found columns: " + ", ".join(c.get("name", "") for c in columns),
        )

    # Step 3: extract numeric data
    # Sort by x for cleaner analysis
    data_rows = []
    for row in rows:
        x_val = _parse_float(row[x_col])
        if x_val is not None:
            data_rows.append((x_val, row))
    data_rows.sort(key=lambda t: t[0])

    if len(data_rows) < 3:
        return AnalysisResult(success=False, error="Insufficient data rows (need ≥ 3).")

    # Get endpoint rows for pure component values
    if pure2_idx < 0:
        pure2_idx = len(data_rows) + pure2_idx
    row1 = data_rows[pure1_idx][1]
    row2 = data_rows[pure2_idx][1]

    analyses = []
    for col_idx, prop_type, col_name, is_density in prop_cols:
        v1_raw = _parse_float(row1[col_idx])
        v2_raw = _parse_float(row2[col_idx])
        if v1_raw is None or v2_raw is None:
            continue

        # For density, we convert to molar volume later if possible.
        # For now, treat density deviation similarly (just inverted sign).
        v1 = v1_raw
        v2 = v2_raw

        ideal_fn = ideal_volume if prop_type == "volume" else ideal_viscosity_log

        points = []
        for x_val, row in data_rows:
            measured = _parse_float(row[col_idx])
            if measured is None:
                continue
            ideal_val = ideal_fn(x_val, v1, v2)
            deviation = measured - ideal_val
            # For density, deviation sign is inverted vs molar volume
            if is_density:
                deviation = -deviation
            points.append(DeviationPoint(x=x_val, measured=measured,
                                         ideal=ideal_val, deviation=deviation))

        if len(points) < 3:
            continue

        # Fit Redlich-Kister to deviation
        x_vals = [p.x for p in points]
        dev_vals = [p.deviation for p in points]
        fit = fit_redlich_kister(x_vals, dev_vals)

        classification = classify_deviation(points, prop_type)

        analyses.append(PropertyAnalysis(
            property_name=col_name,
            column_index=col_idx,
            x_column_index=x_col,
            x_column_name=columns[x_col].get("name", "x"),
            pure1_value=v1,
            pure2_value=v2,
            points=points,
            fit=fit,
            classification=classification,
            is_density=is_density,
        ))

    if not analyses:
        return AnalysisResult(success=False, error="Could not compute deviations for any property.")

    # System-level classification
    class_labels = [a.classification for a in analyses]
    if all(c == "attractive" for c in class_labels):
        system_class = "Both attractive"
    elif all(c == "repulsive" for c in class_labels):
        system_class = "Both repulsive"
    elif "attractive" in class_labels and "repulsive" in class_labels:
        # Find which is which
        vol_cls = next((a.classification for a in analyses
                        if "vol" in a.property_name.lower() or a.is_density), None)
        visc_cls = next((a.classification for a in analyses
                         if "visc" in a.property_name.lower()), None)
        if vol_cls and visc_cls and vol_cls != visc_cls:
            system_class = f"Volume {vol_cls}, Viscosity {visc_cls}"
        else:
            system_class = "Mixed"
    else:
        system_class = ", ".join(set(class_labels))

    return AnalysisResult(
        success=True,
        x_column=columns[x_col].get("name", "x"),
        properties_analyzed=analyses,
        system_class=system_class,
    )


def analyze_custom_csv(csv_text: str) -> AnalysisResult:
    """Analyze pasted CSV text.

    Expects first row as headers, subsequent rows as data.
    Columns should include a mole fraction and at least one of
    molar volume / density / viscosity.
    """
    lines = [l.strip() for l in csv_text.strip().split('\n') if l.strip()]
    if len(lines) < 3:
        return AnalysisResult(success=False, error="Need at least a header + 2 data rows.")

    # Detect delimiter
    header = lines[0]
    if '\t' in header:
        sep = '\t'
    elif ';' in header:
        sep = ';'
    else:
        sep = ','

    col_names = [c.strip() for c in header.split(sep)]
    columns = [{"name": n, "type": "variable"} for n in col_names]

    rows = []
    for line in lines[1:]:
        cells = [c.strip() for c in line.split(sep)]
        # Pad short rows
        while len(cells) < len(col_names):
            cells.append('')
        rows.append(cells)

    return analyze_block(columns, rows)


def result_to_dict(result: AnalysisResult) -> dict:
    """Convert AnalysisResult to JSON-serializable dict."""
    if not result.success:
        return {"success": False, "error": result.error}

    props = []
    for a in result.properties_analyzed:
        pts = [
            {"x": p.x, "measured": p.measured, "ideal": p.ideal, "deviation": p.deviation}
            for p in a.points
        ]
        fit_d = None
        if a.fit and a.fit.coefficients:
            fit_d = {
                "coefficients": [round(c, 8) for c in a.fit.coefficients],
                "order": a.fit.order,
                "rmse": round(a.fit.rmse, 8),
                "r_squared": round(a.fit.r_squared, 6),
            }
        props.append({
            "property_name": a.property_name,
            "classification": a.classification,
            "pure1_value": a.pure1_value,
            "pure2_value": a.pure2_value,
            "x_column_name": a.x_column_name,
            "is_density": a.is_density,
            "n_points": len(a.points),
            "points": pts,
            "fit": fit_d,
        })

    return {
        "success": True,
        "x_column": result.x_column,
        "system_class": result.system_class,
        "properties": props,
    }
