# inventario-farmacia

Software architecture and Spec Kit assets for a pharmacy / controlled-medication
inventory management system (stakeholders: QF, ISP, SEREMI, MINSAL; POS
integration; controlled-substance tracking).

## Repository structure

- **`resources/`** — original delivery PDFs, treated as immutable source
  material. Currently holds the team's canvas delivery,
  `[TDS DIS 2026] Equipo 2.pdf`, and a standalone System Context Canvas
  export, `system-context.pdf`.
- **`.agents/skills/7cs-architectural-context/`** — reads an Architectural Context
  Canvas (7Cs, 10 free-form sections) from a PDF or image and converts it
  into a structured Canvas Object Model (COM). Ingestion only; it does not
  write to `constitution.md` or `spec.md`. See
  `.agents/skills/7cs-architectural-context/SKILL.md`.
- **`.agents/skills/7cs-functional-A/`** — reads a Functional Canvas (7Cs,
  14 loose sections plus a `Bundles & components` frame) from a PDF or image
  and converts it into a COM. Ingestion only — same contract as the other two
  ingestion skills. See `.agents/skills/7cs-functional-A/SKILL.md` and
  `.agents/skills/7cs-functional-A/references/com-schema.md`.
- **`.agents/skills/7cs-functional-B/`** — Stage B mapping skill. Consumes
  the COM produced by `7cs-functional-A` (one per bundle, possibly several
  per delivery) and emits, per bundle, the `FR-{bundle.code}-{NNN}`
  fragment (with `Dado/Cuando/Entonces` scenarios) and the `§Key Entities`
  block for `/speckit.specify`, plus the technology stack + constraints for
  `/speckit.plan`. See `.agents/skills/7cs-functional-B/SKILL.md`.
- **`.agents/skills/7cs-system-context/`** — reads a System Context Canvas (7Cs,
  fixed 4×4 grid of Users/Systems/Repositories/Devices ×
  Source/Data input/Data output/Target, 16 sections) from a PDF or image and
  converts it into a COM. Same ingestion-only contract as the
  architectural-context skill. See `.agents/skills/7cs-system-context/SKILL.md`.
- **`com/`** — Canvas Object Models (JSON) persisted by the ingestion
  skills, one flat file per canvas: `<delivery_id>-<canvas>-p<n>.json`.
  Currently holds one processed Architectural Context page
  (`E1-architectural_context-p2.json`) and one processed System Context
  page (`E1-system_context-p1.json`).
- **`CLAUDE.md`** — repository guidelines (structure, naming conventions,
  commit style) for agents working in this repo.

More canvas skills (Business Context, Structural, Deployment) and the
downstream mapping/orchestration/audit skills, plus the `mapping/`,
`composed/`, `audit/`, and `evidence/` stages of the pipeline, are planned
but not yet built.
