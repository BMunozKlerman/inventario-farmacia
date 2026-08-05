---
name: 7cs-system-context
description: Reads a System Context Canvas (7Cs) from a PDF or image and converts it into a structured Canvas Object Model (COM) — header, sections, post-its, and groupers — with zero interpretation. Use this skill whenever the user uploads, attaches, or references a PDF or image of a System Context Canvas and needs it turned into structured data. This skill does NOT produce constitution.md or spec.md content, does not classify post-its by meaning, and does not apply any mapping rules — it only extracts the canvas into its COM. Mapping the COM to Spec Kit artifacts is a separate skill's job.
---

# 7cs-system-context

Ingestion-only skill. Turns a PDF page or image of a System Context
Canvas into a structured Canvas Object Model (COM). It maps nothing to
`constitution.md` or `spec.md` — that belongs to a different skill that
consumes this skill's output. Its only responsibility is faithful,
literal extraction: pixels to structured data, nothing more.

## when_to_use

The user provides a PDF or image whose title (top-left corner) reads
"System Context Canvas", or asks to extract, parse, digitize, or
structure a System Context Canvas.

## inputs

```yaml
input: pdf_path | image_path
  # a PDF page or an image (png/jpg) containing exactly one
  # System Context Canvas. Read it with native vision; do not
  # attempt external OCR unless the environment requires it.
delivery_id: string   # e.g. "E1"; if omitted, derive it from the filename
```

## outputs

```yaml
com: CanvasObjectModel   # the only output — full schema in references/com-schema.md
com_path: string         # where the COM was persisted, e.g. "com/E1-system_context-p1.json"
clarifications: [ string ]
```

## Golden rule

The COM does not interpret. It copies literal text and coordinates. No
mapping, no rewriting, no classifying post-its by meaning or destination —
only by which section physically contains them. All interpretation is out
of scope for this skill.

## procedure

1. **Isolate the page.** If the input is a multi-page PDF, treat each page
   as one image with no text layer. If it's already a single image, treat
   it as one page.
2. **Classify the page.** Read the title in the top-left corner. It must
   read "System Context Canvas". If it doesn't match — a different canvas
   type, a payroll table, a C4 diagram, a blank page — mark the page
   `out_of_scope`, emit a single clarification, and stop. Do not produce a
   COM for the wrong canvas.
3. **Read the header verbatim.** Capture System, Organization, Canvas,
   Version and Date exactly as written. Empty fields are valid data, not
   an error — record them as `null` and add a provenance clarification.
4. **Segment sections.** The System Context Canvas is a fixed 4×4 grid:
   four row categories (Users, Systems, Repositories, Devices) crossed
   with four column roles (Source, Data input interfaces, Data output
   interfaces, Target), for sixteen sections total, each a white
   rectangle with its own printed label: Source users, User data input
   interfaces, User data output interfaces, Target users, Source systems,
   System data input interfaces, System data output interfaces, Target
   systems, Source repositories, Repository data input interfaces,
   Repository data output interfaces, Target repositories, Source
   devices, Device data input interfaces, Device data output interfaces,
   Target devices. Unlike the Architectural Context Canvas, all sixteen
   boxes belong to the fixed template and are normally printed even when
   empty of post-its — record a present-but-empty section as a
   `sections[]` entry with `stickies: []`, not as an absent one. Only a
   section box missing from the printed grid itself goes into
   `empty_sections`.
5. **Read post-its literally.** Each yellow rectangle produces a record
   with its literal text, its bounding box, and the section that contains
   it. Font size varies across post-its — never infer importance,
   priority, or category from it. Copy the text exactly as printed; do
   not correct spelling, expand abbreviations, or paraphrase.
6. **Resolve groupers.** A bordered rectangle that encloses post-its and
   carries a loose label encodes a composition relationship. Represent it
   as a parent/child hierarchy in the COM — don't flatten it into
   standalone post-its.
7. **Assemble and emit the COM.** Follow the schema and field-by-field
   notes in `references/com-schema.md` — read it before writing the first
   COM of a session, and whenever a field's shape is unclear.
8. **Persist the COM.** Write the assembled COM as JSON to a flat file
   directly under `com/` — no per-delivery subfolder — named
   `com/<delivery_id>-system_context-p<n>.json`, where `<n>` is the page
   number from the `source` field (`p1` if the input is a single image).
   Report that path as `com_path` in the output.

## guardrails

- Never map a post-it to a constitution or spec destination — that is a
  different skill's responsibility, not this one's.
- Never rewrite, summarize, translate, or paraphrase a post-it's text —
  copy it exactly as printed, in its original language.
- Never infer or invent header fields, section names, or post-it text
  that isn't legible in the image.
- An illegible post-it → `[NEEDS CLARIFICATION: illegible post-it in
  <section>]`, never a guessed transcription.
- A canvas whose title doesn't match "System Context Canvas" →
  `out_of_scope` clarification, stop immediately, emit no COM.
- Never persist the COM anywhere other than
  `com/<delivery_id>-system_context-p<n>.json` — a flat filename directly
  under `com/`, with no per-delivery subfolder, that downstream mapping
  and orchestration skills depend on.
- Never generate an ingest report or a page index (e.g. `<delivery_id>-
  ingest-report.md`, `<delivery_id>-page-index.json`) — those are
  produced by a separate orchestration skill that aggregates all canvases
  in a delivery, not by this one.

## acceptance

```yaml
- com.sections cover all sixteen sections printed on the canvas grid,
  including present-but-empty ones (stickies: [])
- every sticky record has text, bbox, and a containing section
- no sticky text differs from what is printed on the canvas
- if the canvas type doesn't match, the output is a single out_of_scope
  clarification and no COM is produced
- the COM is persisted as a flat file at
  `com/<delivery_id>-system_context-p<n>.json` (no subfolder) and
  `com_path` in the output matches that path
```

## Reference files

- `references/com-schema.md` — full COM JSON schema, field-by-field
  notes, section code prefixes, and a worked example extracted from a
  real canvas. Read it before assembling your first COM.
- `references/rewriting-rules.md` — the section→destination mapping
  table and the rewriting rules that a *downstream* mapping skill applies
  to this COM to produce `constitution.md` and `spec.md` fragments. This
  ingestion skill does not apply them itself — they're kept here so both
  skills stay consistent once the mapping skill is built.

## Fit in the pipeline

This is the Stage A ingestion step, scoped to System Context Canvases
only. Its output (the COM), persisted as a flat file at
`com/<delivery_id>-system_context-p<n>.json`, is the sole input for a
separate mapping skill that applies the rules in
`references/rewriting-rules.md` to produce `constitution.md` and
`spec.md` fragments. This skill never produces that mapped text itself.
Companion delivery-level artifacts (an ingest report, a page index) are
produced by a separate orchestration skill, not by this one.
