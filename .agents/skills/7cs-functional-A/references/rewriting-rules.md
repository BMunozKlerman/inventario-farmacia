# Rewriting Rules — Functional Canvas → Spec Kit

This file exists for symmetry with `7cs-architectural-context/references/rewriting-rules.md`
and `7cs-system-context/references/rewriting-rules.md`, which each carry
the section→destination mapping table and the rewriting rules that the
**downstream mapping skill** applies to its COM.

## Where the real rules live

The mapping rules for the Functional Canvas are in
`7cs-functional-B/references/reglas-reescritura.md` — the R1–R7 table
that turns post-its into:

- **R1** — entities for `spec.md §Key Entities` (attributes open, never
  invented)
- **R2** — functional requirements (`FR-{bundle.code}-{NNN}`) with a
  `Dado/Cuando/Entonces` scenario
- **R3** — integration FRs (with the technology name moved to `plan.md`)
- **R4** — time-triggered jobs (with `[NEEDS CLARIFICATION: periodicidad]`
  when the canvas omits it)
- **R5** — success criteria (never an FR)
- **R6** — technology names into `plan.md` / `constitution.md`, out of
  `spec.md`
- **R7** — external limits with a compensating FR explicitly derived

## Why this file is empty

`7cs-functional-A` is ingestion-only. By the Golden Rule, it does not
interpret, classify, or map post-its — that is exclusively the job of
`7cs-functional-B`. Keeping a placeholder here (rather than a copy of
the R1–R7 table) is deliberate: a single source of truth for the rules
lives next to the skill that applies them, and there is no risk of the
ingestion skill drifting into mapping behaviour.

If you are reading this file because you want to understand how a
Functional Canvas post-it becomes a requirement, read
`7cs-functional-B/references/reglas-reescritura.md`. If you are reading
this file because you want to assemble a COM, you only need
`7cs-functional-A/references/com-schema.md`.