---
name: 7cs-architectural-context
description: Recibe páginas o imágenes separadas desde un PDF 7Cs, acepta únicamente un Architectural Context Canvas y genera su COM literal. Ignora cualquier página de otro tipo y no transforma el COM a Spec Kit.
---

# 7cs-architectural-context - Lector COM

Analizar sólo candidatos separados por `7cs-canvas-ingest`. Leer `references/com-schema.md` antes de emitir.

```yaml
inputs: {page_image: path, source_pdf: string, page: integer, delivery_id: string}
outputs:
  status: accepted | ignored | needs_clarification
  com_path: com/<delivery_id>-architectural_context-p<page>.json | null
  clarifications: [string]
```

1. Aceptar sólo el título `Architectural Context Canvas`.
2. Para otro canvas devolver `ignored`, sin COM ni interpretación.
3. Copiar literalmente cabecera, secciones, post-its, `bbox`, groupers y relaciones.
4. Mantener secciones presentes vacías con `stickies: []`; usar `empty_sections` sólo si faltan físicamente.
5. Persistir `canvas: "architectural_context"`.

No aplicar reglas de reescritura, corregir ortografía, completar métricas ni inferir texto. Cada post-it aceptado tiene id `ACC-<SECTION>-<NN>`, texto, sección, `bbox` y `parent`.

