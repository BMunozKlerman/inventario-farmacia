# inventario-farmacia

Software architecture and Spec Kit assets for a pharmacy / controlled-medication
inventory management system (stakeholders: QF, ISP, SEREMI, MINSAL; POS
integration; controlled-substance tracking).

## Repository structure

- **`resources/`** — original delivery PDFs, treated as immutable source
  material. Currently holds the team's canvas delivery,
  `[TDS DIS 2026] Equipo 2.pdf`.
- **`skills/7cs-architectural-context/`** — the only skill built so far. Reads
  an Architectural Context Canvas (7Cs) from a PDF or image and converts it
  into a structured Canvas Object Model (COM). Ingestion only; it does not
  write to `constitution.md` or `spec.md`. See
  `skills/7cs-architectural-context/SKILL.md`.
- **`skills/7cs-functional/`** — functional programming skill for analyzing and documenting the functional aspects of the pharmacy inventory system. This skill processes functional requirements and mappings to create structured functional specifications based on the 7CS framework.
- **`com/`** — Canvas Object Models (JSON) persisted by the skill, one flat
  file per canvas: `<delivery_id>-architectural_context-p<n>.json`. Currently
  holds one processed page from the delivery above.
- **`CLAUDE.md`** — repository guidelines (structure, naming conventions,
  commit style) for agents working in this repo.

More canvas skills (Business Context, System Context, Structural,
Functional, Deployment) and the downstream mapping/orchestration/audit
skills, plus the `mapping/`, `composed/`, `audit/`, and `evidence/` stages
of the pipeline, are planned but not yet built.
