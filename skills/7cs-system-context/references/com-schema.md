# COM Schema — System Context Canvas

Full JSON shape for the Canvas Object Model produced by
`7cs-system-context`. Read this before assembling or validating a COM, or
whenever a field's shape is unclear.

## Top-level fields

| Field | Type | Notes |
|---|---|---|
| `source` | string | `"<filename>#p<n>"` |
| `canvas` | string | constant: `"system_context"` |
| `template` | string \| null | version read from the footer, e.g. `"7Cs v1.1 June 2026"`; `null` if illegible |
| `delivery_id` | string | from input, or derived from the filename if omitted |
| `header` | object | `system`, `organization`, `canvas`, `version`, `date` — each `string \| null` |
| `sections` | array | one entry per section printed on the 4×4 grid (16 total; present-but-empty ones included with `stickies: []`) |
| `empty_sections` | array of strings | names of the 16 expected sections whose box is physically absent from the printed grid itself (not merely empty of stickies) |

## `sections[]` entry

```json
{ "name": "<section name as printed>", "stickies": [ <sticky>, ... ] }
```

## `sticky` object

| Field | Type | Notes |
|---|---|---|
| `id` | string | `SCC-<section-code>-<running number>`, e.g. `"SCC-SU-01"` |
| `text` | string | literal, unedited — same language, same spelling as printed |
| `bbox` | `[x0, y0, x1, y1]` | best-effort pixel / reading-order estimate; not guaranteed exact unless a vector-aware parser is available |
| `parent` | string \| null | `id` of the enclosing grouper sticky, if any |

## Section code prefixes

The canvas-level prefix is `SCC` (System Context Canvas). Each section
also has a short code used in sticky ids as `SCC-<code>-<n>`.

| Code | Section |
|---|---|
| `SU` | Source users |
| `UDI` | User data input interfaces |
| `UDO` | User data output interfaces |
| `TU` | Target users |
| `SS` | Source systems |
| `SDI` | System data input interfaces |
| `SDO` | System data output interfaces |
| `TS` | Target systems |
| `SR` | Source repositories |
| `RDI` | Repository data input interfaces |
| `RDO` | Repository data output interfaces |
| `TR` | Target repositories |
| `SD` | Source devices |
| `DDI` | Device data input interfaces |
| `DDO` | Device data output interfaces |
| `TD` | Target devices |

## Worked example (partial, from a real canvas)

```json
{
  "source": "system-context.pdf#p1",
  "canvas": "system_context",
  "template": "7Cs v1.1 June 2026",
  "delivery_id": "E1",
  "header": { "system": null, "organization": null, "canvas": null, "version": null, "date": null },
  "sections": [
    { "name": "Source users",
      "stickies": [
        { "id": "SCC-SU-01", "text": "QF DT", "bbox": [30,155,85,210], "parent": null },
        { "id": "SCC-SU-02", "text": "QF Complementario", "bbox": [100,155,220,205], "parent": null }
      ] },
    { "name": "Source repositories", "stickies": [] }
  ],
  "empty_sections": []
}
```
