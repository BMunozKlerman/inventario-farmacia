# COM Functional Back

`7cs-functional-B` acepta únicamente `Functional Canvas Back` y produce este COM. No aplica reglas de mapeo.

```json
{
  "source": "resources/delivery.pdf#p7",
  "canvas": "functional",
  "variant": "back",
  "delivery_id": "E1",
  "header": {"system": null, "organization": null, "canvas": "Functional Canvas Back", "version": null, "date": null},
  "sections": [
    {"name": "Data objects", "stickies": [
      {"id": "FNC-BCK-OB-01", "text": "texto literal", "bbox": [0, 0, 1, 1], "parent": null}
    ]}
  ],
  "empty_sections": [],
  "notes": []
}
```

## Reglas

- `variant` siempre es `back`.
- Id: `FNC-BCK-<section-code>-<NN>`.
- Una sección visible sin post-its permanece en `sections` con `stickies: []`.
- `empty_sections` contiene sólo secciones físicamente ausentes.
- El texto se copia sin corrección, traducción o interpretación.
- `Bundles & components` es una sección plana, no un grouper.
- La transformación posterior corresponde a `7cs-com-transform`.

