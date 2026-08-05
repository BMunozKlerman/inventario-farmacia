---
name: 7cs-system-context
description: Recibe páginas o imágenes separadas desde un PDF 7Cs, acepta únicamente un System Context Canvas y genera su COM literal. Ignora cualquier página de otro tipo y no transforma el COM a Spec Kit.
---

# 7cs-system-context - Lector COM

```yaml
inputs: {page_image: path, source_pdf: string, page: integer, delivery_id: string}
outputs:
  status: accepted | ignored | needs_clarification
  com_path: com/<delivery_id>-system_context-p<page>.json | null
  clarifications: [string]
```

1. Aceptar sólo `System Context Canvas`; otros títulos se ignoran sin COM.
2. Leer `references/com-schema.md` y copiar literalmente las 16 secciones impresas, post-its, `bbox` y relaciones.
3. Registrar secciones presentes sin post-its como `stickies: []`.
4. No inferir direcciones, contrapartes, actores ni interfaces por proximidad.
5. Persistir `canvas: "system_context"` con ids `SCC-<SECTION>-<NN>`.

