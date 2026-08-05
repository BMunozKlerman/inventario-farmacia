# COM Schema — Functional Canvas

Full JSON shape for the Canvas Object Model produced by
`7cs-functional-A`. Read this before assembling or validating a COM, or
whenever a field's shape is unclear. The COM is the only input that
`7cs-functional-B` consumes — it never goes back to the PDF.

## Top-level fields

| Field | Type | Notes |
|---|---|---|
| `source` | string | `"<filename>#p<n>"` |
| `canvas` | string | constant: `"functional"` (closed vocabulary) |
| `template` | string \| null | version read from the footer, e.g. `"7Cs v1.1 June 2026"`; `null` if illegible |
| `delivery_id` | string | from input, or derived from the filename if omitted |
| `header` | object | `system`, `organization`, `canvas`, `version`, `date` — each `string \| null` |
| `sections` | array | one entry per section physically present; see below |
| `empty_sections` | array of strings | names of the 14 expected sections whose box is physically absent from the printed canvas |
| `notes` | array of strings | free-form provenance clarifications (e.g. header fields left blank) |

## `sections[]` entry

```json
{ "name": "<section name as printed>", "stickies": [ <sticky>, ... ] }
```

A section present on the printed canvas but containing no post-its is
recorded with `stickies: []`. It is **not** moved to `empty_sections`
— that field is reserved for sections whose rectangle is physically
absent from the page.

## `sticky` object

| Field | Type | Notes |
|---|---|---|
| `id` | string | `FNC-<section-code>-<running number>`, e.g. `"FNC-OB-01"` |
| `text` | string | literal, unedited — same language, same spelling as printed |
| `bbox` | `[x0, y0, x1, y1]` | best-effort pixel / reading-order estimate; not guaranteed exact unless a vector-aware parser is available |
| `parent` | string \| null | id of the enclosing grouper sticky, if any — usually `null` in this canvas, since the "Bundles & components" frame is not a grouper |

## Section code prefixes

The canvas-level prefix is `FNC` (Functional Canvas). Each section also
has a short code used in sticky ids as `FNC-<code>-<n>`. The fourteen
sections are the vocabulary of the Functional Canvas (7Cs v1.1, June
2026).

| Code | Section |
|---|---|
| `BC` | Bundles & components |
| `OB` | Data objects |
| `UI` | User inputs |
| `UPI` | UI-processing inputs |
| `API` | API inputs |
| `DI` | Data imports |
| `DE` | Data exports |
| `J` | Jobs |
| `EH` | Event handlers |
| `ET` | Event triggers |
| `H` | Helpers |
| `UV` | User visualizations / reports |
| `TS` | Technology stack |
| `CT` | Constraints |

## Worked example (illustrative, from a synthetic canvas)

The snippet below mirrors the shape used by `7cs-functional-B` in its
`references/ejemplo-trabajado-etl.md`. It is **not** drawn from a real
canvas ingested into this repository — no Functional Canvas has been
ingested here yet.

```json
{
  "source": "Ejemplo 1.pdf#p7",
  "canvas": "functional",
  "template": "7Cs v1.1 June 2026",
  "delivery_id": "E1",
  "header": {
    "system": null,
    "organization": null,
    "canvas": null,
    "version": null,
    "date": null
  },
  "sections": [
    {
      "name": "Bundles & components",
      "stickies": [
        { "id": "FNC-BC-01", "text": "Ingestor Worker (ETL)", "bbox": [52, 80, 250, 145], "parent": null }
      ]
    },
    {
      "name": "Data objects",
      "stickies": [
        { "id": "FNC-OB-01", "text": "Publicación (Paper)", "bbox": [52, 200, 250, 260], "parent": null },
        { "id": "FNC-OB-02", "text": "Documento de publicación", "bbox": [270, 200, 460, 260], "parent": null }
      ]
    },
    {
      "name": "Jobs",
      "stickies": [
        { "id": "FNC-J-01", "text": "Ejecucion de ingesta programada", "bbox": [52, 320, 320, 380], "parent": null }
      ]
    },
    {
      "name": "User inputs",
      "stickies": []
    },
    {
      "name": "UI-processing inputs",
      "stickies": []
    },
    {
      "name": "User visualizations / reports",
      "stickies": []
    }
  ],
  "empty_sections": [
    "API inputs",
    "Data imports",
    "Data exports",
    "Event handlers",
    "Event triggers",
    "Helpers",
    "Technology stack",
    "Constraints"
  ],
  "notes": []
}
```

In the example above, the first three sections after `Bundles &
components` (`User inputs`, `UI-processing inputs`, `User visualizations
/ reports`) are present on the printed canvas but contain no post-its;
they remain in `sections[]` with `stickies: []`. The last eight
sections are physically absent from the page and go into
`empty_sections`. `7cs-functional-B` will read `empty_sections` to
classify each absence as `coherente` or `inconsistencia`.