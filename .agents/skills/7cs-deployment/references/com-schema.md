# COM Schema — Deployment Canvas

Full JSON shape for the Canvas Object Model produced by **phase 1
(ingestion)** of `7cs-deployment`. Read this before assembling or
validating a COM, and whenever a field's shape is unclear.

**Golden rule: the COM does not interpret.** It copies literal text and
coordinates. Every judgement — whether an empty `Cloud abstractions` is
coherent, whether a post-it rises to `spec.md` or stays in `plan.md`,
whether the `Bundles` section agrees with the Structural census — belongs
to **phase 2 (mapping)** and never appears inside the COM.

## Top-level fields

| Field | Type | Notes |
|---|---|---|
| `source` | string | `"<filename>#p<n>"` |
| `canvas` | string | constant: `"deployment"` |
| `template` | string \| null | version read from the footer, e.g. `"7Cs v1.1 June 2026"`; `null` if illegible |
| `delivery_id` | string | from input, or derived from the filename if omitted |
| `header` | object | `system`, `organization`, `canvas`, `version`, `date` — each `string \| null` |
| `sections` | array | one entry per section printed on the template (15 total; present-but-empty ones included with `stickies: []`) |
| `empty_sections` | array of strings | names of the 15 expected sections whose box is physically absent from the printed template (not merely empty of stickies) |
| `notes` | array of strings | optional; literal evidence with no field of its own, e.g. a legible connector arrow between two post-its. Omit when empty |

## `sections[]` entry

```json
{ "name": "<section name as printed>", "stickies": [ <sticky>, ... ] }
```

## `sticky` object

| Field | Type | Notes |
|---|---|---|
| `id` | string | `DPC-<section-code>-<NN>`, e.g. `"DPC-EN-01"`; `NN` zero-padded to 2 digits, numbered in reading order within the section |
| `text` | string | literal, unedited — same language, same spelling, acronyms unexpanded |
| `bbox` | `[x0, y0, x1, y1]` | best-effort pixel / reading-order estimate in the frame of the rendered page; not guaranteed exact unless a vector-aware parser is available |
| `parent` | string \| null | `id` of the enclosing grouper sticky, if any |

## Section code prefixes

The canvas-level prefix is `DPC` (Deployment Canvas). Each of the fifteen
sections also has a short code used in sticky ids as `DPC-<code>-<NN>`.

| Code | Section | Column |
|---|---|---|
| `EN` | Environments | left |
| `CO` | Constraints | left |
| `BU` | Bundles | middle |
| `MW` | Middleware | middle |
| `RT` | Runtime | middle |
| `OR` | Orchestration & scheduling | middle |
| `CR` | Container runtimes | middle |
| `OS` | Operating systems | middle |
| `VE` | Virtualization engines | middle |
| `CA` | Cloud abstractions | middle |
| `HW` | Hardware | middle |
| `LO` | Locations | middle |
| `NW` | Networks | right |
| `IN` | Installation | right |
| `OP` | Operation | right |

`OR` (Orchestration & scheduling) and `OS` (Operating systems) are
deliberately distinct — never abbreviate both to `OS`.

Section names are copied **as printed on the template** (in English), even
when the post-it text is in Spanish: they are the canvas's own labels, not
a translation.

## Conventions

- **`canvas`** belongs to the pipeline's closed vocabulary; `"deployment"`
  for this skill. Any other page (another canvas type, a C4 diagram, a
  payroll table, a blank sheet) is marked `out_of_scope` in the page index
  and produces no COM.
- **Ids are stable across runs** (idempotence): the same canvas
  re-ingested yields the same `DPC-<code>-<NN>` for the same post-it.
- **Empty is evidence, not omission.** A printed section with no post-its
  stays in `sections[]` with `stickies: []`. Its *meaning* (coherent vs
  inconsistent) is not recorded here.
- **Font size is not data.** A post-it printed three times larger than its
  neighbours carries no extra priority; record only text and `bbox`.
- **Arrows are not groupers.** Connectors between post-its go to `notes[]`
  if legible, never into `parent`, and never merge the two post-its they
  join.
- **`header`**: literal header fields. `null` when empty — an empty header
  is also data and produces an artifact-identification clarification.

## Additional phase 2 input (not part of the COM)

- **`bundle_census`** — the bundle list produced by `7cs-structural`.
  Required by rule R-B (deployable-unit reconciliation). If it's missing,
  the skill emits a clarification and does not reconcile on its own.

## Worked example (real canvas — `[TDS DIS 2026] Equipo 2.pdf`, p. 6)

Fifteen sections printed, fifteen post-its, five present-but-empty
sections (`Operating systems`, `Virtualization engines`,
`Cloud abstractions`, `Hardware`, `Locations`), empty header.

```json
{
  "source": "[TDS DIS 2026] Equipo 2.pdf#p6",
  "canvas": "deployment",
  "template": "7Cs v1.1 June 2026",
  "delivery_id": "E1",
  "header": { "system": null, "organization": null, "canvas": null, "version": null, "date": null },
  "sections": [
    { "name": "Environments",
      "stickies": [
        { "id": "DPC-EN-01", "text": "Desarrollo", "bbox": [26,133,105,213], "parent": null },
        { "id": "DPC-EN-02", "text": "Producción", "bbox": [27,232,105,311], "parent": null }
      ] },
    { "name": "Bundles",
      "stickies": [
        { "id": "DPC-BU-01", "text": "Frontend: SPA (aplicación web con diseño responsivo)", "bbox": [251,79,375,150], "parent": null },
        { "id": "DPC-BU-02", "text": "Backend: monolito (Node.js)", "bbox": [423,86,537,151], "parent": null }
      ] },
    { "name": "Cloud abstractions", "stickies": [] }
  ],
  "empty_sections": []
}
```

Post-it text stays in its original language — that is the golden rule, not
an oversight. The full COM for this canvas is persisted at
`com/E1-deployment-p6.json`.
