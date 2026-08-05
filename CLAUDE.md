# Repository Guidelines

## Project Structure & Module Organization

This repository is building a 7Cs-to-Spec Kit documentation pipeline. Only the
ingestion stage exists so far, covering two canvas types: Architectural
Context and System Context.

- `resources/`: original delivery PDFs; treat as immutable source material.
- `.agents/skills/7cs-architectural-context/`: ingests a PDF page or image of an
  Architectural Context Canvas (10 free-form sections) into a Canvas Object
  Model (COM). See its `SKILL.md` for the full contract, and
  `references/com-schema.md` and `references/rewriting-rules.md` for the COM
  schema and the rewriting rules a future mapping skill will apply.
- `.agents/skills/7cs-system-context/`: ingests a PDF page or image of a System
  Context Canvas (fixed 4×4 grid — Users/Systems/Repositories/Devices ×
  Source/Data input/Data output/Target, 16 sections total) into a COM. Same
  contract shape as the architectural-context skill; see its own `SKILL.md`
  and `references/`.
- `com/`: Canvas Object Models (JSON) persisted by the skills, one flat file
  per canvas — no per-delivery subfolder.

No other pipeline stage (canvas-mapping skills beyond these two, `mapping/`,
`composed/`, `audit/`, `evidence/`, `scripts/`) exists in this repository yet.
Don't assume they do.

Use delivery-prefixed, flat names for everything under `com/`, e.g.
`com/E1-architectural_context-p2.json` or `com/E1-system_context-p1.json` —
`<delivery_id>-<canvas>-p<n>.json`, where `<n>` is the real page number the
canvas was found on. Post-it IDs are stable and section-coded, e.g.
`ACC-ST-01` (Architectural Context Canvas) or `SCC-SU-01` (System Context
Canvas) — see the section code prefix table in each skill's
`references/com-schema.md`.

## Build, Test, and Development Commands

There is no application build, package manager, or script in this repository.
Each skill runs by having an agent read and follow its `SKILL.md`
(`.agents/skills/7cs-architectural-context/SKILL.md` or
`.agents/skills/7cs-system-context/SKILL.md`) against a PDF or image; there is no CLI
entry point yet.

Useful manual checks:

```bash
jq . com/E1-architectural_context-p2.json
jq . com/E1-system_context-p1.json
```

## Coding Style & Naming Conventions

Preserve literal canvas text — including original spelling — in every COM field.
Never infer, invent, or complete header fields, section names, post-it text, or
metrics that aren't legible in the source. Use `[NEEDS CLARIFICATION: ...]`
instead of guessing.

## Testing Guidelines

There is no automated test suite yet. Each skill's `SKILL.md` defines its own
`acceptance` criteria (section coverage, one record per sticky, literal text
preservation, `out_of_scope` handling, and the `com_path` output matching the
persisted file). Treat those as the pass/fail bar for that skill until a
dedicated audit stage is built.

## Commit & Pull Request Guidelines

Existing history uses Conventional Commits (`feat:`, `fix:`, `chore:`), one-line,
imperative — e.g. `fix: persist COM as flat com/<delivery_id>-architectural_context-p<n>.json`.
Follow that convention for new commits.
