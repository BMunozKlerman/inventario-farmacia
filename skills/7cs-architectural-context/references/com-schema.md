# COM Schema — Architectural Context Canvas

Full JSON shape for the Canvas Object Model produced by
`7cs-architectural-context`. Read this before assembling or validating a
COM, or whenever a field's shape is unclear.

## Top-level fields

| Field | Type | Notes |
|---|---|---|
| `source` | string | `"<filename>#p<n>"` |
| `canvas` | string | constant: `"architectural_context"` |
| `template` | string \| null | version read from the footer, e.g. `"7Cs v1.1 June 2026"`; `null` if illegible |
| `delivery_id` | string | from input, or derived from the filename if omitted |
| `header` | object | `system`, `organization`, `canvas`, `version`, `date` — each `string \| null` |
| `sections` | array | one entry per section physically present; see below |
| `empty_sections` | array of strings | names of the 10 expected sections that are physically absent from the image |

## `sections[]` entry

```json
{ "name": "<section name as printed>", "stickies": [ <sticky>, ... ] }
```

## `sticky` object

| Field | Type | Notes |
|---|---|---|
| `id` | string | `<section-code>-<running number>`, e.g. `"ACC-ST-01"` |
| `text` | string | literal, unedited — same language, same spelling as printed |
| `bbox` | `[x0, y0, x1, y1]` | best-effort pixel / reading-order estimate; not guaranteed exact unless a vector-aware parser is available |
| `parent` | string \| null | `id` of the enclosing grouper sticky, if any |

## Section code prefixes

| Prefix | Section |
|---|---|
| `ST` | Stakeholders |
| `BS` | Business strategy |
| `IT` | IT strategy |
| `BG` | Business goals & drivers |
| `TG` | Technology goals & drivers |
| `BP` | Business standards & policies |
| `TP` | Technology standards & policies |
| `SC` | Situational constraints |
| `BPR` | Business principles |
| `TPR` | Technical principles |

## Worked example (partial, from a real canvas)

```json
{
  "source": "farmacia-canvas.png#p1",
  "canvas": "architectural_context",
  "template": "7Cs v1.1 June 2026",
  "delivery_id": "farmacia-canvas",
  "header": { "system": null, "organization": null, "canvas": null, "version": null, "date": null },
  "sections": [
    { "name": "Stakeholders",
      "stickies": [
        { "id": "ACC-ST-01", "text": "QF DT", "bbox": [48,128,103,172], "parent": null },
        { "id": "ACC-ST-07", "text": "ISP", "bbox": [472,132,522,172], "parent": null }
      ] },
    { "name": "Business goals & drivers",
      "stickies": [
        { "id": "ACC-BG-01", "text": "Reducción de pérdidas económicas por merma", "bbox": [48,368,132,412], "parent": null },
        { "id": "ACC-BG-03", "text": "Eficiencia operativa", "bbox": [248,372,310,408], "parent": null }
      ] }
  ],
  "empty_sections": []
}
```
