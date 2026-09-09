"""
Compound name aliases.

Maps common alternative names, abbreviations, IUPAC synonyms, and trivial
names to the canonical ``common_name`` stored in compound_ids.csv.
All keys are lowercase.
"""

# alias (lowercase) → canonical common_name (as stored in compound_ids.csv)
COMP_ALIASES: dict[str, str] = {
    # ── Water ────────────────────────────────────────────────────
    "h2o":                      "water",
    "dihydrogen monoxide":      "water",
    "dihydrogen oxide":         "water",
    # ── Simple alcohols ──────────────────────────────────────────
    "etoh":                     "ethanol",
    "ethyl alcohol":            "ethanol",
    "grain alcohol":            "ethanol",
    "meoh":                     "methanol",
    "methyl alcohol":           "methanol",
    "wood alcohol":             "methanol",
    "1-propanol":               "propan-1-ol",
    "n-propanol":               "propan-1-ol",
    "propanol":                 "propan-1-ol",
    "propyl alcohol":           "propan-1-ol",
    "n-propyl alcohol":         "propan-1-ol",
    "1-propyl alcohol":         "propan-1-ol",
    "2-propanol":               "propan-2-ol",
    "isopropanol":              "propan-2-ol",
    "isopropyl alcohol":        "propan-2-ol",
    "ipa":                      "propan-2-ol",
    "rubbing alcohol":          "propan-2-ol",
    "1-butanol":                "butan-1-ol",
    "n-butanol":                "butan-1-ol",
    "butyl alcohol":            "butan-1-ol",
    "n-butyl alcohol":          "butan-1-ol",
    "2-butanol":                "butan-2-ol",
    "sec-butanol":              "butan-2-ol",
    "sec-butyl alcohol":        "butan-2-ol",
    "isobutanol":               "2-methyl-1-propanol",
    "isobutyl alcohol":         "2-methyl-1-propanol",
    "2-methyl-1-propanol":      "2-methyl-1-propanol",
    "tert-butanol":             "2-methylpropan-2-ol",
    "tert-butyl alcohol":       "2-methylpropan-2-ol",
    "t-butanol":                "2-methylpropan-2-ol",
    "1-pentanol":               "pentan-1-ol",
    "n-pentanol":               "pentan-1-ol",
    "amyl alcohol":             "pentan-1-ol",
    "pentyl alcohol":           "pentan-1-ol",
    "1-hexanol":                "hexan-1-ol",
    "n-hexanol":                "hexan-1-ol",
    "hexyl alcohol":            "hexan-1-ol",
    "1-octanol":                "octan-1-ol",
    "n-octanol":                "octan-1-ol",
    "octyl alcohol":            "octan-1-ol",
    # ── Diols / polyols ──────────────────────────────────────────
    "ethylene glycol":          "1,2-ethanediol",
    "glycol":                   "1,2-ethanediol",
    "meg":                      "1,2-ethanediol",
    "monoethylene glycol":      "1,2-ethanediol",
    # ── Aromatics ────────────────────────────────────────────────
    "methylbenzene":            "toluene",
    "phh":                      "benzene",
    "p-xylene":                 "1,4-dimethylbenzene",
    "para-xylene":              "1,4-dimethylbenzene",
    "o-xylene":                 "1,2-dimethylbenzene",
    "ortho-xylene":             "1,2-dimethylbenzene",
    "m-xylene":                 "1,3-dimethylbenzene",
    "meta-xylene":              "1,3-dimethylbenzene",
    # ── Alkanes ──────────────────────────────────────────────────
    "n-pentane":                "pentane",
    "n-hexane":                 "hexane",
    "n-heptane":                "heptane",
    "n-octane":                 "octane",
    "n-nonane":                 "nonane",
    "n-decane":                 "decane",
    "n-dodecane":               "dodecane",
    "isooctane":                "2,2,4-trimethylpentane",
    # ── Gases ────────────────────────────────────────────────────
    "co2":                      "carbon dioxide",
    "o2":                       "oxygen",
    "n2":                       "nitrogen",
    # ── Ketones ──────────────────────────────────────────────────
    "dimethyl ketone":          "acetone",
    "propanone":                "acetone",
    "2-propanone":              "acetone",
    "methyl ethyl ketone":      "butanone",
    "mek":                      "butanone",
    "2-butanone":               "butanone",
    # ── Ethers ───────────────────────────────────────────────────
    "thf":                      "tetrahydrofuran",
    "oxolane":                  "tetrahydrofuran",
    "mtbe":                     "2-methoxy-2-methylpropane",
    "methyl tert-butyl ether":  "2-methoxy-2-methylpropane",
    # ── Esters ───────────────────────────────────────────────────
    "etoac":                    "ethyl acetate",
    "methyl acetate":           "methyl ethanoate",
    "meoac":                    "methyl ethanoate",
    # ── Nitriles / amides ────────────────────────────────────────
    "mecn":                     "acetonitrile",
    "methyl cyanide":           "acetonitrile",
    "dmf":                      "dimethylformamide",
    "n,n-dimethylformamide":    "dimethylformamide",
    "dmso":                     "dimethyl sulfoxide",
    "nmp":                      "N-methylpyrrolidone",
    "n-methyl-2-pyrrolidone":   "N-methylpyrrolidone",
    "1-methyl-2-pyrrolidone":   "N-methylpyrrolidone",
    # ── Halogenated ──────────────────────────────────────────────
    "chloroform":               "trichloromethane",
    "chcl3":                    "trichloromethane",
    # ── Carboxylic acids ─────────────────────────────────────────
    "glacial acetic acid":      "acetic acid",
    "ethanoic acid":            "acetic acid",
    # ── Inorganic salts ──────────────────────────────────────────
    "nacl":                     "sodium chloride",
    "table salt":               "sodium chloride",
    "kcl":                      "potassium chloride",
    # ── Cycloalkanes ─────────────────────────────────────────────
    "cyhex":                    "cyclohexane",
    "mch":                      "methylcyclohexane",
    # ── Alkenes ──────────────────────────────────────────────────
    "1-hexene":                 "hex-1-ene",
    "propylene":                "propene",
    "r1270":                    "propene",
    # ── Ionic liquids (most common) ──────────────────────────────
    "bmim bf4":                 "1-butyl-3-methylimidazolium tetrafluoroborate",
    "[bmim][bf4]":              "1-butyl-3-methylimidazolium tetrafluoroborate",
    "bmim ntf2":                "1-butyl-3-methylimidazolium bis(trifluoromethylsulfonyl)imide",
    "[bmim][ntf2]":             "1-butyl-3-methylimidazolium bis(trifluoromethylsulfonyl)imide",
    "[bmim][tf2n]":             "1-butyl-3-methylimidazolium bis(trifluoromethylsulfonyl)imide",
}

# Build lowercase lookup once
_LOOKUP: dict[str, str] = {k.lower(): v for k, v in COMP_ALIASES.items()}


def expand_comp_alias(query: str) -> str:
    """Return canonical compound name if *query* matches a known alias,
    otherwise return the original *query* unchanged."""
    return _LOOKUP.get(query.strip().lower(), query)
