"""Shared fixtures for the real-corpus ``block_search_adv`` regression suite.

Set ``THERMOML_QUERY_ROOT`` to exercise a checkout other than the enclosing
ThermoML query repository.
"""

from __future__ import annotations

import copy
import importlib.util
import json
import os
import sys
from pathlib import Path
from typing import Any, Callable

import pytest


TEST_DIR = Path(__file__).resolve().parent
STAGING_ROOT = TEST_DIR.parent



def _looks_like_query_root(candidate: Path) -> bool:
    return (
        (
            candidate
            / "card_db_search_tools"
            / "basic_search_tools"
        ).is_dir()
        and (candidate / "card_databases_storage").is_dir()
    )


def _query_root() -> Path:
    configured = os.environ.get("THERMOML_QUERY_ROOT")
    enclosing_checkouts = tuple(
        candidate
        for candidate in (TEST_DIR, *TEST_DIR.parents)
        if _looks_like_query_root(candidate)
    )
    candidates = (
        *((Path(configured),) if configured else ()),
        *enclosing_checkouts,
    )
    seen: set[str] = set()
    for candidate in candidates:
        normalized = os.path.normcase(os.fspath(candidate.resolve()))
        if normalized in seen:
            continue
        seen.add(normalized)
        if _looks_like_query_root(candidate):
            return candidate
    pytest.fail(
        "ThermoML query repository is unavailable; install this suite under "
        "its card_db_search_tools/tests tree or set THERMOML_QUERY_ROOT.",
        pytrace=False,
    )


QUERY_ROOT = _query_root()
BASIC_TOOLS = QUERY_ROOT / "card_db_search_tools" / "basic_search_tools"
PUBLIC_MODULE_CANDIDATES = (
    STAGING_ROOT / "12_block_search_adv.py",
    STAGING_ROOT / "basic_search_tools" / "12_block_search_adv.py",
    BASIC_TOOLS / "12_block_search_adv.py",
)

for import_root in (QUERY_ROOT, BASIC_TOOLS, STAGING_ROOT):
    text = os.fspath(import_root)
    if text not in sys.path:
        sys.path.insert(0, text)


def _load_file_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        pytest.fail(f"Could not create an import spec for {path}.", pytrace=False)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _is_staged(path: Path) -> bool:
    try:
        path.resolve().relative_to(STAGING_ROOT.resolve())
    except ValueError:
        return False
    return True


def _configure_staged_database_paths(module) -> None:
    """Point a locally staged package at the selected live data checkout.

    The production package naturally derives these paths from its installed
    location.  A temporary staging directory cannot do that, so the test
    harness supplies the exact same checkout explicitly without modifying the
    staged implementation.
    """

    catalogs = sys.modules.get("advanced_block_search.catalogs")
    engine = sys.modules.get("advanced_block_search.engine")
    if catalogs is None or engine is None:
        pytest.fail(
            "The staged advanced_block_search package was not imported.",
            pytrace=False,
        )

    card_storage = QUERY_ROOT / "card_databases_storage"
    paths = {
        "_WORKSPACE": QUERY_ROOT,
        "_CSV_DIR": (
            card_storage / "Canonicalized_ID_name_lists_csvs"
        ),
        "PCS_DB": (
            card_storage / "Individual_cards_dbs" / "PCS_INDIV.db"
        ),
        "RAW_DB": (
            QUERY_ROOT
            / "ThermoML.v2020-09-30.db"
            / "thermoml_raw.db"
        ),
        "PM_REGISTRY_DB": (
            card_storage / "PureOrMixtureData_registry.db"
        ),
        "RXN_REGISTRY_DB": (
            card_storage / "ReactionData_registry.db"
        ),
    }
    missing = [
        os.fspath(path)
        for name, path in paths.items()
        if not name.startswith("_") and not path.is_file()
    ]
    if missing:
        pytest.fail(
            "Required ThermoML test databases are unavailable: "
            + ", ".join(missing),
            pytrace=False,
        )

    for name, path in paths.items():
        setattr(catalogs, name, path)
        if hasattr(engine, name):
            setattr(engine, name, path)

    loader = getattr(catalogs, "_load_runtime_catalogs_cached", None)
    if loader is not None and hasattr(loader, "cache_clear"):
        loader.cache_clear()


@pytest.fixture(scope="session")
def adv_module():
    for candidate in PUBLIC_MODULE_CANDIDATES:
        if candidate.is_file():
            candidate_parent = os.fspath(candidate.parent)
            if candidate_parent in sys.path:
                sys.path.remove(candidate_parent)
            sys.path.insert(0, candidate_parent)
            if _is_staged(candidate):
                os.environ["THERMOML_QUERY_AGENT_ROOT"] = os.fspath(
                    QUERY_ROOT
                )
            module = _load_file_module("_block_search_adv_under_test", candidate)
            function = getattr(module, "block_search_adv", None)
            if not callable(function):
                pytest.fail(
                    f"{candidate} does not export block_search_adv(**request).",
                    pytrace=False,
                )
            if _is_staged(candidate):
                _configure_staged_database_paths(module)
            return module
    pytest.fail(
        "12_block_search_adv.py has not been staged or installed.",
        pytrace=False,
    )


@pytest.fixture(scope="session")
def run_adv(
    adv_module,
) -> Callable[[dict[str, Any]], dict[str, Any]]:
    """Execute and cache deterministic requests for this test session."""

    cache: dict[str, dict[str, Any]] = {}

    def run(request: dict[str, Any]) -> dict[str, Any]:
        cache_key = json.dumps(
            request,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
        if cache_key not in cache:
            function = adv_module.block_search_adv
            result = function(**copy.deepcopy(request))
            assert isinstance(result, dict)
            assert result.get("schema") == "block_search_adv/result-v1", result
            review = result.get("preexecution_review", {})
            assert review.get("raw_execution_authorized") is True
            assert review.get("automatic_confirmation") is True
            assert review.get("confirmed_stages") == [
                "composite_id_enrichment",
                "database_id_intent",
                "final_intent_and_syntax",
            ]
            normalized = result.get("normalized_query")
            assert isinstance(normalized, dict)
            assert normalized.get("input_contract") == (
                "block_search_adv/flat-v2"
            )
            assert not {
                "compound_list",
                "para_identity",
                "target_identity",
                "constraint_filter",
                "inline_state_filter",
                "filtering_identity",
                "compute",
            }.intersection(normalized)
            for value in normalized.values():
                assert not isinstance(value, dict)
                if isinstance(value, list):
                    assert all(isinstance(item, str) for item in value)
            assert isinstance(result.get("results"), list)
            assert result.get("n_results") == len(result["results"])
            n_binding_matches = 0
            for block_result in result["results"]:
                assert isinstance(block_result, dict)
                assert isinstance(block_result.get("block"), dict)
                assert isinstance(block_result["block"].get("doi"), str)
                assert isinstance(block_result["block"].get("lit_num_id"), str)
                assert block_result["block"]["lit_num_id"].startswith("GLOBlit_")
                assert isinstance(block_result.get("binding_matches"), list)
                assert block_result["binding_matches"]
                n_binding_matches += len(block_result["binding_matches"])
            assert result.get("n_binding_matches") == n_binding_matches
            assert isinstance(result.get("diagnostics"), dict)
            assert isinstance(result.get("truncated"), bool)
            cache[cache_key] = result
        return copy.deepcopy(cache[cache_key])

    return run


def compound_entry(
    alias: str,
    comp_num_id: str,
    *,
    scope: str = "system",
) -> str:
    declaration = f"{comp_num_id} AS {alias}"
    return declaration if scope == "system" else f"{declaration} IN {scope}"


def selector(
    alias: str,
    global_id: str,
    *,
    component_ref: str | None = None,
    phase_num_id: str | None = None,
    min_values: int = 1,
    min_distinct: int | None = None,
    cardinality: str = "exactly_one",
) -> str:
    parts = [global_id, "AS", alias]
    if component_ref is not None:
        parts.extend(("COMPONENT", component_ref))
    if phase_num_id is not None:
        parts.extend(("PHASE", phase_num_id))
    parts.extend(("MIN_FINITE", str(min_values)))
    if min_distinct is not None:
        parts.extend(("MIN_DISTINCT", str(min_distinct)))
    if cardinality != "exactly_one":
        parts.extend(
            (
                "CARDINALITY",
                "EACH" if cardinality == "all" else cardinality.upper(),
            )
        )
    return " ".join(parts)


def fixed_filter(
    alias: str,
    global_id: str,
    lower: int | float,
    upper: int | float,
    unit: str,
    semantic_type: str,
    *,
    component_ref: str | None = None,
    phase_num_id: str | None = None,
) -> str:
    del semantic_type
    declaration = selector(
        alias,
        global_id,
        component_ref=component_ref,
        phase_num_id=phase_num_id,
    )
    return (
        f"{declaration} WHERE VALUE BETWEEN "
        f"{lower}[{unit}] AND {upper}[{unit}]"
    )


def base_request(
    doi: str,
    *,
    compounds: list[str],
    exact_system: bool,
    system_min: int,
    system_max: int,
    system_types: list[str],
    para: list[str],
    targets: list[str],
    constraints: list[str] | None = None,
    inline_states: list[str] | None = None,
    block_phases: list[str] | None = None,
    filtering: list[dict[str, str]] | None = None,
    where: str | None = None,
    minimum_count: int = 1,
    minimum_of: list[str] | None = None,
    compute: list[str] | None = None,
    select: list[str] | None = None,
    order_by: list[str] | None = None,
    limit: int = 50,
    explanation: str,
) -> dict[str, Any]:
    del filtering, minimum_of
    return {
        "compounds": compounds,
        "compound_match": "exact" if exact_system else "all",
        "system_scope": "declared",
        "system_type": system_types[0] if system_types else None,
        "system_size_min": system_min,
        "system_size_max": system_max,
        "parameters": para,
        "targets": targets,
        "fixed_constraints": constraints or [],
        "inline_state": inline_states or [],
        "literature": [
            f"DOI={doi}",
            "YEAR BETWEEN 1900 AND 2026",
        ],
        "phases": list(block_phases or []),
        "phase_match": "any",
        "where": where,
        "minimum_common_points": minimum_count,
        "calculate": compute or [],
        "select": select
        or ["COUNT(*) AS rows_after_where"],
        "having": None,
        "order_by": order_by or [],
        "limit": limit,
        "explanation": explanation,
    }


def unary_request(*, minimum_count: int = 4) -> dict[str, Any]:
    temperature = selector(
        "temperature",
        "GLOBconstr_2",
        phase_num_id="GLOBphase_3",
        min_values=4,
        min_distinct=2,
    )
    pressure = selector(
        "pressure",
        "GLOBconstr_1",
        phase_num_id="GLOBphase_3",
        min_values=4,
        min_distinct=2,
    )
    target = selector(
        "conductivity",
        "GLOBprop_34",
        phase_num_id="GLOBphase_3",
        min_values=4,
    )
    return base_request(
        "10.1007/s10765-005-5566-6",
        compounds=[compound_entry("carbon_dioxide", "GLOBcomp_3")],
        exact_system=True,
        system_min=1,
        system_max=1,
        system_types=["unary"],
        para=[temperature, pressure],
        targets=[target],
        block_phases=["GLOBphase_3"],
        filtering=[
            {"ref": "temperature", "from": "para_identity"},
            {"ref": "pressure", "from": "para_identity"},
        ],
        where=(
            "temperature BETWEEN 425[K] AND 429[K] "
            "AND pressure BETWEEN 1000[kPa] AND 5000[kPa]"
        ),
        minimum_count=minimum_count,
        minimum_of=["temperature", "pressure", "conductivity"],
        select=["MEAN(conductivity) AS mean_conductivity"],
        explanation=(
            "Find unary carbon dioxide conductivity rows at high "
            "temperature and moderate pressure."
        ),
    )


def binary_ranking_request(
    *,
    mole_fraction_id: str = "GLOBconstr_3",
    minimum_count: int = 3,
    limit: int = 50,
) -> dict[str, Any]:
    composition = selector(
        "x_ionic_liquid",
        mole_fraction_id,
        component_ref="ionic_liquid",
        phase_num_id="GLOBphase_1",
        min_values=3,
        min_distinct=2,
    )
    target = selector(
        "h_excess",
        "GLOBprop_17",
        phase_num_id="GLOBphase_1",
        min_values=3,
    )
    return base_request(
        "10.1016/j.jct.2010.11.014",
        compounds=[
            compound_entry("ionic_liquid", "GLOBcomp_681"),
        ],
        exact_system=False,
        system_min=2,
        system_max=2,
        system_types=["binary"],
        para=[composition],
        targets=[target],
        constraints=[
            fixed_filter(
                "pressure_constraint",
                "GLOBvar_3",
                101,
                102,
                "kPa",
                "pressure",
                phase_num_id="GLOBphase_1",
            ),
            fixed_filter(
                "temperature_constraint",
                "GLOBvar_1",
                298,
                299,
                "K",
                "thermodynamic_temperature",
                phase_num_id="GLOBphase_1",
            ),
        ],
        block_phases=["GLOBphase_1"],
        filtering=[
            {"ref": "x_ionic_liquid", "from": "para_identity"},
        ],
        where="x_ionic_liquid BETWEEN 0.2[1] AND 0.8[1]",
        minimum_count=minimum_count,
        minimum_of=["x_ionic_liquid", "h_excess"],
        compute=[
            "EXP(LN(x_ionic_liquid)) AS x_roundtrip",
            (
                "ABS(h_excess) / "
                "(x_roundtrip * (1[1] - x_roundtrip)) AS scaled_h"
            ),
        ],
        select=["MEAN(scaled_h) AS mean_scaled_h"],
        order_by=["mean_scaled_h DESC NULLS LAST"],
        limit=limit,
        explanation=(
            "Rank binary ionic liquid excess enthalpy blocks by a "
            "composition-scaled mean."
        ),
    )


def target_translation_request(
    *,
    target_id: str = "GLOBconstr_3",
    minimum_count: int = 2,
) -> dict[str, Any]:
    temperature = selector(
        "temperature",
        "GLOBconstr_2",
        phase_num_id="GLOBphase_4",
        min_values=2,
        min_distinct=2,
    )
    target = selector(
        "liquid_x",
        target_id,
        component_ref="pentafluoroethane",
        phase_num_id="GLOBphase_4",
        min_values=2,
        min_distinct=2,
    )
    return base_request(
        "10.1021/je700588d",
        compounds=[
            compound_entry("pentafluoroethane", "GLOBcomp_147"),
            compound_entry("ionic_liquid", "GLOBcomp_64"),
        ],
        exact_system=True,
        system_min=2,
        system_max=2,
        system_types=["binary"],
        para=[temperature],
        targets=[target],
        block_phases=["GLOBphase_4"],
        filtering=[
            {"ref": "temperature", "from": "para_identity"},
            {"ref": "liquid_x", "from": "target_identity"},
        ],
        where=(
            "temperature BETWEEN 290[K] AND 310[K] "
            "AND liquid_x BETWEEN 0.7[1] AND 0.8[1]"
        ),
        minimum_count=minimum_count,
        minimum_of=["temperature", "liquid_x"],
        compute=["EXP(LN(liquid_x)) AS x_roundtrip"],
        select=["MEAN(x_roundtrip) AS mean_x_roundtrip"],
        explanation=(
            "Find liquid pentafluoroethane mole fractions at intermediate "
            "temperatures."
        ),
    )


def reaction_request() -> dict[str, Any]:
    target = selector(
        "reaction_enthalpy",
        "GLOBprop_36",
        min_values=1,
    )
    inline_states = [
        (
            "GLOBvar_1 AS reaction_temperature "
            "ON TARGET reaction_enthalpy "
            "WHERE VALUE BETWEEN 298[K] AND 299[K]"
        ),
        (
            "GLOBconstr_1 AS reaction_pressure "
            "ON TARGET reaction_enthalpy "
            "WHERE VALUE BETWEEN 199[kPa] AND 201[kPa]"
        ),
    ]
    return base_request(
        "10.1007/s10765-009-0568-4",
        compounds=[
            compound_entry(
                "potassium_benzoate",
                "GLOBcomp_7883",
                scope="any",
            )
        ],
        exact_system=False,
        system_min=1,
        system_max=10,
        system_types=[],
        para=[],
        targets=[target],
        inline_states=inline_states,
        filtering=[
            {"ref": "reaction_enthalpy", "from": "target_identity"},
        ],
        where="reaction_enthalpy <= -600[kJ/mol]",
        minimum_count=1,
        minimum_of=["reaction_enthalpy"],
        select=[
            "MEAN(reaction_enthalpy) AS mean_reaction_enthalpy"
        ],
        explanation=(
            "Find the potassium benzoate formation enthalpy at its reported "
            "inline temperature and pressure."
        ),
    )


def missing_value_request(
    *,
    minimum_count: int = 8,
    ambiguous_target: bool = False,
    target_cardinality: str = "exactly_one",
) -> dict[str, Any]:
    feed = selector(
        "feed_methanol_x",
        "GLOBconstr_3",
        component_ref="methanol",
        phase_num_id="GLOBphase_4",
        min_values=1,
    )
    ether_target = selector(
        "ether_x",
        "GLOBvar_2",
        component_ref="ether",
        phase_num_id=None if ambiguous_target else "GLOBphase_5",
        min_values=1,
        cardinality=target_cardinality,
    )
    targets = [ether_target]
    minimum_of = ["feed_methanol_x", "ether_x"]
    if not ambiguous_target:
        targets.append(
            selector(
                "methanol_x",
                "GLOBconstr_3",
                component_ref="methanol",
                phase_num_id="GLOBphase_5",
                min_values=1,
            )
        )
        minimum_of.append("methanol_x")
    return base_request(
        "10.1016/j.fluid.2007.04.018",
        compounds=[
            compound_entry("methanol", "GLOBcomp_4"),
            compound_entry("ether", "GLOBcomp_4625"),
            compound_entry("water", "GLOBcomp_1"),
        ],
        exact_system=True,
        system_min=3,
        system_max=3,
        system_types=["ternary"],
        para=[feed],
        targets=targets,
        constraints=[
            fixed_filter(
                "temperature_constraint",
                "GLOBvar_1",
                298,
                299,
                "K",
                "thermodynamic_temperature",
                phase_num_id="GLOBphase_4",
            ),
            fixed_filter(
                "pressure_constraint",
                "GLOBvar_3",
                100,
                102,
                "kPa",
                "pressure",
                phase_num_id="GLOBphase_4",
            ),
        ],
        filtering=[
            {"ref": "feed_methanol_x", "from": "para_identity"},
        ],
        where="feed_methanol_x >= 0[1]",
        minimum_count=minimum_count,
        minimum_of=minimum_of,
        select=["COUNT(*) AS rows_after_where"],
        explanation=(
            "Count complete ternary liquid equilibrium rows with explicitly "
            "qualified component and phase bindings."
        ),
    )


@pytest.fixture(scope="session")
def unary_result(run_adv):
    return run_adv(unary_request())


@pytest.fixture(scope="session")
def binary_result(run_adv):
    return run_adv(binary_ranking_request())


@pytest.fixture(scope="session")
def reaction_result(run_adv):
    return run_adv(reaction_request())
