---
name: 7cs-structural
description: Recibe páginas o imágenes separadas desde un PDF 7Cs, acepta únicamente un Structural Canvas y genera su COM literal de capas, bundles, componentes e interfaces. Ignora otros canvas y no genera todavía el censo derivado.
---

# 7cs-structural - Lector COM

```yaml
inputs: {page_image: path, source_pdf: string, page: integer, delivery_id: string}
outputs:
  status: accepted | ignored | needs_clarification
  com_path: com/<delivery_id>-structural-p<page>.json | null
  clarifications: [string]
```

1. Aceptar sólo `Structural Canvas`; ignorar el resto.
2. Copiar literalmente capas, bundles, componentes, interfaces, groupers, relaciones y `bbox`.
3. Usar ids `STR-<SECTION>-<NN>`; no inventar códigos de bundle ni vínculos Functional.
4. Persistir `canvas: "structural"`.

El censo canónico de bundles se deriva posteriormente desde este COM, nunca durante lectura.

