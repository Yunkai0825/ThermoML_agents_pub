# Claim-verification method

This package contains claim-level judgments only. It intentionally excludes
whole-answer scores, workflow comparisons, timing, token use, and cost.

## Resolved categories

- **database_verified**: the claim matches original raw ThermoML records after
  checking the applicable system, property, phase, composition and basis,
  temperature, pressure, units, method, and provenance.
- **domain_knowledge**: the claim is correct physical chemistry, a supported
  primary-literature fact, a valid conversion/calculation/interpolation, or an
  appropriately qualified physical interpretation. Derived values are not
  reclassified as original measurements.
- **incorrect**: the value, definition, scope, attribution, inference, or
  causal/proof claim is demonstrably wrong.

The categories are mutually exclusive. An absent citation alone is not an
incorrect claim. A database match verifies faithful alignment with the stored
record; it does not independently certify the experiment.

## Claim units

A unit is a substantive scientific assertion or coupled experimental tuple,
not each numeral. Repeated summaries, label-only headings, workflow text,
confidence statements, and deterministic ledger restatements are not counted
again. Distinct numerical and interpretive assertions may be separated.

## Unresolved empirical assertions

Five narrow assertions could not be responsibly assigned to a resolved
category from the accessible evidence. They are retained under
`unresolved_claims` in the corresponding answer files and are not a fourth
category or part of the 796 resolved-claim denominator.

## Evidence and paths

Evidence values are retained losslessly apart from rewriting references to the
six retained support artifacts as `evidence/<name>`. Those paths are relative
to this directory. Absolute raw-database and external literature references
remain provenance references.

The original rendered-answer path is stored as `source_path_at_review`
together with its review-time SHA-256. Six hierarchical sources remain
available and were reverified; 36 historical paths are no longer present.
Their stored hashes are identity records, not claims that those paths are live.

## Physical-chemistry safeguards

The review distinguishes mole fraction, mass fraction, and molality; pure
endpoints and mixture interiors; measured, derived, and excess properties;
mass-specific and molar heat capacities; mutual and tracer diffusion; and
measurement uncertainty versus inter-paper scatter. Mechanistic plausibility
does not establish a unique cause. SRD-46 contains different observables here,
so it is not treated as a numerical alignment source for these ThermoML claims.
