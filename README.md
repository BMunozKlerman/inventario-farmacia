# inventario-farmacia

Software architecture and Spec Kit assets for a pharmacy / controlled-medication
inventory management system (stakeholders: QF, ISP, SEREMI, MINSAL; POS
integration; controlled-substance tracking).

## Repository structure

- **`resources/`** — original delivery PDFs, treated as immutable source
  material. Currently holds the team's canvas delivery,
  `[TDS DIS 2026] Equipo 2.pdf`, and a standalone System Context Canvas
  export, `system-context.pdf`.
- **`skills/7cs-architectural-context/`** — reads an Architectural Context
  Canvas (7Cs, 10 free-form sections) from a PDF or image and converts it
  into a structured Canvas Object Model (COM). Ingestion only; it does not
  write to `constitution.md` or `spec.md`. See
  `skills/7cs-architectural-context/SKILL.md`.
- **`skills/7cs-system-context/`** — reads a System Context Canvas (7Cs,
  fixed 4×4 grid of Users/Systems/Repositories/Devices ×
  Source/Data input/Data output/Target, 16 sections) from a PDF or image and
  converts it into a COM. Same ingestion-only contract as the
  architectural-context skill. See `skills/7cs-system-context/SKILL.md`.
- **`com/`** — Canvas Object Models (JSON) persisted by the skills, one flat
  file per canvas: `<delivery_id>-<canvas>-p<n>.json`. Currently holds one
  processed Architectural Context page (`E1-architectural_context-p2.json`)
  and one processed System Context page (`E1-system_context-p1.json`).
- **`CLAUDE.md`** — repository guidelines (structure, naming conventions,
  commit style) for agents working in this repo.

More canvas skills (Business Context, Structural, Functional, Deployment)
and the downstream mapping/orchestration/audit skills, plus the `mapping/`,
`composed/`, `audit/`, and `evidence/` stages of the pipeline, are planned
but not yet built.
