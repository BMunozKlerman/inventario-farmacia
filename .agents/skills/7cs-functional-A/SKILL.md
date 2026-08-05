---
name: 7cs-functional-A
description: Recibe páginas o imágenes separadas desde un PDF 7Cs, acepta únicamente el Functional Canvas Front y genera su COM literal con variant == "front". Ignora Functional Back y todos los demás canvas; no deriva FR ni escenarios.
---

# 7cs-functional-A - Lector Front

```yaml
inputs: {page_image: path, source_pdf: string, page: integer, delivery_id: string}
outputs:
  status: accepted | ignored | needs_clarification
  com_path: com/<delivery_id>-functional-front-p<page>.json | null
  clarifications: [string]
```

1. Aceptar sólo el título literal `Functional Canvas Front`.
2. Ignorar `Functional Canvas Back` y cualquier otro canvas sin producir COM.
3. Leer `references/com-schema.md` y copiar cabecera, secciones, post-its, `bbox` y relaciones literalmente.
4. Tratar `Bundles & components` como sección plana.
5. Persistir `canvas: "functional"`, `variant: "front"` e ids `FNC-FRT-<SECTION>-<NN>`.

No generar FR, entidades derivadas, escenarios, stack de plan ni códigos de bundle.

