"""Explicit, failure-isolated specialized-tool browser registry."""

from __future__ import annotations

import re
from typing import Iterable

from .base import SpecializedToolBrowserPlugin


_PLUGIN_ID_RE = re.compile(r"^[a-z][a-z0-9-]*$")


class SpecializedToolPluginRegistry:
    """Own the installed browser plugins.

    Registration is explicit rather than filesystem code discovery: cache
    folders are data, never executable plugins.  A future pipeline adds its
    adapter to :func:`build_default_registry` (or injects it in an application
    factory/test) and cannot disturb already registered plugins.
    """

    def __init__(
        self, plugins: Iterable[SpecializedToolBrowserPlugin] = ()
    ) -> None:
        self._plugins: dict[str, SpecializedToolBrowserPlugin] = {}
        for plugin in plugins:
            self.register(plugin)

    def register(self, plugin: SpecializedToolBrowserPlugin) -> None:
        plugin_id = plugin.manifest.plugin_id
        if not _PLUGIN_ID_RE.fullmatch(plugin_id):
            raise ValueError(
                f"Invalid specialized-tool plugin_id {plugin_id!r}; expected "
                "lowercase kebab-case"
            )
        if plugin_id in self._plugins:
            raise ValueError(f"Duplicate specialized-tool plugin_id {plugin_id!r}")
        self._plugins[plugin_id] = plugin

    def get(self, plugin_id: str) -> SpecializedToolBrowserPlugin:
        try:
            return self._plugins[plugin_id]
        except KeyError as exc:
            raise LookupError(
                f"Unknown specialized-tool browser plugin {plugin_id!r}"
            ) from exc

    def manifests(self) -> list[dict]:
        return [
            plugin.manifest.to_dict()
            for _, plugin in sorted(self._plugins.items())
        ]


def build_default_registry() -> SpecializedToolPluginRegistry:
    """Build the installed plugin set for the ThermoML browser."""

    from .property_screening import PropertyScreeningBrowserPlugin

    return SpecializedToolPluginRegistry([PropertyScreeningBrowserPlugin()])
