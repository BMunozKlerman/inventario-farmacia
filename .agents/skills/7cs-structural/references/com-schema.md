# COM Schema — Structural Canvas

Full JSON shape for the Canvas Object Model produced by `7cs-structural`. Read this before assembling or validating a COM, or whenever a field's shape is unclear.

## Top-level fields

| Field | Type | Notes |
|---|---|---|
| `source` | string | `"<filename>#p<n>"` |
| `canvas` | string | constant: `"structural"` |
| `template` | string \| null | version read from the footer, e.g. `"7Cs v1.1 June 2026"`; `null` if illegible |
| `delivery_id` | string | from input, or derived from the filename if omitted |
| `header` | object | `system`, `organization`, `canvas`, `version`, `date` — each `string \| null` |
| `sections` | array | one entry per section physically present; see below |
| `empty_sections` | array of strings | names of the expected sections that are physically absent from the image |
| `notes` | array of strings | observations regarding canvas rendering, location of titles, or missing fields |

## `sections[]` entry

```json
{ "name": "<section name as printed>", "stickies": [ <sticky>, ... ] }
```

## `sticky` object

| Field | Type | Notes |
|---|---|---|
| `id` | string | `STR<section-code>-<running number>`, e.g. `"STR-FB-01"` |
| `text` | string | literal, unedited — same language, same spelling as printed |
| `bbox` | `[x0, y0, x1, y1]` | best-effort pixel / reading-order estimate; not guaranteed exact unless a vector-aware parser is available |
| `parent` | string \| null | `id` of the enclosing grouper sticky, if any |

## Section code prefixes

| Prefix | Section |
|---|---|
| `FB` | Frontend bundles |
| `IFIN` | Data input interfaces to frontend bundles |
| `IFOUT` | Data output interfaces from frontend bundles |
| `BB` | Backend bundles |
| `IBIN` | Data input interfaces to backend bundles |
| `IBOUT` | Data output interfaces from backend bundles |
| `RB` | Repository bundles |
| `IRIN` | Data input interfaces to repository bundles |
| `IROUT` | Data output interfaces from repository bundles |
| `PB` | Platform & Infrastructure bundles |
| `IPIN` | Data input interfaces to platform & infrastructure bundles |
| `IPOUT` | Data output interfaces from platform & infrastructure bundles |
| `DB` | Device bundles |
| `IDIN` | Data input interfaces to device bundles |
| `IDOUT` | Data output interfaces from device bundles |
| `C` | Constraints |

## Worked example (partial, from a real canvas)

```json
{
  "source": "[TDS DIS 2026] Equipo 2.pdf#p4",
  "canvas": "structural",
  "template": "7Cs v1.1 June 2026",
  "delivery_id": "farmacia-canvas",
  "header": { "system": null, "organization": null, "canvas": null, "version": null, "date": null },
  "sections": [
    {
      "name": "Frontend bundles",
      "stickies": [
        { "id": "STR-FB-01", "text": "Single Page Application (SPA) web con diseño responsivo", "bbox": [70.0, 130.0, 770.0, 200.0], "parent": null }
      ]
    }
  ],
  "empty_sections": [
    "Data output interfaces to frontend bundles",
    "Data input interfaces to backend bundles",
    "Data output interfaces to backend bundles"
  ],
  "notes": [
    "Header fields System, Organization, Version and Date are not printed on this canvas page; recorded as null."
  ]
}
```