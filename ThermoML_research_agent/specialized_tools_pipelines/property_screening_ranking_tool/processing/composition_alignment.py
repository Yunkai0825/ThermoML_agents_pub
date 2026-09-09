"""Build a self-consistent tri-basis composition translation table.

The irreducible normalized representations are mole fraction ``x``, mass
fraction ``w``, and volume fraction ``phi``.  Other ThermoML composition
descriptors are interpreted as constraints on those representations.  A
candidate field group is accepted only when its explicitly permitted
conversion paths identify one physical composition.  Independent sufficient
groups then cross-validate that composition row by row.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Any, Mapping, Sequence

import numpy as np

from ..tool_settings import (
    COMPOSITION_GROUP_SCORE_WEIGHTS,
    COMPOSITION_SUPPORT_REFERENCE_POINTS,
)


FUNDAMENTAL_REPRESENTATIONS = (
    "mole_fraction",
    "mass_fraction",
    "volume_fraction",
)

_DIRECT_BASES = set(FUNDAMENTAL_REPRESENTATIONS)
_RATIO_BASES = {"molality", "amount_ratio", "mass_ratio"}
_CONCENTRATION_BASES = {"molarity", "mass_concentration"}
_BASIS_PRIORITY = {
    "mole_fraction": 100,
    "mass_fraction": 90,
    "volume_fraction": 80,
    "molality": 70,
    "amount_ratio": 65,
    "mass_ratio": 60,
    "molarity": 50,
    "mass_concentration": 45,
}


@dataclass(frozen=True)
class CompositionField:
    """One authoritative component-linked composition column."""

    role: str
    basis: str
    component_num_id: str
    local_id: str
    global_id: str
    values: np.ndarray
    scope_component_num_ids: tuple[str, ...] = ()


@dataclass
class _CandidateGroup:
    group_id: str
    fields: tuple[CompositionField, ...]
    bridge: str | None
    bridge_source_ids: tuple[str, ...]
    relation: str
    conversion_paths: tuple[str, ...]
    mole_fractions: np.ndarray
    valid: np.ndarray
    exact_without_empirical_bridge: bool

    @property
    def valid_rows(self) -> int:
        return int(np.count_nonzero(self.valid))

    @property
    def information_count(self) -> int:
        return len(self.fields) + int(self.bridge is not None)

    @property
    def token_set(self) -> frozenset[str]:
        tokens = {f"field:{field.local_id}" for field in self.fields}
        if self.bridge is not None:
            tokens.add(f"bridge:{self.bridge}")
        return frozenset(tokens)

    @property
    def source_basis_label(self) -> str:
        bases = sorted({field.basis for field in self.fields})
        return bases[0] if len(bases) == 1 else "mixed:" + "+".join(bases)

    def score_breakdown(
        self,
        *,
        row_relevance_scores: np.ndarray,
        total_relevance: float,
        component_count: int,
    ) -> dict[str, Any]:
        weighted_support = float(
            np.sum(row_relevance_scores[self.valid])
        )
        priority = min(
            (_BASIS_PRIORITY.get(field.basis, 0) for field in self.fields),
            default=0,
        )
        components = {
            "coverage": (
                weighted_support / total_relevance
                if total_relevance > 0.0
                else 0.0
            ),
            "support": min(
                1.0,
                weighted_support / COMPOSITION_SUPPORT_REFERENCE_POINTS,
            ),
            "exactness": (
                1.0 if self.exact_without_empirical_bridge else 0.5
            ),
            "bridge_independence": (
                1.0 if self.bridge is None else 0.5
            ),
            "basis_directness": priority / 100.0,
            "parsimony": min(
                1.0,
                max(1, component_count - 1) / self.information_count,
            ),
        }
        score = sum(
            COMPOSITION_GROUP_SCORE_WEIGHTS[name] * value
            for name, value in components.items()
        )
        return {
            "composite_score": float(score),
            "components": components,
            "weights": dict(COMPOSITION_GROUP_SCORE_WEIGHTS),
            "effective_support": weighted_support,
        }


@dataclass(frozen=True)
class CompositionAlignmentResult:
    coordinates: np.ndarray | None
    coordinate_comp_num_ids: tuple[str, ...]
    coordinate_bases: tuple[str, ...]
    plan: dict[str, Any]
    error_code: str | None = None
    error_message: str | None = None
    error_details: dict[str, Any] | None = None


def _unit_vector(size: int, index: int) -> np.ndarray:
    result = np.zeros(size, dtype=float)
    result[index] = 1.0
    return result


def _fraction_equation(
    representation: str,
    component_index: int,
    value: float,
    masses: np.ndarray,
    pure_volumes: np.ndarray | None,
    scope_indexes: tuple[int, ...],
) -> tuple[np.ndarray | None, str]:
    """Translate one fundamental fraction into an equation on mole amounts."""
    size = len(masses)
    selected = _unit_vector(size, component_index)
    scope = np.zeros(size, dtype=float)
    scope[list(scope_indexes or tuple(range(size)))] = 1.0
    scoped = bool(scope_indexes)
    if representation == "mole_fraction":
        return (
            selected - value * scope,
            (
                "reported solvent-subsystem mole fraction -> scoped mole "
                "constraint"
                if scoped
                else "reported mole fraction -> mole representation"
            ),
        )
    if representation == "mass_fraction":
        if not np.all(np.isfinite(masses)):
            return None, "mass fraction requires every component molar mass"
        return (
            masses[component_index] * selected - value * masses * scope,
            (
                "reported solvent-subsystem mass fraction -> scoped mass "
                "constraint -> mole representation"
                if scoped
                else "reported mass fraction -> mole representation via "
                "formula molar masses"
            ),
        )
    if representation == "volume_fraction":
        if pure_volumes is None or not np.all(np.isfinite(pure_volumes)):
            return (
                None,
                "volume fraction requires definition- and phase-compatible "
                "component molar volumes",
            )
        return (
            pure_volumes[component_index] * selected
            - value * pure_volumes * scope,
            (
                "reported solvent-subsystem volume fraction -> scoped volume "
                "constraint -> mole representation via component molar volumes"
                if scoped
                else "reported volume fraction -> mole representation via "
                "component molar-volume bridge"
            ),
        )
    return None, f"unsupported fundamental representation {representation}"


def _ratio_equation(
    field: CompositionField,
    value: float,
    component_index: int,
    solvent_index: int | None,
    masses: np.ndarray,
) -> tuple[np.ndarray | None, str]:
    """Translate molality or an amount/mass ratio into a mole constraint."""
    size = len(masses)
    selected = _unit_vector(size, component_index)
    reference = solvent_index
    if reference is None and size == 2:
        reference = 1 - component_index
    if field.basis == "molality":
        if (
            solvent_index is None
            or solvent_index == component_index
            or not np.isfinite(masses[solvent_index])
        ):
            return None, "molality requires one explicit solvent and its molar mass"
        return (
            selected
            - value
            * masses[solvent_index]
            / 1000.0
            * _unit_vector(size, solvent_index),
            "molality -> solute/solvent amount ratio -> mole representation",
        )
    if reference is None or reference == component_index:
        return None, f"{field.basis} requires one unambiguous reference component"
    if field.basis == "amount_ratio":
        return (
            selected - value * _unit_vector(size, reference),
            "amount ratio -> mole representation",
        )
    if field.basis == "mass_ratio":
        if not np.all(np.isfinite(masses)):
            return None, "mass ratio requires both component molar masses"
        return (
            masses[component_index] * selected
            - value * masses[reference] * _unit_vector(size, reference),
            "mass ratio -> mass representation -> mole representation",
        )
    return None, f"unsupported derived ratio {field.basis}"


def _concentration_bridge_equation(
    field: CompositionField,
    value: float,
    bridge_kind: str,
    bridge_value: float,
    component_index: int,
    masses: np.ndarray,
) -> tuple[np.ndarray | None, str]:
    """Use a same-row total density to normalize one concentration field."""
    size = len(masses)
    bridge_family = bridge_kind.split("::", 1)[0]
    if not np.isfinite(bridge_value) or bridge_value <= 0:
        return None, f"{bridge_kind} is absent or nonpositive"
    selected = _unit_vector(size, component_index)
    if field.basis == "molarity" and bridge_family == "amount_density":
        x_value = value * 1000.0 / bridge_value
        return (
            selected - x_value * np.ones(size),
            "molarity + total amount density -> mole fraction",
        )
    if field.basis == "molarity" and bridge_family == "mass_density":
        if not np.all(np.isfinite(masses)):
            return None, "molarity + mass density requires molar masses"
        w_value = value * masses[component_index] / bridge_value
        return (
            masses[component_index] * selected - w_value * masses,
            "molarity + total mass density -> mass fraction -> mole fraction",
        )
    if (
        field.basis == "mass_concentration"
        and bridge_family == "mass_density"
    ):
        if not np.all(np.isfinite(masses)):
            return None, "mass concentration requires molar masses"
        w_value = value / bridge_value
        return (
            masses[component_index] * selected - w_value * masses,
            "mass concentration + total mass density -> mass fraction -> "
            "mole fraction",
        )
    if (
        field.basis == "mass_concentration"
        and bridge_family == "amount_density"
    ):
        if not np.isfinite(masses[component_index]):
            return None, "mass concentration requires component molar mass"
        x_value = value * 1000.0 / (
            masses[component_index] * bridge_value
        )
        return (
            selected - x_value * np.ones(size),
            "mass concentration + total amount density -> mole fraction",
        )
    return None, f"{field.basis} cannot use {bridge_kind}"


def _relative_concentration_equations(
    fields: Sequence[CompositionField],
    values: Sequence[float],
    positions: Mapping[str, int],
    masses: np.ndarray,
) -> tuple[list[np.ndarray] | None, list[str]]:
    """Remove the unknown common volume scale from concentration groups."""
    equations: list[np.ndarray] = []
    paths: list[str] = []
    grouped: dict[str, list[tuple[CompositionField, float]]] = {}
    for field, value in zip(fields, values):
        if field.basis in _CONCENTRATION_BASES:
            grouped.setdefault(field.basis, []).append((field, value))
    for basis, observations in grouped.items():
        if len(observations) < 2:
            continue
        reference_field, reference_value = observations[0]
        reference_index = positions[reference_field.component_num_id]
        if basis == "molarity":
            reference_amount = reference_value
        else:
            if not np.isfinite(masses[reference_index]):
                return None, ["mass concentration requires molar masses"]
            reference_amount = reference_value / masses[reference_index]
        if reference_amount < 0:
            return None, ["negative concentration is not a composition"]
        for field, value in observations[1:]:
            component_index = positions[field.component_num_id]
            if basis == "molarity":
                amount = value
            else:
                if not np.isfinite(masses[component_index]):
                    return None, ["mass concentration requires molar masses"]
                amount = value / masses[component_index]
            if amount < 0:
                return None, ["negative concentration is not a composition"]
            equations.append(
                reference_amount * _unit_vector(len(masses), component_index)
                - amount * _unit_vector(len(masses), reference_index)
            )
        paths.append(
            f"{basis} component ratios cancel the common sample-volume scale"
        )
    return equations, paths


def _solve_mole_representation(
    equations: Sequence[np.ndarray],
    component_count: int,
    closure_atol: float,
    consistency_atol: float,
) -> np.ndarray | None:
    """Solve only after chemical conversions have produced mole constraints."""
    if not equations:
        return None
    matrix = np.asarray(equations, dtype=float)
    norms = np.linalg.norm(matrix, axis=1)
    if np.any(~np.isfinite(norms)) or np.any(norms <= closure_atol):
        return None
    normalized = matrix / norms[:, np.newaxis]
    # N-1 is a consequence of identifying one normalized vector, not a rule
    # for how many raw ThermoML fields must be supplied.
    if np.linalg.matrix_rank(normalized, tol=1e-10) != component_count - 1:
        return None
    augmented = np.vstack((normalized, np.ones(component_count)))
    target = np.concatenate((np.zeros(len(normalized)), np.ones(1)))
    result, _residuals, rank, _singular = np.linalg.lstsq(
        augmented, target, rcond=None
    )
    if rank != component_count:
        return None
    if np.max(np.abs(normalized @ result)) > consistency_atol:
        return None
    if abs(float(result.sum()) - 1.0) > closure_atol:
        return None
    if np.any(result < -closure_atol) or np.any(
        result > 1.0 + closure_atol
    ):
        return None
    return np.clip(result, 0.0, 1.0)


def _evaluate_group(
    selected: tuple[CompositionField, ...],
    bridge: str | None,
    order: tuple[str, ...],
    masses: np.ndarray,
    pure_volumes: np.ndarray | None,
    solvent_index: int | None,
    bridge_values: Mapping[str, np.ndarray],
    bridge_source_ids: Mapping[str, Sequence[str]],
    closure_atol: float,
    consistency_atol: float,
) -> _CandidateGroup | None:
    row_count = len(selected[0].values)
    component_count = len(order)
    positions = {component: index for index, component in enumerate(order)}
    mole_fractions = np.full(
        (row_count, component_count), np.nan, dtype=float
    )
    valid = np.zeros(row_count, dtype=bool)
    path_catalog: set[str] = set()
    for row_index in range(row_count):
        values = [float(field.values[row_index]) for field in selected]
        if not all(np.isfinite(value) for value in values):
            continue
        equations: list[np.ndarray] = []
        row_paths: list[str] = []
        failed = False
        for field, value in zip(selected, values):
            component_index = positions[field.component_num_id]
            if field.basis in _DIRECT_BASES:
                equation, path = _fraction_equation(
                    field.basis,
                    component_index,
                    value,
                    masses,
                    pure_volumes,
                    tuple(
                        positions[component]
                        for component in field.scope_component_num_ids
                        if component in positions
                    ),
                )
            elif field.basis in _RATIO_BASES:
                equation, path = _ratio_equation(
                    field,
                    value,
                    component_index,
                    solvent_index,
                    masses,
                )
            elif bridge is not None:
                equation, path = _concentration_bridge_equation(
                    field,
                    value,
                    bridge,
                    float(bridge_values[bridge][row_index]),
                    component_index,
                    masses,
                )
            else:
                equation, path = None, (
                    f"{field.basis} retains an unknown common scale"
                )
            if (
                field.basis in _DIRECT_BASES | _RATIO_BASES
                and equation is None
            ):
                failed = True
                break
            if equation is not None:
                equations.append(equation)
                row_paths.append(path)
        if failed:
            continue
        if bridge is None:
            relative, paths = _relative_concentration_equations(
                selected, values, positions, masses
            )
            if relative is None:
                continue
            equations.extend(relative)
            row_paths.extend(paths)
        result = _solve_mole_representation(
            equations,
            component_count,
            closure_atol,
            consistency_atol,
        )
        if result is not None:
            mole_fractions[row_index] = result
            valid[row_index] = True
            path_catalog.update(row_paths)
    if not np.any(valid):
        return None
    bases = sorted({field.basis for field in selected})
    label = bases[0] if len(bases) == 1 else "mixed_" + "_".join(bases)
    local_ids = "+".join(sorted(field.local_id for field in selected))
    group_id = f"{label}:{local_ids}"
    if bridge is not None:
        group_id += f":bridge={bridge}"
    empirical = (
        bridge is not None
        or any(field.basis == "volume_fraction" for field in selected)
    )
    return _CandidateGroup(
        group_id=group_id,
        fields=selected,
        bridge=bridge,
        bridge_source_ids=tuple(
            bridge_source_ids.get(bridge, ())
        )
        if bridge
        else (),
        relation=(
            "chemically gated composition constraints identify one "
            "mole-fraction vector"
        ),
        conversion_paths=tuple(sorted(path_catalog)),
        mole_fractions=mole_fractions,
        valid=valid,
        exact_without_empirical_bridge=not empirical,
    )


def _build_minimal_groups(
    fields: Sequence[CompositionField],
    order: tuple[str, ...],
    masses: np.ndarray,
    pure_volumes: np.ndarray | None,
    solvent_index: int | None,
    bridge_values: Mapping[str, np.ndarray],
    bridge_source_ids: Mapping[str, Sequence[str]],
    closure_atol: float,
    consistency_atol: float,
) -> tuple[list[_CandidateGroup], list[_CandidateGroup]]:
    groups: list[_CandidateGroup] = []
    # Concentrations can retain one latent scale, so a minimal identifying
    # group may contain N fields rather than N-1.
    maximum_fields = min(len(order), len(fields))
    for size in range(1, maximum_fields + 1):
        for selected in combinations(fields, size):
            bridge_options: tuple[str | None, ...] = (None,)
            if any(
                field.basis in _CONCENTRATION_BASES for field in selected
            ):
                bridge_options += tuple(sorted(bridge_values))
            for bridge in bridge_options:
                candidate = _evaluate_group(
                    tuple(selected),
                    bridge,
                    order,
                    masses,
                    pure_volumes,
                    solvent_index,
                    bridge_values,
                    bridge_source_ids,
                    closure_atol,
                    consistency_atol,
                )
                if candidate is not None:
                    groups.append(candidate)
    minimal: list[_CandidateGroup] = []
    for candidate in sorted(
        groups, key=lambda item: (len(item.token_set), item.group_id)
    ):
        if any(
            existing.token_set < candidate.token_set
            for existing in minimal
        ):
            continue
        minimal.append(candidate)
    return minimal, groups


def _tri_basis_state(
    mole_fractions: np.ndarray,
    masses: np.ndarray,
    pure_volumes: np.ndarray | None,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    mass_fractions: np.ndarray | None = None
    volume_fractions: np.ndarray | None = None
    if np.all(np.isfinite(masses)):
        mass_terms = mole_fractions * masses[np.newaxis, :]
        mass_fractions = mass_terms / mass_terms.sum(axis=1, keepdims=True)
    if pure_volumes is not None and np.all(np.isfinite(pure_volumes)):
        volume_terms = mole_fractions * pure_volumes[np.newaxis, :]
        volume_fractions = volume_terms / volume_terms.sum(
            axis=1, keepdims=True
        )
    return mass_fractions, volume_fractions


def _row_values(
    values: np.ndarray | None,
    row_index: int,
    order: tuple[str, ...],
) -> dict[str, float] | None:
    if values is None:
        return None
    return {
        component: float(values[row_index, index])
        for index, component in enumerate(order)
    }


def _volumetric_state_rows(
    mole_fractions: np.ndarray,
    valid_rows: np.ndarray,
    masses: np.ndarray,
    row_ids: Sequence[str],
    bridge_values: Mapping[str, np.ndarray],
    relative_tolerance: float,
) -> tuple[list[dict[str, Any]], int]:
    """Cross-check equivalent bulk volume/density measurements per row."""
    records: list[dict[str, Any]] = []
    conflicts = 0
    for row_index, row_id in enumerate(row_ids):
        evidence: list[dict[str, Any]] = []
        mass_density_values: list[float] = []
        amount_density_values: list[float] = []
        for bridge_id, values in sorted(bridge_values.items()):
            value = float(values[row_index])
            if not np.isfinite(value) or value <= 0:
                continue
            family = bridge_id.split("::", 1)[0]
            evidence.append(
                {
                    "bridge_id": bridge_id,
                    "family": family,
                    "canonical_value": value,
                }
            )
            if family == "mass_density":
                mass_density_values.append(value)
            elif family == "amount_density":
                amount_density_values.append(value)
        if not evidence:
            records.append(
                {"BLKpoint_id": row_id, "status": "unavailable"}
            )
            continue

        mixture_mass = None
        if valid_rows[row_index] and np.all(np.isfinite(masses)):
            mixture_mass = float(np.dot(mole_fractions[row_index], masses))
            if mixture_mass <= 0:
                mixture_mass = None
        all_amount_equivalents = list(amount_density_values)
        if mixture_mass is not None:
            all_amount_equivalents.extend(
                value * 1000.0 / mixture_mass
                for value in mass_density_values
            )

        def relative_spread(values: Sequence[float]) -> float:
            if len(values) < 2:
                return 0.0
            scale = max(abs(float(np.mean(values))), 1e-300)
            return float((max(values) - min(values)) / scale)

        mass_spread = relative_spread(mass_density_values)
        amount_spread = relative_spread(amount_density_values)
        cross_spread = relative_spread(all_amount_equivalents)
        maximum_spread = max(mass_spread, amount_spread, cross_spread)
        if maximum_spread > relative_tolerance:
            conflicts += 1
            records.append(
                {
                    "BLKpoint_id": row_id,
                    "status": "conflicting_bulk_volume_evidence",
                    "mixture_molar_mass_g_mol": mixture_mass,
                    "maximum_relative_disagreement": maximum_spread,
                    "evidence": evidence,
                }
            )
            continue

        amount_density = (
            float(np.mean(all_amount_equivalents))
            if all_amount_equivalents
            else None
        )
        mass_density = (
            amount_density * mixture_mass / 1000.0
            if amount_density is not None and mixture_mass is not None
            else (
                float(np.mean(mass_density_values))
                if mass_density_values
                else None
            )
        )
        records.append(
            {
                "BLKpoint_id": row_id,
                "status": "self_consistent",
                "mixture_molar_mass_g_mol": mixture_mass,
                "mass_density_kg_m3": mass_density,
                "amount_density_mol_m3": amount_density,
                "molar_volume_m3_mol": (
                    1.0 / amount_density
                    if amount_density is not None
                    else None
                ),
                "specific_volume_m3_kg": (
                    1.0 / mass_density
                    if mass_density is not None
                    else None
                ),
                "maximum_relative_disagreement": maximum_spread,
                "evidence": evidence,
            }
        )
    return records, conflicts


def solve_composition_alignment(
    *,
    component_order: tuple[str, ...],
    fields: Sequence[CompositionField],
    molar_masses_g_mol: Mapping[str, float | None],
    row_ids: Sequence[str],
    solvent_comp_num_id: str | None,
    bridge_values: Mapping[str, np.ndarray],
    bridge_source_ids: Mapping[str, Sequence[str]],
    pure_molar_volumes: Mapping[str, float] | None,
    pure_volume_evidence: Sequence[dict[str, Any]],
    closure_atol: float,
    consistency_atol: float,
    volumetric_consistency_rtol: float,
    row_relevance_scores: Sequence[float] | None = None,
) -> CompositionAlignmentResult:
    """Return canonical mole coordinates and the complete tri-basis table."""
    order = tuple(component_order)
    component_count = len(order)
    row_count = len(row_ids)
    relevance = np.asarray(
        row_relevance_scores
        if row_relevance_scores is not None
        else np.ones(row_count, dtype=float),
        dtype=float,
    )
    if len(relevance) != row_count:
        raise ValueError("row relevance length does not match row_ids")
    if np.any(~np.isfinite(relevance)) or np.any(relevance < 0.0):
        raise ValueError("row relevance scores must be finite and nonnegative")
    relevance = np.clip(relevance, 0.0, 1.0)
    total_relevance = float(np.sum(relevance))
    masses = np.asarray(
        [
            molar_masses_g_mol.get(component, np.nan) or np.nan
            for component in order
        ],
        dtype=float,
    )
    pure_volumes = None
    if pure_molar_volumes is not None and all(
        component in pure_molar_volumes for component in order
    ):
        pure_volumes = np.asarray(
            [pure_molar_volumes[component] for component in order],
            dtype=float,
        )
    if component_count == 1:
        mole = np.ones((row_count, 1), dtype=float)
        mass, volume = _tri_basis_state(mole, masses, pure_volumes)
        return CompositionAlignmentResult(
            coordinates=np.empty((row_count, 0), dtype=float),
            coordinate_comp_num_ids=(),
            coordinate_bases=(),
            plan={
                "kind": "tri_basis_composition_translation",
                "irreducible_representations": list(
                    FUNDAMENTAL_REPRESENTATIONS
                ),
                "degrees_of_freedom": 0,
                "component_order": list(order),
                "molar_masses_g_mol": {
                    order[0]: (
                        float(masses[0])
                        if np.isfinite(masses[0])
                        else None
                    )
                },
                "valid_rows": row_count,
                "excluded_rows": 0,
                "mean_selected_group_composite_score": 1.0,
                "row_assignments": [
                    {
                        "BLKpoint_id": row_ids[index],
                        "status": "valid",
                        "selected_group_id": "unary_identity",
                        "selected_group_composite_score": 1.0,
                        "validated_by_group_ids": [],
                        "maximum_mole_fraction_disagreement": 0.0,
                    }
                    for index in range(row_count)
                ],
                "translation_rows": [
                    {
                        "BLKpoint_id": row_ids[index],
                        "mole_fraction": _row_values(mole, index, order),
                        "mass_fraction": _row_values(mass, index, order),
                        "volume_fraction": _row_values(
                            volume, index, order
                        ),
                    }
                    for index in range(row_count)
                ],
            },
        )
    if not fields:
        return CompositionAlignmentResult(
            coordinates=None,
            coordinate_comp_num_ids=(),
            coordinate_bases=(),
            plan={},
            error_code="COMPOSITION_IDENTITY_UNRESOLVED",
            error_message=(
                "No component-linked composition declaration can be "
                "resolved."
            ),
        )
    if any(len(field.values) != row_count for field in fields):
        raise ValueError("composition field lengths do not match row_ids")
    solvent_index = (
        order.index(solvent_comp_num_id)
        if solvent_comp_num_id in order
        else None
    )
    minimal_groups, validation_groups = _build_minimal_groups(
        fields,
        order,
        masses,
        pure_volumes,
        solvent_index,
        bridge_values,
        bridge_source_ids,
        closure_atol,
        consistency_atol,
    )
    if not minimal_groups:
        return CompositionAlignmentResult(
            coordinates=None,
            coordinate_comp_num_ids=(),
            coordinate_bases=(),
            plan={
                "kind": "tri_basis_composition_translation",
                "irreducible_representations": list(
                    FUNDAMENTAL_REPRESENTATIONS
                ),
                "component_order": list(order),
                "available_bases": sorted(
                    {field.basis for field in fields}
                ),
            },
            error_code="COMPOSITION_TRANSLATION_DEPENDENCIES_MISSING",
            error_message=(
                "No chemically permitted field group identifies a complete "
                "mole-, mass-, or volume-fraction representation."
            ),
            error_details={
                "available_fields": [field.local_id for field in fields]
            },
        )

    group_scores = {
        group.group_id: group.score_breakdown(
            row_relevance_scores=relevance,
            total_relevance=total_relevance,
            component_count=component_count,
        )
        for group in validation_groups
    }

    mole = np.full((row_count, component_count), np.nan, dtype=float)
    assignments: list[dict[str, Any]] = []
    selected_counts: dict[str, int] = {}
    conflict_count = 0
    uncovered_count = 0
    for row_index, row_id in enumerate(row_ids):
        selectable = [
            group for group in minimal_groups if group.valid[row_index]
        ]
        validators = [
            group for group in validation_groups if group.valid[row_index]
        ]
        if not selectable:
            uncovered_count += 1
            assignments.append(
                {"BLKpoint_id": row_id, "status": "uncovered"}
            )
            continue
        maximum_disagreement = 0.0
        for left_index, left in enumerate(validators):
            for right in validators[left_index + 1 :]:
                maximum_disagreement = max(
                    maximum_disagreement,
                    float(
                        np.max(
                            np.abs(
                                left.mole_fractions[row_index]
                                - right.mole_fractions[row_index]
                            )
                        )
                    ),
                )
        if maximum_disagreement > consistency_atol:
            conflict_count += 1
            assignments.append(
                {
                    "BLKpoint_id": row_id,
                    "status": "conflicting_representations",
                    "maximum_mole_fraction_disagreement": (
                        maximum_disagreement
                    ),
                    "candidate_group_ids": sorted(
                        group.group_id for group in validators
                    ),
                }
            )
            continue
        selected = min(
            selectable,
            key=lambda group: (
                -round(
                    group_scores[group.group_id]["composite_score"], 15
                ),
                group.group_id,
            ),
        )
        mole[row_index] = selected.mole_fractions[row_index]
        selected_counts[selected.group_id] = (
            selected_counts.get(selected.group_id, 0) + 1
        )
        assignments.append(
            {
                "BLKpoint_id": row_id,
                "status": "valid",
                "selected_group_id": selected.group_id,
                "selected_group_composite_score": group_scores[
                    selected.group_id
                ]["composite_score"],
                "validated_by_group_ids": sorted(
                    group.group_id
                    for group in validators
                    if group.group_id != selected.group_id
                ),
                "maximum_mole_fraction_disagreement": (
                    maximum_disagreement
                ),
            }
        )
    valid = np.all(np.isfinite(mole), axis=1)
    if not np.any(valid):
        return CompositionAlignmentResult(
            coordinates=None,
            coordinate_comp_num_ids=(),
            coordinate_bases=(),
            plan={
                "kind": "tri_basis_composition_translation",
                "irreducible_representations": list(
                    FUNDAMENTAL_REPRESENTATIONS
                ),
                "component_order": list(order),
                "row_assignments": assignments,
                "conflicting_rows": conflict_count,
                "uncovered_rows": uncovered_count,
            },
            error_code=(
                "COMPOSITION_DEFINITIONS_INCONSISTENT"
                if conflict_count
                else "INVALID_COMPOSITION_ROWS"
            ),
            error_message=(
                "No row has a self-consistent complete composition "
                "representation."
            ),
        )

    mass, volume = _tri_basis_state(mole, masses, pure_volumes)
    volumetric_rows, volumetric_conflicts = _volumetric_state_rows(
        mole,
        valid,
        masses,
        row_ids,
        bridge_values,
        volumetric_consistency_rtol,
    )
    volumetric_by_point = {
        row["BLKpoint_id"]: row for row in volumetric_rows
    }
    group_records = []
    minimal_ids = {group.group_id for group in minimal_groups}
    for group in sorted(
        validation_groups, key=lambda item: item.group_id
    ):
        group_records.append(
            {
                "group_id": group.group_id,
                "source_basis": group.source_basis_label,
                "measured_fields": [
                    {
                        "role": field.role,
                        "basis": field.basis,
                        "local_id": field.local_id,
                        "global_id": field.global_id,
                        "component_num_id": field.component_num_id,
                        "scope_component_num_ids": list(
                            field.scope_component_num_ids
                        ),
                    }
                    for field in group.fields
                ],
                "bridge": group.bridge,
                "bridge_source_ids": list(group.bridge_source_ids),
                "conversion_paths": list(group.conversion_paths),
                "relation": group.relation,
                "information_count": group.information_count,
                "minimal_identifying_group": group.group_id in minimal_ids,
                "composition_rank": component_count - 1,
                "valid_rows": group.valid_rows,
                "coverage_fraction": (
                    group.valid_rows / row_count if row_count else 0.0
                ),
                "exact_without_empirical_bridge": (
                    group.exact_without_empirical_bridge
                ),
                **group_scores[group.group_id],
            }
        )
    selected_groups = [
        group
        for group in minimal_groups
        if group.group_id in selected_counts
    ]
    translation_rows = [
        {
            "BLKpoint_id": row_ids[row_index],
            "selected_group_id": assignments[row_index][
                "selected_group_id"
            ],
            "mole_fraction": _row_values(mole, row_index, order),
            "mass_fraction": _row_values(mass, row_index, order),
            "volume_fraction": _row_values(volume, row_index, order),
            "volumetric_state": volumetric_by_point[row_ids[row_index]],
        }
        for row_index in np.where(valid)[0]
    ]
    plan = {
        "kind": "tri_basis_composition_translation",
        "irreducible_representations": list(
            FUNDAMENTAL_REPRESENTATIONS
        ),
        "conversion_graph": {
            "mole_fraction<->mass_fraction": (
                "exact when all formula molar masses are available"
            ),
            "mole_fraction<->volume_fraction": (
                "conditional on definition- and phase-compatible component "
                "molar volumes"
            ),
            "mass_fraction<->volume_fraction": (
                "through mole fraction and both bridge sets"
            ),
        },
        "volume_fraction_definition": (
            "pre-mixing/additive component-volume convention based on "
            "phase-compatible pure-component molar volumes; not an actual "
            "partial-volume partition of the mixed phase"
        ),
        "volumetric_state_layer": {
            "role": (
                "state-dependent total-volume bridge; it supplies bulk "
                "scale but does not by itself partition volume among components"
            ),
            "self_consistency_rtol": volumetric_consistency_rtol,
            "conflicting_rows": volumetric_conflicts,
            "rows": volumetric_rows,
        },
        "degrees_of_freedom": component_count - 1,
        "selection_policy": (
            "chemically permitted identifiability -> remove sufficient "
            "supersets -> maximize the recorded composite of relevance-"
            "weighted coverage, support, exactness, bridge independence, "
            "basis directness, and parsimony; every independent sufficient "
            "group must agree"
        ),
        "composition_group_score_weights": dict(
            COMPOSITION_GROUP_SCORE_WEIGHTS
        ),
        "composition_support_reference_points": (
            COMPOSITION_SUPPORT_REFERENCE_POINTS
        ),
        "self_consistency_atol_mole_fraction": consistency_atol,
        "component_order": list(order),
        "reference_component": order[-1],
        "field_catalog": [
            {
                "role": field.role,
                "basis": field.basis,
                "component_num_id": field.component_num_id,
                "local_id": field.local_id,
                "global_id": field.global_id,
                "scope_component_num_ids": list(
                    field.scope_component_num_ids
                ),
                "finite_rows": int(
                    np.count_nonzero(np.isfinite(field.values))
                ),
            }
            for field in sorted(fields, key=lambda item: item.local_id)
        ],
        "bridge_catalog": [
            {
                "bridge_id": bridge_id,
                "family": bridge_id.split("::", 1)[0],
                "source_local_ids": list(
                    bridge_source_ids.get(bridge_id, ())
                ),
                "finite_rows": int(
                    np.count_nonzero(np.isfinite(values))
                ),
            }
            for bridge_id, values in sorted(bridge_values.items())
        ],
        "candidate_groups": group_records,
        "selected_group_counts": dict(sorted(selected_counts.items())),
        "mean_selected_group_composite_score": float(
            np.mean(
                [
                    assignment["selected_group_composite_score"]
                    for assignment in assignments
                    if assignment.get("status") == "valid"
                ]
            )
        ),
        "selected_bases": sorted(
            {group.source_basis_label for group in selected_groups}
        ),
        "all_selected_groups_exact_stoichiometric": all(
            group.exact_without_empirical_bridge
            for group in selected_groups
        ),
        "representation_availability": {
            "mole_fraction": True,
            "mass_fraction": mass is not None,
            "volume_fraction": volume is not None,
        },
        "pure_molar_volume_ensembles": list(pure_volume_evidence),
        "row_assignments": assignments,
        "translation_rows": translation_rows,
        "valid_rows": int(np.count_nonzero(valid)),
        "excluded_rows": int(row_count - np.count_nonzero(valid)),
        "conflicting_rows": conflict_count,
        "uncovered_rows": uncovered_count,
        "molar_masses_g_mol": {
            component: (
                float(masses[index])
                if np.isfinite(masses[index])
                else None
            )
            for index, component in enumerate(order)
        },
    }
    return CompositionAlignmentResult(
        coordinates=mole[:, :-1],
        coordinate_comp_num_ids=order[:-1],
        coordinate_bases=tuple(
            "canonical_mole_fraction"
            for _ in range(component_count - 1)
        ),
        plan=plan,
    )
