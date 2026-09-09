"""
Measurement method aliases.

Maps common abbreviations, instrument names, and technique shorthand to the
canonical ``meas_id`` stored in measurement_ids.csv.  All keys are lowercase.
"""

# alias (lowercase) → canonical meas_id
MEAS_ALIASES: dict[str, str] = {
    # ── Chromatography ───────────────────────────────────────────
    "gc":                       "chromatography",
    "hplc":                     "chromatography",
    "gas chromatography":       "chromatography",
    "liquid chromatography":    "chromatography",
    "correlation gc":           "correlation_gas_chromatography",
    # ── Density ──────────────────────────────────────────────────
    "vibrating tube":           "vibrating_tube_method",
    "vibrating u-tube":         "vibrating_tube_method",
    "densimeter":               "vibrating_tube_method",
    "dma":                      "vibrating_tube_method",
    "anton paar":               "vibrating_tube_method",
    "pycnometer":               "pycnometric_method",
    "pycnometry":               "pycnometric_method",
    "density calibration":      "density_calibration_data",
    # ── Refractometry ────────────────────────────────────────────
    "refractometer":            "standard_abbe_refractometry",
    "abbe refractometer":       "standard_abbe_refractometry",
    "refractometry":            "standard_abbe_refractometry",
    "refractive index calibration": "index_of_refraction_calibration_data",
    # ── Viscometry ───────────────────────────────────────────────
    "capillary viscometer":     "capillary_tube_ostwald_ubbelohde_method",
    "ostwald viscometer":       "capillary_tube_ostwald_ubbelohde_method",
    "ubbelohde viscometer":     "capillary_tube_ostwald_ubbelohde_method",
    "ubbelohde":                "capillary_tube_ostwald_ubbelohde_method",
    "falling ball":             "falling_or_rolling_sphere_viscometry",
    "falling sphere":           "falling_or_rolling_sphere_viscometry",
    "rolling ball":             "falling_or_rolling_sphere_viscometry",
    "concentric cylinder":      "concentric_cylinders_viscometry",
    "couette":                  "concentric_cylinders_viscometry",
    "rotational viscometer":    "concentric_cylinders_viscometry",
    # ── Calorimetry ──────────────────────────────────────────────
    "differential scanning calorimetry": "dsc",
    "flow calorimeter":         "flow_calorimetry",
    "flow calorimetry":         "flow_calorimetry",
    "calvet":                   "calvet_calorimetry",
    "calvet calorimeter":       "calvet_calorimetry",
    "titration calorimetry":    "titration_calorimetry",
    "itc":                      "titration_calorimetry",
    "adiabatic calorimetry":    "vacuum_adiabatic_calorimetry",
    "adiabatic calorimeter":    "vacuum_adiabatic_calorimetry",
    "small adiabatic calorimetry": "small_less_than_1g_adiabatic_calorimetry",
    "bomb calorimetry":         "static_bomb_calorimetry",
    "bomb calorimeter":         "static_bomb_calorimetry",
    "combustion calorimetry":   "static_bomb_calorimetry",
    "drop calorimetry":         "drop_calorimetry",
    "drop calorimeter":         "drop_calorimetry",
    # ── Ebulliometry ─────────────────────────────────────────────
    "ebulliometer":             "ebulliometric_method_recirculating_still",
    "ebulliometry":             "ebulliometric_method_recirculating_still",
    "recirculating still":      "ebulliometric_method_recirculating_still",
    # ── Acoustics / speed of sound ───────────────────────────────
    "sing-around":              "sing_around_technique_in_a_fixed_path_interferometer",
    "sing around":              "sing_around_technique_in_a_fixed_path_interferometer",
    "acoustic interferometer":  "linear_variable_path_acoustic_interferometer",
    "variable path interferometer": "linear_variable_path_acoustic_interferometer",
    "pulse echo":               "pulse_echo_method",
    "pulse-echo":               "pulse_echo_method",
    # ── Tensiometry ──────────────────────────────────────────────
    "ring tensiometer":         "ring_tensiometer",
    "du nouy ring":             "ring_tensiometer",
    "du noüy":                  "ring_tensiometer",
    "pendant drop":             "pendant_drop_shape",
    # ── Electrical ───────────────────────────────────────────────
    "ac cell":                  "alternating_current_cell_with_electrodes",
    "ac conductivity cell":     "alternating_current_cell_with_electrodes",
    "impedance cell":           "alternating_current_cell_with_electrodes",
    # ── Phase equilibrium ────────────────────────────────────────
    "phase equilibration":      "phase_equilibration",
    "static method":            "phase_equilibration",
    "transpiration":            "transpiration_method",
    "transpiration method":     "transpiration_method",
    # ── Spectroscopy ─────────────────────────────────────────────
    "single path length":       "single_path_length_method",
    "absorption spectroscopy":  "single_path_length_method",
}

_LOOKUP: dict[str, str] = {k.lower(): v for k, v in MEAS_ALIASES.items()}


def expand_meas_alias(query: str) -> str:
    """Return canonical meas_id if *query* matches a known alias,
    otherwise return the original *query* unchanged."""
    return _LOOKUP.get(query.strip().lower(), query)
