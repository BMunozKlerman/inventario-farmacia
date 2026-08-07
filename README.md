# inventario-farmacia

Pipeline 7Cs para convertir un PDF de canvas en COM literales y un entregable trazable.

Funciona en macOS, Linux y Windows, y con cualquier CLI de agente de IA compatible
(Codex, Claude Code, Gemini u otro declarado por configuración).

## Flujo

1. Colocar el PDF en `resources/`.
2. `7cs-canvas-ingest` renderiza, separa y enruta los canvas; no genera COM.
3. Cada skill lectora acepta solamente su canvas y genera un COM literal en `com/`.
4. `7cs-com-transform` genera fragmentos, contexto de plan, trazas y dudas en `mapping/`.
5. `7cs-spec-compose` construye el entregable en `composed/`.
6. `7cs-spec-audit` verifica cobertura, identificadores y falsabilidad en `audit/`.
7. `7cs-backend-slice` genera código fuente ejecutable para exactamente un post-it Functional Back en `implementation/`.

Si una etapa necesita una aclaración, el pipeline se pausa en la consola, muestra la pregunta y
espera una respuesta. El agente vuelve a analizar la etapa: si la respuesta es suficiente continúa;
si no, formula nuevamente la aclaración. La composición y la auditoría no se ejecutan mientras
exista una pregunta abierta.

Los lectores son Business Context, Architectural Context, System Context, Structural,
Functional Front, Functional Back y Deployment. El COM conserva texto literal, secciones,
coordenadas y relaciones; no contiene requisitos derivados.

## Requisitos

- **Python 3.9 o superior** (sólo librería estándar; sin dependencias que instalar).
- **Poppler** (`pdftoppm`) disponible en el `PATH`:

  | Sistema | Instalación |
  |---|---|
  | macOS | `brew install poppler` |
  | Debian/Ubuntu | `sudo apt install poppler-utils` |
  | Fedora | `sudo dnf install poppler-utils` |
  | Windows | `choco install poppler` o `scoop install poppler` |

- **Un CLI de agente de IA** en el `PATH`, con su sesión ya iniciada. Ver la sección siguiente.
- Un PDF 7Cs dentro de `resources/`.

## Elegir el agente de IA

El pipeline no depende de un proveedor concreto. Los perfiles están declarados en
`config/agents.json` y se resuelven así:

1. Si `SEVENCS_AGENT` está definida, se usa ese perfil.
2. Si no, se recorre `detection_order` y se toma el primer ejecutable presente en el `PATH`.

```bash
SEVENCS_AGENT=claude python3 scripts/run_project.py
```

Para usar un binario que no esté en el `PATH` o una variante propia:

```bash
SEVENCS_AGENT_COMMAND=/ruta/a/mi-agente python3 scripts/run_project.py
```

Para agregar un agente nuevo, añade una entrada a `config/agents.json`:

```json
"mi-agente": {
  "command": "mi-agente",
  "exec_args": ["--no-interactive", "--workdir", "{root}"],
  "prompt_mode": "stdin",
  "image_mode": "prompt_paths"
}
```

- `exec_args`: argumentos fijos; `{root}` se sustituye por la raíz del repositorio.
- `prompt_mode`: `stdin` envía el prompt por entrada estándar; `arg` lo pasa como último argumento.
- `image_mode`: `flag` repite `image_arg` (con `{image}`) por cada imagen; `prompt_paths` anexa las
  rutas al final del prompt para que el agente las lea desde el workspace.
- `login_check` (opcional): subcomando que debe devolver 0 si hay sesión activa.

Los perfiles autodetectados son **interactivos**: el agente pedirá aprobación antes de ejecutar
comandos, así que el pipeline debe correrse desde una terminal real. Para una corrida desatendida
(CI, por ejemplo) existe el perfil opt-in `claude-unattended`, que preaprueba únicamente las
herramientas que el pipeline necesita. Nunca se autodetecta; hay que pedirlo explícitamente:

```bash
SEVENCS_AGENT=claude-unattended python3 scripts/run_project.py
```

Las skills viven en `.agents/skills/` y el pipeline **las inyecta literalmente en el prompt** de cada
etapa. No dependen del mecanismo de descubrimiento de skills de ningún agente (`.agents/`, `.claude/`,
etc.), así que basta con que el CLI elegido acepte un prompt y pueda escribir en el workspace.

La autenticación, la cuota y los límites dependen del agente elegido. El proyecto no gestiona
credenciales ni usa `OPENAI_API_KEY`. El renderizado del PDF ocurre localmente, pero las imágenes se
procesan mediante el agente; no es inferencia offline.

## Ejecutar el proyecto

Desde la raíz del repositorio, con un solo PDF en `resources/`:

```bash
python3 scripts/run_project.py
```

En Windows, usar `python` en lugar de `python3`. También hay lanzadores de conveniencia:
`./run-project.sh` (macOS/Linux) y `run-project.bat` (Windows).

El lanzador detecta el PDF automáticamente y usa `E1` como identificador.

Para generar y validar solamente los siete COM:

```bash
python3 scripts/run_project.py --com-only
```

Para usar otro identificador:

```bash
python3 scripts/run_project.py --delivery-id PROYECTO2
```

Cuando haya más de un PDF en `resources/`, indicar cuál procesar:

```bash
python3 scripts/run_project.py --pdf-path resources/otro.pdf --delivery-id PROYECTO2
```

Usar un `--delivery-id` diferente para conservar resultados de ejecuciones anteriores.

## Resultados

- `evidence/`: imágenes, índice e informe de ingesta.
- `com/`: siete COM literales en JSON.
- `mapping/`: fragmentos, contexto de plan, trazas y aclaraciones.
- `composed/`: especificación, plan y trazabilidad compuestos.
- `audit/`: informe y resumen de auditoría.
- `clarifications/`: preguntas, estado y respuestas proporcionadas durante la ejecución.
- `implementation/`: bundle backend mínimo, pruebas, Dockerfile y trazabilidad de un post-it.

Una ejecución completa termina con:

```text
Pipeline completo: PASS
```

El bundle generado incluye sus propios lanzadores. Por ejemplo:

```bash
cd implementation/E1/backend-stock-query && ./run.sh
```

## Validación local

```bash
python3 -m unittest discover -s tests
```

Exigir cobertura de trazas igual a 1,00 y que la prueba de falsabilidad rechace la eliminación de
una traza. La suite corre sin agente de IA ni Poppler instalados y no accede a la red.
