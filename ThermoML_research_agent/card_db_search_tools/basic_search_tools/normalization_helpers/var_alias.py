"""
Variable aliases.

Maps common shorthand symbols and alternate phrasings to the canonical
``var_id`` stored in variable_ids.csv.  All keys are lowercase.
"""

# alias (lowercase) → canonical var_id
VAR_ALIASES: dict[str, str] = {
    # ── Temperature / pressure ───────────────────────────────────
    "temperature":              "temperature_k",
    "t":                        "temperature_k",
    "temp":                     "temperature_k",
    "pressure":                 "pressure_kpa",
    "p":                        "pressure_kpa",
    # ── Composition ──────────────────────────────────────────────
    "mole fraction":            "mole_fraction_{DOIcomp_id}",
    "x":                        "mole_fraction_{DOIcomp_id}",
    "mass fraction":            "mass_fraction_{DOIcomp_id}",
    "w":                        "mass_fraction_{DOIcomp_id}",
    "molality":                 "molality_mol_kg_{DOIcomp_id}",
    "m":                        "molality_mol_kg_{DOIcomp_id}",
    "molarity":                 "amount_concentration_molarity_mol_dm3_{DOIcomp_id}",
    "c":                        "amount_concentration_molarity_mol_dm3_{DOIcomp_id}",
    "concentration":            "amount_concentration_molarity_mol_dm3_{DOIcomp_id}",
    "volume fraction":          "volume_fraction_{DOIcomp_id}",
    "phi_v":                    "volume_fraction_{DOIcomp_id}",
    # ── Solvent composition ──────────────────────────────────────
    "solvent molality":         "solvent_molality_mol_kg_{DOIcomp_id}",
    "solvent mass fraction":    "solvent_mass_fraction_{DOIcomp_id}",
    "solvent mole fraction":    "solvent_mole_fraction_{DOIcomp_id}",
    "solvent molarity":         "solvent_amount_concentration_molarity_mol_dm3_{DOIcomp_id}",
    "solvent volume fraction":  "solvent_volume_fraction_{DOIcomp_id}",
    # ── Ratios ───────────────────────────────────────────────────
    "mass ratio":               "mass_ratio_of_solute_to_solvent_{DOIcomp_id}",
    "amount ratio":             "amount_ratio_of_solute_to_solvent_{DOIcomp_id}",
    "mole ratio":               "amount_ratio_of_solute_to_solvent_{DOIcomp_id}",
    # ── Solution ─────────────────────────────────────────────────
    "initial molality":         "initial_molality_of_solute_mol_kg",
    "final molality":           "final_molality_of_solute_mol_kg",
    # ── Miscellaneous ────────────────────────────────────────────
    "frequency":                "frequency_mhz",
    "f":                        "frequency_mhz",
    "freq":                     "frequency_mhz",
}

_LOOKUP: dict[str, str] = {k.lower(): v for k, v in VAR_ALIASES.items()}


def expand_var_alias(query: str) -> str:
    """Return canonical var_id if *query* matches a known alias,
    otherwise return the original *query* unchanged."""
    return _LOOKUP.get(query.strip().lower(), query)
