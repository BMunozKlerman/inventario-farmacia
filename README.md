# inventario-farmacia

Software architecture and Spec Kit assets for a pharmacy / controlled-medication
inventory management system (stakeholders: QF, ISP, SEREMI, MINSAL; POS
integration; controlled-substance tracking).

## `skills/`

Claude Code skills used to turn 7Cs architecture canvases into Spec Kit
artifacts (`constitution.md`, `spec.md`, `plan.md`), following the
"De canvas 7Cs a especificaciones ejecutables con Spec Kit" pipeline.

- **`7cs-architectural-context`** — reads an Architectural Context Canvas
  (7Cs) from a PDF or image and converts it into a structured Canvas
  Object Model (COM). Ingestion only; it does not write to
  `constitution.md` or `spec.md`. See `skills/7cs-architectural-context/SKILL.md`.

More canvas skills (Business Context, System Context, Structural,
Functional, Deployment) and the downstream mapping/orchestration/audit
skills are planned but not yet built.
