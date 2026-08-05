# inventario-farmacia

Pipeline 7Cs para convertir un PDF de canvas en COM literales y un entregable trazable.

## Flujo

1. Colocar el PDF en `resources/`.
2. `7cs-canvas-ingest` renderiza, separa y enruta los canvas; no genera COM.
3. Cada skill lectora acepta solamente su canvas y genera un COM literal en `com/`.
4. `7cs-com-transform` genera fragmentos, contexto de plan, trazas y dudas en `mapping/`.
5. `7cs-spec-compose` construye el entregable en `composed/`.
6. `7cs-spec-audit` verifica cobertura, identificadores y falsabilidad en `audit/`.

Los lectores son Business Context, Architectural Context, System Context, Structural, Functional Front, Functional Back y Deployment. El COM conserva texto literal, secciones, coordenadas y relaciones; no contiene requisitos derivados.

## Requisitos

- Windows PowerShell.
- Extensión oficial de OpenAI para VS Code, que incluye Codex CLI.
- Sesión de Codex iniciada con una cuenta ChatGPT.
- Un PDF 7Cs dentro de `resources/`.

Para iniciar sesión cuando `codex` no esté disponible directamente en PowerShell:

```powershell
$codexExe = Get-ChildItem "$env:USERPROFILE/.vscode/extensions/openai.chatgpt-*-win32-x64/bin/windows-x86_64/codex.exe" |
  Sort-Object FullName -Descending |
  Select-Object -First 1 -ExpandProperty FullName

& $codexExe login
& $codexExe login status
```

## Ejecutar el proyecto

Abrir PowerShell en la raíz del repositorio:

```powershell
cd "C:\Users\kahos\Desktop\inventario-farmacia"
```

Cuando exista un solo PDF en `resources/`, ejecutar el pipeline completo con:

```powershell
.\run-project.cmd
```

El lanzador detecta el PDF automáticamente y usa `E1` como identificador.

Para generar y validar solamente los siete COM:

```powershell
.\run-project.cmd -ComOnly
```

Para usar otro identificador:

```powershell
.\run-project.cmd -DeliveryId "PROYECTO2"
```

Cuando haya más de un PDF en `resources/`, indicar cuál procesar:

```powershell
.\run-project.cmd -PdfPath ".\resources\otro.pdf" -DeliveryId "PROYECTO2"
```

Usar un `DeliveryId` diferente para conservar resultados de ejecuciones anteriores.

## Resultados

- `evidence/`: imágenes, índice e informe de ingesta.
- `com/`: siete COM literales en JSON.
- `mapping/`: fragmentos, contexto de plan, trazas y aclaraciones.
- `composed/`: especificación, plan y trazabilidad compuestos.
- `audit/`: informe y resumen de auditoría.

Una ejecución completa termina con:

```text
[5/5] Pipeline completo: PASS
```

## Validación local

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\test-one-postit-budget.ps1
```

El proyecto no utiliza `OPENAI_API_KEY`. Codex usa la cuota incluida en el plan de ChatGPT y sus límites. El renderizado ocurre localmente, pero las imágenes se procesan mediante OpenAI; no es inferencia offline.
