# Repository Guidelines

## Project Structure & Module Organization

This repository is building a 7Cs-to-Spec Kit documentation pipeline. Only the
first stage exists so far — ingestion of the Architectural Context Canvas.

- `resources/`: original delivery PDFs; treat as immutable source material.
- `skills/7cs-architectural-context/`: the only skill built so far. Ingests a PDF
  page or image of an Architectural Context Canvas into a Canvas Object Model
  (COM). See its `SKILL.md` for the full contract, and `references/com-schema.md`
  and `references/rewriting-rules.md` for the COM schema and the rewriting rules
  a future mapping skill will apply.
- `com/`: Canvas Object Models (JSON) persisted by the skill, one flat file per
  canvas — no per-delivery subfolder.

No other pipeline stage (canvas-mapping skills beyond this one, `mapping/`,
`composed/`, `audit/`, `evidence/`, `scripts/`) exists in this repository yet.
Don't assume they do.

Use delivery-prefixed, flat names for everything under `com/`, e.g.
`com/E1-architectural_context-p2.json` — `<delivery_id>-architectural_context-p<n>.json`,
where `<n>` is the real page number the canvas was found on. Post-it IDs are
stable and section-coded, e.g. `E1-ST-01` (see the section code prefix table in
`skills/7cs-architectural-context/references/com-schema.md`).

## Build, Test, and Development Commands

There is no application build, package manager, or script in this repository.
The skill runs by having an agent read and follow
`skills/7cs-architectural-context/SKILL.md` against a PDF or image; there is no
CLI entry point yet.

Useful manual checks:

```bash
jq . com/E1-architectural_context-p2.json
```

## Coding Style & Naming Conventions

Preserve literal canvas text — including original spelling — in every COM field.
Never infer, invent, or complete header fields, section names, post-it text, or
metrics that aren't legible in the source. Use `[NEEDS CLARIFICATION: ...]`
instead of guessing.

## Testing Guidelines

There is no automated test suite yet. `skills/7cs-architectural-context/SKILL.md`
defines its own `acceptance` criteria (section coverage, one record per sticky,
literal text preservation, `out_of_scope` handling, and the `com_path` output
matching the persisted file). Treat those as the pass/fail bar for this skill
until a dedicated audit stage is built.

## Commit & Pull Request Guidelines

Existing history uses Conventional Commits (`feat:`, `fix:`, `chore:`), one-line,
imperative — e.g. `fix: persist COM as flat com/<delivery_id>-architectural_context-p<n>.json`.
Follow that convention for new commits.
