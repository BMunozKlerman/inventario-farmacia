---
name: 7cs-functional-A
description: Reads a Functional Canvas (7Cs) from a PDF or image and converts it into a structured Canvas Object Model (COM) — header, sections, post-its, and the Bundles & components frame — with zero interpretation. Use this skill whenever the user uploads, attaches, or references a PDF or image of a Functional Canvas and needs it turned into structured data. This skill does NOT produce constitution.md or spec.md content, does not classify post-its by meaning, does not derive FRs or Given/When/Then scenarios, and does not apply any mapping rules — it only extracts the canvas into its COM. Mapping the COM to Spec Kit artifacts (FR + §Key Entities + plan stack) is the separate skill 7cs-functional-B.
---

# 7cs-functional-A

Ingestion-only skill. Turns a PDF page or image of a Functional
Canvas into a structured Canvas Object Model (COM). It maps nothing to
`constitution.md`, `spec.md`, or `plan.md` — that belongs to
`7cs-functional-B`, which consumes this skill's COM. Its only
responsibility is faithful, literal extraction: pixels to structured
data, nothing more.

## when_to_use

The user provides a PDF or image whose title (top-left corner) reads
"Functional Canvas", or asks to extract, parse, digitize, or structure a
Functional Canvas. The Functional Canvas has fourteen sections that
typically appear as loose labelled rectangles on a gray background
(plus a "Bundles & components" frame that lists the bundle names whose
Functional Canvas this is — not a hierarchical grouper).

## inputs

```yaml
input: pdf_path | image_path
  # a PDF page or an image (png/jpg) containing exactly one
  # Functional Canvas. Read it with native vision; do not
  # attempt external OCR unless the environment requires it.
delivery_id: string   # e.g. "E1"; if omitted, derive it from the filename
```

## outputs

```yaml
com: CanvasObjectModel   # the only output — full schema in references/com-schema.md
com_path: string         # where the COM was persisted, e.g. "com/E1-functional-p7.json"
clarifications: [ string ]
```

## Golden rule

The COM does not interpret. It copies literal text and coordinates. No
mapping, no rewriting, no classifying post-its by meaning or destination
into FR / Key Entities / plan — only by which section physically
contains them. All interpretation is out of scope for this skill and is
the job of `7cs-functional-B`.

## procedure

1. **Isolate the page.** If the input is a multi-page PDF, treat each page
   as one image with no text layer. If it's already a single image, treat
   it as one page.
2. **Classify the page.** Read the title in the top-left corner. It must
   read "Functional Canvas". If it doesn't match — a different canvas
   type, a payroll table, a C4 diagram, a blank page — mark the page
   `out_of_scope`, emit a single clarification, and stop. Do not
   produce a COM for the wrong canvas.
3. **Read the header verbatim.** Capture System, Organization, Canvas,
   Version and Date exactly as written. Empty fields are valid data, not
   an error — record them as `null` and add a provenance clarification.
4. **Segment sections.** Sections are white rectangles on a gray
   background, each with its own printed label. Detect them by their
   outline and label them with the text actually printed on them — not by
   fixed position, since position and order vary between canvases.
   Fourteen sections are expected for this canvas type, in roughly
   reading order: Bundles & components, Data objects, User inputs,
   UI-processing inputs, API inputs, Data imports, Data exports, Jobs,
   Event handlers, Event triggers, Helpers, User visualizations /
   reports, Technology stack, Constraints. A section physically absent
   from the image goes into `empty_sections`, not into a clarification
   about missing data — its absence is not necessarily an error. A
   section present but containing no post-its stays in `sections[]` with
   `stickies: []`.
5. **Read post-its literally.** Each yellow rectangle produces a record
   with its literal text, its bounding box, and the section that contains
   it. Font size varies across post-its — never infer importance,
   priority, or category from it. Copy the text exactly as printed; do
   not correct spelling, expand abbreviations, or paraphrase. Post-it
   ids follow the `FNC-<section-code>-<NN>` format (see
   `references/com-schema.md`).
6. **Resolve the Bundles & components frame (not a grouper).** The
   "Bundles & components" rectangle is a list of bundle names whose
   Functional Canvas this page is — it is **not** a hierarchical
   grouper. Record its post-its as plain stickies in the `Bundles &
   components` section (with `parent: null`); do not nest other stickies
   under them. If a future variant of the canvas carries a bordered
   rectangle enclosing post-its with a loose label, model it as a
   grouper (`groupers[]` with `parent` references) following the
   convention in `references/com-schema.md`.
7. **Assemble and emit the COM.** Follow the schema and field-by-field
   notes in `references/com-schema.md` — read it before writing the first
   COM of a session, and whenever a field's shape is unclear.
8. **Persist the COM.** Write the assembled COM as JSON to a flat file
   directly under `com/` — no per-delivery subfolder — named
   `com/<delivery_id>-functional-p<n>.json`, where `<n>` is the page
   number from the `source` field (`p1` if the input is a single image).
   Report that path as `com_path` in the output. When the delivery has
   several Functional Canvases (one per bundle, possibly on the same or
   different pages), persist one COM per Functional Canvas — the
   downstream skill `7cs-functional-B` iterates over them.

## guardrails

- Never map a post-it to a constitution, spec, or plan destination — that
  is `7cs-functional-B`'s responsibility, not this one's.
- Never derive FRs, `FR-{bundle}-{NNN}` ids, Dado/Cuando/Entonces
  scenarios, or `Key Entities` from this skill — that is mapping, not
  ingestion.
- Never rewrite, summarize, translate, or paraphrase a post-it's text —
  copy it exactly as printed, in its original language.
- Never infer or invent header fields, section names, or post-it text
  that isn't legible in the image.
- An illegible post-it → `[NEEDS CLARIFICATION: illegible post-it in
  <section>]`, never a guessed transcription.
- A canvas whose title doesn't match "Functional Canvas" →
  `out_of_scope` clarification, stop immediately, emit no COM.
- Never persist the COM anywhere other than
  `com/<delivery_id>-functional-p<n>.json` — a flat filename directly
  under `com/`, with no per-delivery subfolder, that downstream
  mapping and orchestration skills depend on.
- Never generate an ingest report or a page index (e.g. `<delivery_id>-
  ingest-report.md`, `<delivery_id>-page-index.json`) — those are
  produced by a separate orchestration skill that aggregates all canvases
  in a delivery, not by this one.

## acceptance

```yaml
- com.sections cover every section physically present on the canvas image
  (present-but-empty sections stay in sections[] with stickies: [])
- com.empty_sections lists the names of the 14 expected sections whose
  box is physically absent from the image (not merely empty of stickies)
- every sticky record has text, bbox, a containing section, and an id
  matching `^FNC-[A-Z]+-[0-9]+$`
- no sticky text differs from what is printed on the canvas
- if the canvas type doesn't match, the output is a single out_of_scope
  clarification and no COM is produced
- the COM is persisted as a flat file at
  `com/<delivery_id>-functional-p<n>.json` (no subfolder) and
  `com_path` in the output matches that path
```

## Reference files

- `references/com-schema.md` — full COM JSON schema, field-by-field
  notes, the 14-section code prefix table, and a worked example
  extracted from an illustrative canvas. Read it before assembling your
  first COM.
- `references/rewriting-rules.md` — the section→destination mapping
  table and the R1–R7 rewriting rules that `7cs-functional-B` applies
  to this COM to produce FRs, §Key Entities, and plan stack. This
  ingestion skill does not apply them itself — they're kept here so
  both skills stay consistent once the mapping skill runs.

## Fit in the pipeline

This is the Stage A ingestion step, scoped to Functional Canvases only.
Its output (the COM), persisted as a flat file at
`com/<delivery_id>-functional-p<n>.json`, is the sole input for
`7cs-functional-B`, which applies the R1–R7 rules in
`references/rewriting-rules.md` to produce the `FR-{bundle.code}-{NNN}`
fragment (for `spec.md`), the `§Key Entities` block, and the
`plan_context` (for `plan.md`). This skill never produces that mapped
text itself. Companion delivery-level artifacts (an ingest report, a
page index) are produced by a separate orchestration skill, not by this
one.