"""ThermoML agents and import support for deeply nested Windows checkouts."""

import os as _os


def _windows_package_paths(paths):
    """Extend only deep package search paths, leaving data/output roots intact."""
    if _os.name != "nt":
        return list(paths)
    result = []
    for path in paths:
        absolute = _os.path.abspath(path)
        if absolute.startswith("\\\\?\\"):
            result.append(absolute)
        elif absolute.startswith("\\\\"):
            result.append("\\\\?\\UNC\\" + absolute[2:])
        else:
            result.append("\\\\?\\" + absolute)
    return result
