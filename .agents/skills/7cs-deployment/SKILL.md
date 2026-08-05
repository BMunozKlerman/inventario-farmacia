---
name: 7cs-deployment
description: Recibe páginas o imágenes separadas desde un PDF 7Cs, acepta únicamente un Deployment Canvas y genera su COM literal de entornos, runtimes, topología y operación. Ignora otros canvas y no genera todavía plan ni NFR.
---

# 7cs-deployment - Lector COM

```yaml
inputs: {page_image: path, source_pdf: string, page: integer, delivery_id: string}
outputs:
  status: accepted | ignored | needs_clarification
  com_path: com/<delivery_id>-deployment-p<page>.json | null
  clarifications: [string]
```

1. Aceptar sólo `Deployment Canvas`; ignorar el resto.
2. Copiar literalmente entornos, nodos, runtimes, redes, instalación, operación, post-its y `bbox`.
3. Usar ids `DEP-<SECTION>-<NN>` y persistir `canvas: "deployment"`.
4. No derivar SLA, RPO, RTO, proveedor, NFR ni decisiones de plan.

