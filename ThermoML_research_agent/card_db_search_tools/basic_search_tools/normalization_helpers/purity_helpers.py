"""Purity value extraction and normalization for ThermoML compound cards."""


def best_purity(samples: list[dict] | None) -> float | None:
    """Return the highest purity fraction (0-1) across all samples/steps.

    Reads the one current nested card schema:
    ``purity_steps[].purity.mol_fraction`` (or mass/vol). Source ThermoML
    contains both fractional and percentage magnitudes, which are converted
    deterministically to a 0-1 result.

    Returns None if no purity data is present.
    """
    if samples is None:
        return None
    if not isinstance(samples, list):
        raise TypeError("samples must be an array or null")
    best = None
    for sample_index, sample in enumerate(samples):
        if not isinstance(sample, dict) or "purity_steps" not in sample:
            raise ValueError(f"samples[{sample_index}] requires purity_steps")
        steps = sample["purity_steps"]
        if steps is None:
            continue
        if not isinstance(steps, list):
            raise TypeError(f"samples[{sample_index}].purity_steps must be an array or null")
        for step_index, step in enumerate(steps):
            if not isinstance(step, dict) or "purity" not in step:
                raise ValueError(
                    f"samples[{sample_index}].purity_steps[{step_index}] requires purity"
                )
            pur = step["purity"]
            if not isinstance(pur, dict):
                raise TypeError("purity must be an object")
            for frac_key in ("mol_fraction", "mass_fraction", "vol_fraction"):
                if frac_key not in pur:
                    raise ValueError(f"purity is missing {frac_key}")
                val = pur[frac_key]
                if val is not None:
                    if isinstance(val, bool) or not isinstance(val, (int, float)) or val < 0:
                        raise TypeError(f"purity.{frac_key} must be a non-negative number or null")
                    normalised = val / 100.0 if val > 1 else val
                    best = normalised if best is None else max(best, normalised)
    return best
