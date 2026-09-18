"""health_check_helper — pre-flight validation for tool + compactor catalogs."""

from NIST_ThermoML_agents import _windows_package_paths

__path__ = _windows_package_paths(__path__)

from .heath_check_tools_compactors_catalogs import (
    run_health_check,
    CatalogHealthCheckError,
)

__all__ = ["run_health_check", "CatalogHealthCheckError"]
