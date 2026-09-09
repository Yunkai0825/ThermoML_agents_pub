"""Shared access to the production ThermoML query catalogs.

The suite intentionally exercises the installed checkout and real card
databases.  Set ``THERMOML_QUERY_ROOT`` to point at another checkout.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest


TEST_DIR = Path(__file__).resolve().parent


def _looks_like_query_root(candidate: Path) -> bool:
    return (
        (candidate / "card_db_search_tools" / "basic_search_tools").is_dir()
        and (candidate / "card_databases_storage").is_dir()
        and (candidate / "NIST_ThermoML_agents").is_dir()
    )


def _query_root() -> Path:
    configured = os.environ.get("THERMOML_QUERY_ROOT")
    candidates = (
        *((Path(configured),) if configured else ()),
        *TEST_DIR.parents,
    )
    for candidate in candidates:
        if _looks_like_query_root(candidate):
            return candidate
    pytest.fail(
        "ThermoML query checkout is unavailable; set THERMOML_QUERY_ROOT.",
        pytrace=False,
    )


QUERY_ROOT = _query_root()
for import_root in (
    QUERY_ROOT,
    QUERY_ROOT / "card_db_search_tools",
    QUERY_ROOT / "card_db_search_tools" / "basic_search_tools",
):
    text = os.fspath(import_root)
    if text not in sys.path:
        sys.path.insert(0, text)


@pytest.fixture(scope="session")
def query_root() -> Path:
    return QUERY_ROOT


@pytest.fixture(scope="session")
def l1_catalog():
    from NIST_ThermoML_agents.NIST_ThermoML_query_agent.query_agent_workflows.L1_workers.l1_query_dispatcher import (
        QueryL1Catalog,
    )

    return QueryL1Catalog()


@pytest.fixture(scope="session")
def l2_catalogs():
    from NIST_ThermoML_agents.NIST_ThermoML_query_agent.query_agent_workflows.L2_leaf_evaluators.l2_dispatchers import (
        L2CompCatalog,
        L2MeasCatalog,
        L2PropCatalog,
        L2RefCatalog,
    )

    return {
        "compound": L2CompCatalog(),
        "measurement": L2MeasCatalog(),
        "property": L2PropCatalog(),
        "reference": L2RefCatalog(),
    }
