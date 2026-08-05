# Canvas Object Model (COM) — esquema (referencia de consumo)

**Este archivo solo documenta la forma del COM que `7cs-functional-B`
consume como entrada.** El COM **no** lo produce este skill — lo produce
`7cs-functional-A` (Etapa A) leyendo el PDF/imagen del Functional Canvas
y persistiéndolo en `com/<delivery_id>-functional-p<n>.json`.

Por la regla de oro del pipeline (el COM no interpreta), la definición
canónica del COM vive en `7cs-functional-A/references/com-schema.md`.
Este archivo es un resumen de consulta rápida para que el mapeo pueda
verificar la forma de su entrada sin abrir el otro skill.

---

**Regla de oro (heredada de `7cs-functional-A`): el COM no interpreta.**
Copia texto literal y coordenadas. Toda interpretación ocurre en los
skills de mapeo (Etapa B), donde queda registrada y es auditable.

## Esquema

```json
{
  "source": "Ejemplo 1.pdf#p1",
  "canvas": "functional",
  "template": "7Cs v1.1 June 2026",
  "delivery_id": "E1",
  "header": {
    "system": null,
    "organization": null,
    "canvas_name": null,
    "version": null,
    "date": null
  },
  "sections": [
    {
      "name": "Data objects",
      "stickies": [
        {
          "id": "FNC-OB-01",
          "text": "Publicación (Paper)",
          "bbox": [52, 585, 183, 650],
          "parent": null
        }
      ]
    },
    {
      "name": "Bundles & components",
      "stickies": [
        {
          "id": "FNC-BC-01",
          "text": "Ingestor Worker (ETL)",
          "bbox": [430, 80, 690, 145],
          "parent": null
        }
      ]
    }
  ],
  "empty_sections": [],
  "notes": []
}
```

## Convenciones (resumen de consumo)

- **`canvas`** (vocabulario cerrado del pipeline): `"functional"` para
  este skill. Cualquier otra página (otro tipo de canvas, diagrama C4,
  nómina, hoja vacía) se marca `out_of_scope` en el índice y no produce
  COM. Esta validación la hace `7cs-functional-A` antes de escribir.
- **`id` de post-it**: `FNC-<sigla de sección>-<NN>` (p.ej. `FNC-OB-04`,
  `FNC-J01`). Las siglas siguen la tabla de 14 secciones del Functional
  Canvas (ver `7cs-functional-A/references/com-schema.md`). Los
  identificadores son estables entre corridas (idempotencia).
- **`bbox`**: `[x1, y1, x2, y2]` en píxeles de la imagen original. Es la
  evidencia citable: un auditor puede recortar la imagen y verificar la
  cita literal.
- **`parent`**: en el Functional Canvas suele ser `null`. El recuadro
  "Bundles & components" **no** se modela como grouper jerárquico — es
  una sección más con sus post-it. Si en una variante futura aparece un
  rectángulo con borde y rótulo suelto encerrando post-it, registrará su
  id en `parent` como en los otros canvas.
- **`empty_sections`**: nombres de las 14 secciones esperadas que no
  aparecen físicamente en el canvas. El vacío es evidencia, no omisión
  silenciosa. Las secciones presentes pero sin post-it van en
  `sections[]` con `stickies: []`.
- **`header`**: campos literales de la cabecera. `null` cuando están
  vacíos — la cabecera vacía también es un dato y genera una duda de
  identificación del artefacto.
- El texto del post-it se copia **literal**, incluidos errores
  ortográficos. El tamaño de fuente varía entre post-it; **nunca**
  inferir importancia del tamaño.
