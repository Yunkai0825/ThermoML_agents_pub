"""Read-only browser adapters for deterministic specialized tools.

The Flask browser depends only on the small normalized contract in this
package.  Specialized pipelines keep ownership of their cache layout and
translate it through a plugin instead of leaking pipeline-specific paths into
routes or templates.
"""

from .base import PluginManifest, SpecializedToolBrowserPlugin
from .registry import SpecializedToolPluginRegistry, build_default_registry

__all__ = [
    "PluginManifest",
    "SpecializedToolBrowserPlugin",
    "SpecializedToolPluginRegistry",
    "build_default_registry",
]
