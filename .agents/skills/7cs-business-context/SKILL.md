---
name: 7cs-business-context
description: Recibe páginas o imágenes separadas desde un PDF 7Cs, acepta únicamente un Business Context Canvas y genera su COM literal. Ignora cualquier página de otro tipo y no transforma el COM a requisitos.
---

# 7cs-business-context - Lector COM

```yaml
inputs: {page_image: path, source_pdf: string, page: integer, delivery_id: string}
outputs:
  status: accepted | ignored | needs_clarification
  com_path: com/<delivery_id>-business_context-p<page>.json | null
  clarifications: [string]
```

1. Aceptar sólo `Business Context Canvas`; devolver `ignored` para cualquier otro título.
2. Copiar cabecera, propósito, actores, perfiles, objetos, áreas/secciones, post-its, `bbox` y groupers literalmente.
3. No convertir metas en métricas, actores en permisos ni objetos en esquemas.
4. Usar ids `BUS-<SECTION>-<NN>` y persistir `canvas: "business_context"`.

