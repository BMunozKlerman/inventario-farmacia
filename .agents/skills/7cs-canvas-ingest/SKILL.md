---
name: 7cs-canvas-ingest
description: Recibe el PDF 7Cs ubicado en resources, lo renderiza y separa en páginas o regiones de canvas, crea evidencia e índice de enrutamiento y entrega cada candidato a todas las skills lectoras. No transcribe post-its ni genera COM por sí mismo.
---

# 7cs-canvas-ingest - Separación y enrutamiento

Leer `references/pipeline-contract.md` antes de procesar.

```yaml
inputs:
  pdf_path: resources/<archivo>.pdf
  delivery_id: string
outputs:
  page_index: evidence/<delivery_id>-page-index.json
  ingest_report: evidence/<delivery_id>-ingest-report.md
  candidates: [page_image]
```

## Procedimiento

1. Rechazar rutas fuera de `resources/`; calcular SHA-256 y no modificar el PDF.
2. Renderizar todas las páginas como `evidence/<delivery_id>-pNN.png`. Si una página contiene varios canvas independientes, crear un recorte por canvas y conservar página y `bbox` de origen.
3. Registrar cada candidato en el índice con fuente, página, recorte, título visible y evidencia.
4. Entregar cada candidato a todos los lectores: Business, Architectural, System, Structural, Functional A, Functional B y Deployment.
5. Cada lector decide `accepted`, `ignored` o `needs_clarification`; el separador no decide por él.
6. Verificar que exactamente un lector acepte cada canvas. Cero o más de uno produce una duda bloqueante.
7. Registrar los `com_path` devueltos por los lectores, sin abrir ni reinterpretar sus COM.

## Acceptance

- Cada página del PDF tiene evidencia e índice.
- Cada canvas tiene exactamente un lector propietario.
- Páginas administrativas o diagramas ajenos quedan `out_of_scope` sin COM.
- El separador nunca produce contenido COM ni requisitos.

