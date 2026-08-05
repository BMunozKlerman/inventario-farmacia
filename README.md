# inventario-farmacia

Pipeline 7Cs para convertir un PDF de canvas en un entregable trazable.

## Flujo correcto

1. El PDF inmutable se coloca en `resources/`.
2. `7cs-canvas-ingest` separa páginas o canvas, crea imágenes en `evidence/` y un índice de enrutamiento. No genera COM.
3. Cada candidato se entrega a todos los lectores. Cada skill acepta únicamente su canvas, ignora los demás y produce un COM literal en `com/`.
4. `7cs-com-transform` consume sólo los COM y genera fragmentos, contexto de plan, trazas y dudas en `mapping/`.
5. `7cs-spec-compose` construye las entradas de Spec Kit y el entregable.
6. `7cs-spec-audit` recontabiliza desde los COM y bloquea resultados incompletos.

## Lectores

- `7cs-business-context`
- `7cs-architectural-context`
- `7cs-system-context`
- `7cs-structural`
- `7cs-functional-A`: exclusivamente Functional Front.
- `7cs-functional-B`: exclusivamente Functional Back.
- `7cs-deployment`

El COM copia texto literal, secciones, coordenadas y relaciones. No contiene requisitos derivados. Una página ajena devuelve `ignored` y no crea archivo.

## Validación local

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ./scripts/test-one-postit-budget.ps1
```

El mismo presupuesto de un post-it se ejecuta en GitHub Actions.

## Ejecutar PDF completo con Codex

El proyecto usa Codex CLI autenticado con la cuenta ChatGPT actual. No usa
OpenAI API ni requiere `OPENAI_API_KEY`. El PDF debe existir en `resources/`.

Primero inicia sesión (una sola vez por equipo o cuando expire la sesión):

```powershell
codex login
codex login status
```

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ./scripts/run-pipeline.ps1 `
  -PdfPath "./resources/[TDS DIS 2026] Equipo 2.pdf" `
  -DeliveryId E1
```

Para probar sólo PDF -> siete COM presupuestados:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ./scripts/run-pipeline.ps1 `
  -PdfPath "./resources/[TDS DIS 2026] Equipo 2.pdf" -DeliveryId E1 -ComOnly
```

El PDF se renderiza localmente y las imágenes se entregan al Codex CLI. Los COM
quedan en `com/`; el resto del flujo queda en `mapping/`, `composed/` y `audit/`.
El procesamiento usa la cuota incluida de Codex según el plan y sus límites;
no es inferencia offline y el contenido visual se procesa mediante OpenAI.

