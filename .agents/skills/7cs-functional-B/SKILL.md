---
name: 7cs-functional-B
description: Recibe páginas o imágenes separadas desde un PDF 7Cs, acepta únicamente el Functional Canvas Back y genera su COM literal con variant == "back". Ignora Functional Front y todos los demás canvas; no deriva FR ni escenarios.
---

# 7cs-functional-B - Lector Back

```yaml
inputs: {page_image: path, source_pdf: string, page: integer, delivery_id: string}
outputs:
  status: accepted | ignored | needs_clarification
  com_path: com/<delivery_id>-functional-back-p<page>.json | null
  clarifications: [string]
```

1. Aceptar sólo el título literal `Functional Canvas Back`.
2. Ignorar `Functional Canvas Front` y cualquier otro canvas sin producir COM.
3. Leer `references/com-schema.md` y copiar cabecera, secciones, post-its, `bbox` y relaciones literalmente.
4. Tratar `Bundles & components` como sección plana.
5. Persistir `canvas: "functional"`, `variant: "back"` e ids `FNC-BCK-<SECTION>-<NN>`.

No generar FR, entidades derivadas, escenarios, stack de plan ni códigos de bundle.

