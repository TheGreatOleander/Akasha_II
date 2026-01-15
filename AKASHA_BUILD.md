# AKASHA II — DETERMINISTIC DELTA ZIP BUILD (CANONICAL)

## EXECUTION TRIGGER
Execution is automatic upon repository inspection when both:
- AKASHA_BUILD.md
- AKASHA_LEDGER.md
are present at repository root.

No confirmation. No dialogue.

## OUTPUT MODE (MANDATORY)
OUTPUT_MODE: VERSIONED_DELTA_ZIP

Failure to emit a ZIP artifact constitutes build failure.

## VERSION AUTHORITY
AKASHA_LEDGER.md is the sole authority.

The active version is read from:
## VERSION_AUTHORITY
current: X.Y.Z

Version increments are permitted ONLY if deltas are emitted.

## DELTA RULES (GENERATION)
- Only new or changed files may be generated.
- Unchanged files MUST NOT be regenerated.
- No placeholders, TODOs, or stubs.
- All output must be production-valid.

## ZIP RULES (DELIVERY)
- A ZIP artifact MUST be materialized.
- The ZIP MUST contain:
  - Only new or changed files
  - Preserved canonical paths
- The ZIP filename MUST be:

Akasha_II_delta_vX.Y.Z.zip

## BUILD COMPLETION DEFINITION
A build is complete ONLY when:
1. Deltas are generated
2. Version is resolved
3. ZIP artifact is created and downloadable

No ZIP = build failed.
