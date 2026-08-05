# Canvas Object Model (COM) — esquema

El COM es el modelo intermedio entre el PDF y los skills de mapeo. Es la **única entrada**
que reciben los skills de mapeo: ningún skill vuelve a mirar el PDF.

**Regla de oro: el COM no interpreta.** Copia texto literal y coordenadas. Toda
interpretación ocurre en los skills de mapeo, donde queda registrada y es auditable.

## Esquema

```json
{
  "source": "Ejemplo 1.pdf#p1",
  "canvas": "business_context",
  "template": "7Cs v1.1 June 2026",
  "header": {
    "system": null,
    "organization": null,
    "canvas_name": null,
    "version": null,
    "date": null
  },
  "sections": [
    {
      "name": "Business objects",
      "stickies": [
        {
          "id": "E1-BO-01",
          "text": "Noticias y Eventos",
          "bbox": [52, 585, 183, 650],
          "parent": null
        },
        {
          "id": "E1-BO-06",
          "text": "Publicaciones científicas (Papers)",
          "bbox": [214, 700, 346, 765],
          "parent": null
        }
      ]
    },
    {
      "name": "Business units & actors",
      "groupers": [
        { "id": "E1-BUA-G1", "label": "Público general", "bbox": [430, 200, 690, 265] }
      ],
      "stickies": [
        { "id": "E1-BUA-06", "text": "Futuros estudiantes", "bbox": [440, 215, 515, 258], "parent": "E1-BUA-G1" }
      ]
    }
  ],
  "empty_sections": [],
  "notes": []
}
```

## Convenciones

- **`canvas`** ∈ vocabulario cerrado: `business_context`, `architectural_context`,
  `system_context`, `structural`, `functional`, `deployment`. Cualquier otra página
  (nómina, diagrama C4, hoja vacía) se marca `out_of_scope` en el índice y no produce COM.
- **`id` de post-it**: `{delivery}-{sigla de sección}-{nn}` (p.ej. `E1-SFA-04`).
  Los identificadores son estables entre corridas (idempotencia).
- **`bbox`**: `[x1, y1, x2, y2]` en píxeles de la imagen original. Es la evidencia citable:
  un auditor puede recortar la imagen y verificar la cita literal.
- **`parent`**: id del agrupador que contiene el post-it. Un rectángulo con borde que
  encierra post-it y tiene rótulo suelto ("Público general") se registra como agrupador
  y sus post-it lo referencian. Esta jerarquía se pierde si solo se leen los textos:
  registrarla es obligatorio.
- **`empty_sections`**: nombres de secciones del vocabulario que existen en la plantilla
  pero no tienen post-it. El vacío es evidencia, no omisión silenciosa.
- **`header`**: campos literales de la cabecera. `null` cuando están vacíos — la cabecera
  vacía también es un dato y genera una duda de identificación del artefacto.
- El texto del post-it se copia **literal**, incluidos errores ortográficos. El tamaño de
  fuente varía entre post-it; **nunca** inferir importancia del tamaño.
