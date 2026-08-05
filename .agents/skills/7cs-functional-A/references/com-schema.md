# COM Functional Front

`7cs-functional-A` acepta únicamente `Functional Canvas Front` y produce este COM. No aplica reglas de mapeo.

```json
{
  "source": "resources/delivery.pdf#p5",
  "canvas": "functional",
  "variant": "front",
  "delivery_id": "E1",
  "header": {"system": null, "organization": null, "canvas": "Functional Canvas Front", "version": null, "date": null},
  "sections": [
    {"name": "User inputs", "stickies": [
      {"id": "FNC-FRT-UI-01", "text": "texto literal", "bbox": [0, 0, 1, 1], "parent": null}
    ]}
  ],
  "empty_sections": [],
  "notes": []
}
```

## Reglas

- `variant` siempre es `front`.
- Id: `FNC-FRT-<section-code>-<NN>`.
- Una sección visible sin post-its permanece en `sections` con `stickies: []`.
- `empty_sections` contiene sólo secciones físicamente ausentes.
- El texto se copia sin corrección, traducción o interpretación.
- `Bundles & components` es una sección plana, no un grouper.
- La transformación posterior corresponde a `7cs-com-transform`.

