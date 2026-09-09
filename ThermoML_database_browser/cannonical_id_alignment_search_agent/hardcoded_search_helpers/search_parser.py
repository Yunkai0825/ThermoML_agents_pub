"""
Smart search parser — first pass (deterministic, no LLM).

Splits user input into structured tokens using these conventions:
  • ``+``  means AND  (all tokens must match the same block)
  • ``;``  separates independent search groups (OR blocks)
  • Bare words/phrases are classified by heuristic rules

Token classification priority:
  1. DOI pattern       → doi
  2. Year range        → year_min / year_max
  3. Molecular formula → formula
  4. Keyword matches   → property / measurement / variable / constraint / phase
  5. Everything else   → compound (default bucket)

Returns a list of ``SearchBlock`` dicts, each with optional keys:
  compounds, properties, measurements, variables, constraints,
  phases, formulas, dois, authors, title_words, year_min, year_max,
  journals, system_type, block_type, min_datapoints, raw_tokens,
  unresolved (tokens that didn't match anything confidently)
"""

from __future__ import annotations
import re
from dataclasses import dataclass, field

# ── Keyword tables (small, inlined for speed) ─────────────────────────────

_PROP_KEYWORDS: dict[str, str] = {
    # user term → canonical prop_id substring (or prop_group)
    "density": "density",
    "viscosity": "viscosity",
    "conductivity": "conductivity",
    "refractive": "refractive",
    "heat capacity": "heat_capacity",
    "cp": "heat_capacity",
    "enthalpy": "enthalpy",
    "entropy": "entropy",
    "gibbs": "gibbs",
    "surface tension": "surface_tension",
    "speed of sound": "speed_of_sound",
    "sound speed": "speed_of_sound",
    "diffusion": "diffusion",
    "osmotic": "osmotic",
    "activity coefficient": "activity_coefficient",
    "fugacity": "fugacity",
    "boiling": "boiling",
    "melting": "melting",
    "freezing": "melting",
    "vapor pressure": "vapor",
    "vapour pressure": "vapor",
    "vle": "mole_fraction",
    "lle": "liquidliquid",
    "sle": "solidliquid",
    "critical": "critical",
    "virial": "virial",
    "compressibility": "compressibility",
    "permittivity": "permittivity",
    "dielectric": "permittivity",
    "thermal expansion": "expansion",
    "excess": "excess",
    "partial molar": "partial_molar",
    "apparent molar": "apparent_molar",
    "solubility": "solubility",
    "interfacial": "interfacial",
}

_MEAS_KEYWORDS: dict[str, str] = {
    "calorimetry": "calorimetry",
    "calorimeter": "calorimetry",
    "dsc": "dsc",
    "dta": "dta",
    "chromatography": "chromatography",
    "gc": "chromatography",
    "hplc": "chromatography",
    "titration": "titration",
    "ebulliometry": "ebulliometric",
    "ebulliometric": "ebulliometric",
    "pycnometer": "pycnometric",
    "pycnometric": "pycnometric",
    "vibrating tube": "vibrating_tube",
    "densimeter": "vibrating_tube",
    "densitometer": "vibrating_tube",
    "refractometry": "refractometry",
    "refractometer": "refractometry",
    "viscometer": "viscometry",
    "viscometry": "viscometry",
    "rheometer": "viscometry",
    "interferometer": "interferometer",
    "gravimetric": "gravimetric",
    "static method": "static_method",
    "flow method": "flow",
}

_SYSTEM_TYPE_KEYWORDS = {
    "pure": "unary",
    "unary": "unary",
    "single component": "unary",
    "binary": "binary",
    "two component": "binary",
    "ternary": "ternary",
    "three component": "ternary",
    "quaternary": "quaternary",
    "mixture": None,  # any non-pure
}

_BLOCK_TYPE_KEYWORDS = {
    "reaction": "ReactionData",
    "combustion": "ReactionData",
    "dissolution": "ReactionData",
    "pure or mixture": "PureOrMixtureData",
    "thermophysical": "PureOrMixtureData",
}

# Noise words to strip
_NOISE = frozenset({
    "the", "a", "an", "of", "for", "in", "on", "at", "to", "and",
    "or", "with", "from", "by", "is", "are", "was", "were", "that",
    "this", "some", "any", "all", "data", "papers", "paper",
    "about", "discuss", "discussing", "studies", "study", "science",
    "using", "estimating", "measuring", "measured", "experimental",
    "involving", "containing", "their", "its", "between",
    "method", "methods", "technique", "techniques",
})

# ── Regex patterns ────────────────────────────────────────────────────────

_DOI_RE = re.compile(r'10\.\d{4,}/\S+', re.IGNORECASE)
_YEAR_RE = re.compile(r'\b(19|20)\d{2}\b')
_YEAR_RANGE_RE = re.compile(r'\b((?:19|20)\d{2})\s*[-–]\s*((?:19|20)\d{2})\b')
_FORMULA_RE = re.compile(
    r'^[A-Z][a-z]?(?:\d+)?(?:[A-Z][a-z]?(?:\d+)?){0,20}$'
)
_FORMULA_LIKELY_RE = re.compile(
    r'^(?:[A-Z][a-z]?\d*){2,}$'
)
_DATAPOINTS_RE = re.compile(r'(?:min|at\s+least)\s+(\d+)\s+(?:data\s*)?points?', re.IGNORECASE)
_NUM_COMPONENTS_RE = re.compile(r'(\d+)\s*[-–]?\s*component', re.IGNORECASE)


# ── Public API ────────────────────────────────────────────────────────────

@dataclass
class SearchBlock:
    """One AND-joined search clause."""
    compounds: list[str] = field(default_factory=list)
    properties: list[str] = field(default_factory=list)
    measurements: list[str] = field(default_factory=list)
    variables: list[str] = field(default_factory=list)
    constraints: list[str] = field(default_factory=list)
    phases: list[str] = field(default_factory=list)
    formulas: list[str] = field(default_factory=list)
    dois: list[str] = field(default_factory=list)
    authors: list[str] = field(default_factory=list)
    title_words: list[str] = field(default_factory=list)
    year_min: int | None = None
    year_max: int | None = None
    journals: list[str] = field(default_factory=list)
    system_type: str = ""
    block_type: str = ""
    min_datapoints: int | None = None
    n_components: int | None = None
    raw_tokens: list[str] = field(default_factory=list)
    unresolved: list[str] = field(default_factory=list)

    def is_empty(self) -> bool:
        return not any([
            self.compounds, self.properties, self.measurements,
            self.variables, self.constraints, self.phases,
            self.formulas, self.dois, self.authors, self.title_words,
            self.year_min, self.year_max, self.journals,
            self.system_type, self.block_type, self.min_datapoints,
            self.n_components,
        ])

    def to_dict(self) -> dict:
        d = {}
        for k in (
            'compounds', 'properties', 'measurements', 'variables',
            'constraints', 'phases', 'formulas', 'dois', 'authors',
            'title_words', 'journals', 'raw_tokens', 'unresolved',
        ):
            v = getattr(self, k)
            if v:
                d[k] = v
        for k in ('year_min', 'year_max', 'min_datapoints', 'n_components'):
            v = getattr(self, k)
            if v is not None:
                d[k] = v
        for k in ('system_type', 'block_type'):
            v = getattr(self, k)
            if v:
                d[k] = v
        return d


def parse_search_input(raw: str) -> list[SearchBlock]:
    """Parse a free-text search string into structured SearchBlocks.

    Syntax:
      • ``;`` separates independent OR-groups (each becomes a SearchBlock)
      • ``+`` within a group means AND (all terms must match)
      • Bare phrases are classified by heuristic

    Examples:
      "ethanol + viscosity"
        → one block: compounds=["ethanol"], properties=["viscosity"]

      "water + density; ethanol + heat capacity"
        → two blocks (OR): first has water+density, second has ethanol+heat_capacity

      "papers that discuss science of ethanol"
        → one block: compounds=["ethanol"]

      "some papers using calorimetry method for estimating DMF-water binary mixture"
        → one block: compounds=["DMF", "water"], measurements=["calorimetry"],
          system_type="binary"
    """
    if not raw or not raw.strip():
        return []

    raw = raw.strip()

    # Split on semicolons first → OR groups
    or_groups = [g.strip() for g in raw.split(';') if g.strip()]

    blocks: list[SearchBlock] = []
    for group in or_groups:
        block = _parse_single_block(group)
        if not block.is_empty() or block.unresolved:
            blocks.append(block)

    return blocks


def _parse_single_block(text: str) -> SearchBlock:
    """Parse one AND-group (separated by +)."""
    block = SearchBlock()

    # Extract DOIs first (they contain special chars)
    for m in _DOI_RE.finditer(text):
        block.dois.append(m.group(0).rstrip('.,;)'))
    text = _DOI_RE.sub(' ', text)

    # Extract year ranges (e.g. "2010-2020")
    for m in _YEAR_RANGE_RE.finditer(text):
        block.year_min = int(m.group(1))
        block.year_max = int(m.group(2))
    text = _YEAR_RANGE_RE.sub(' ', text)

    # Extract min datapoints
    m = _DATAPOINTS_RE.search(text)
    if m:
        block.min_datapoints = int(m.group(1))
        text = text[:m.start()] + ' ' + text[m.end():]

    # Extract n_components
    m = _NUM_COMPONENTS_RE.search(text)
    if m:
        block.n_components = int(m.group(1))
        text = text[:m.start()] + ' ' + text[m.end():]

    # Split on + for AND tokens
    tokens = [t.strip() for t in text.split('+') if t.strip()]

    for token in tokens:
        block.raw_tokens.append(token)
        _classify_token(token, block)

    return block


def _classify_token(token: str, block: SearchBlock) -> None:
    """Classify a single token and add it to the appropriate bucket."""
    t_lower = token.lower().strip()

    # Skip pure noise
    if t_lower in _NOISE:
        return

    # Strip leading/trailing noise words from multi-word token
    words = t_lower.split()
    words = [w for w in words if w not in _NOISE]
    if not words:
        return
    cleaned = ' '.join(words)

    # 1. Check for standalone year
    if re.fullmatch(r'(19|20)\d{2}', cleaned):
        y = int(cleaned)
        if block.year_min is None:
            block.year_min = y
        else:
            block.year_max = y
        return

    # 2. Check for block type keywords
    for kw, bt in _BLOCK_TYPE_KEYWORDS.items():
        if kw in cleaned:
            block.block_type = bt
            # Don't return — might also contain compound info
            break

    # 3. Check for system type keywords
    for kw, st in _SYSTEM_TYPE_KEYWORDS.items():
        if kw in cleaned:
            if st:
                block.system_type = st
            # Continue — "binary mixture of X" also has compound info
            # Remove the keyword from cleaned for further processing
            cleaned = cleaned.replace(kw, '').strip()
            words = [w for w in cleaned.split() if w not in _NOISE]
            cleaned = ' '.join(words)
            if not cleaned:
                return
            break

    # 4. Check for property keywords (multi-word first, then single-word)
    matched_prop = _match_keyword_table(cleaned, _PROP_KEYWORDS)
    if matched_prop:
        block.properties.append(matched_prop)
        return

    # 5. Check for measurement keywords
    matched_meas = _match_keyword_table(cleaned, _MEAS_KEYWORDS)
    if matched_meas:
        block.measurements.append(matched_meas)
        return

    # 6. Check if it looks like a molecular formula
    token_stripped = token.strip()
    if _FORMULA_LIKELY_RE.match(token_stripped) and len(token_stripped) <= 30:
        block.formulas.append(token_stripped)
        return

    # 7. Default: treat as compound name
    # But first, strip any remaining noise phrases
    if cleaned:
        block.compounds.append(cleaned)
    else:
        block.unresolved.append(token.strip())


def _match_keyword_table(text: str, table: dict[str, str]) -> str | None:
    """Check if text matches any keyword in the table.

    Returns the canonical value if matched, None otherwise.
    Tries multi-word keys first (longer = more specific).
    """
    # Sort by key length descending for greedy matching
    for kw in sorted(table, key=len, reverse=True):
        if kw in text:
            return table[kw]
    return None
