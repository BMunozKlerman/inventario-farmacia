---
name: 7cs-architectural-context
description: Reads an Architectural Context Canvas (7Cs) from a PDF or image and converts it into a structured Canvas Object Model (COM) — header, sections, post-its, and groupers — with zero interpretation. Use this skill whenever the user uploads, attaches, or references a PDF or image of an Architectural Context Canvas and needs it turned into structured data. This skill does NOT produce constitution.md or spec.md content, does not classify post-its by meaning, and does not apply any mapping rules — it only extracts the canvas into its COM. Mapping the COM to Spec Kit artifacts is a separate skill's job.
---

# 7cs-architectural-context

Ingestion-only skill. Turns a PDF page or image of an Architectural
Context Canvas into a structured Canvas Object Model (COM). It maps
nothing to `constitution.md` or `spec.md` — that belongs to a different
skill that consumes this skill's output. Its only responsibility is
faithful, literal extraction: pixels to structured data, nothing more.

## when_to_use

The user provides a PDF or image whose title (top-left corner) reads
"Architectural Context Canvas", or asks to extract, parse, digitize, or
structure an Architectural Context Canvas.

## inputs

```yaml
input: pdf_path | image_path
  # a PDF page or an image (png/jpg) containing exactly one
  # Architectural Context Canvas. Read it with native vision; do not
  # attempt external OCR unless the environment requires it.
delivery_id: string   # e.g. "E1"; if omitted, derive it from the filename
```

## outputs

```yaml
com: CanvasObjectModel   # the only output — full schema in references/com-schema.md
com_path: string         # where the COM was persisted, e.g. "com/E1/architectural-context.json"
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
   read "Architectural Context Canvas". If it doesn't match — a different
   canvas type, a payroll table, a C4 diagram, a blank page — mark the
   page `out_of_scope`, emit a single clarification, and stop. Do not
   produce a COM for the wrong canvas.
3. **Read the header verbatim.** Capture System, Organization, Canvas,
   Version and Date exactly as written. Empty fields are valid data, not
   an error — record them as `null` and add a provenance clarification.
4. **Segment sections.** Sections are white rectangles on a gray
   background, each with its own printed label. Detect them by their
   outline and label them with the text actually printed on them — not by
   fixed position, since position and order vary between canvases. Ten
   sections are expected for this canvas type: Stakeholders, Business
   strategy, IT strategy, Business goals & drivers, Technology goals &
   drivers, Business standards & policies, Technology standards &
   policies, Situational constraints, Business principles, Technical
   principles. A section physically absent from the image goes into
   `empty_sections`, not into a clarification about missing data — its
   absence is not necessarily an error.
5. **Read post-its literally.** Each yellow rectangle produces a record
   with its literal text, its bounding box, and the section that contains
   it. Font size varies across post-its — never infer importance,
   priority, or category from it. Copy the text exactly as printed; do
   not correct spelling, expand abbreviations, or paraphrase.
6. **Resolve groupers.** A bordered rectangle that encloses post-its and
   carries a loose label (e.g. "Público general") encodes a composition
   relationship. Represent it as a parent/child hierarchy in the COM —
   don't flatten it into standalone post-its.
7. **Assemble and emit the COM.** Follow the schema and field-by-field
   notes in `references/com-schema.md` — read it before writing the first
   COM of a session, and whenever a field's shape is unclear.
8. **Persist the COM.** Write the assembled COM as JSON to
   `com/<delivery_id>/architectural-context.json`, creating the directory
   if it doesn't exist yet. Report that path as `com_path` in the output.

## guardrails

- Never map a post-it to a constitution or spec destination — that is a
  different skill's responsibility, not this one's.
- Never rewrite, summarize, translate, or paraphrase a post-it's text —
  copy it exactly as printed, in its original language.
- Never infer or invent header fields, section names, or post-it text
  that isn't legible in the image.
- An illegible post-it → `[NEEDS CLARIFICATION: illegible post-it in
  <section>]`, never a guessed transcription.
- A canvas whose title doesn't match "Architectural Context Canvas" →
  `out_of_scope` clarification, stop immediately, emit no COM.
- Never persist the COM anywhere other than
  `com/<delivery_id>/architectural-context.json` — a fixed, predictable
  path the downstream mapping skill depends on.

## acceptance

```yaml
- com.sections cover every section physically present on the canvas image
- every sticky record has text, bbox, and a containing section
- no sticky text differs from what is printed on the canvas
- if the canvas type doesn't match, the output is a single out_of_scope
  clarification and no COM is produced
- the COM is persisted at `com/<delivery_id>/architectural-context.json`
  and `com_path` in the output matches that path
```

## Reference files

- `references/com-schema.md` — full COM JSON schema, field-by-field
  notes, section code prefixes, and a worked example extracted from a
  real canvas. Read it before assembling your first COM.
- `references/rewriting-rules.md` — the section→destination mapping
  table and the R-Q / R-C / R-T rewriting rules that a *downstream*
  mapping skill applies to this COM to produce `constitution.md` and
  `spec.md` fragments. This ingestion skill does not apply them itself —
  they're kept here so both skills stay consistent once the mapping
  skill is built.

## Fit in the pipeline

This is the Stage A ingestion step, scoped to Architectural Context
Canvases only. Its output (the COM), persisted at
`com/<delivery_id>/architectural-context.json`, is the sole input for a
separate mapping skill that applies the rules in
`references/rewriting-rules.md` to produce `constitution.md` and
`spec.md` fragments. This skill never produces that mapped text itself.
