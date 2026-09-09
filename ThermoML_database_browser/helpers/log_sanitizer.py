"""Keep HTTP dependency debug output out of the browser's agent terminal."""

import logging

_NOISY_LOGGERS = ("httpx", "httpcore", "urllib3", "requests", "openai")


def suppress_noisy_dependency_debug() -> dict[str, int]:
    """Temporarily suppress dependency DEBUG logs and retain explicit levels."""
    previous = {}
    names = set(_NOISY_LOGGERS)
    names.update(
        name for name in list(logging.root.manager.loggerDict)
        if any(name.startswith(prefix + ".") for prefix in _NOISY_LOGGERS)
    )
    for name in sorted(names, key=lambda value: (value.count("."), value), reverse=True):
        logger = logging.getLogger(name)
        previous[name] = logger.level
        if logger.getEffectiveLevel() < logging.WARNING:
            logger.setLevel(logging.WARNING)
    return previous


def restore_logger_levels(previous: dict[str, int]) -> None:
    """Restore logger configuration after a browser run finishes."""
    for name, level in previous.items():
        logging.getLogger(name).setLevel(level)
