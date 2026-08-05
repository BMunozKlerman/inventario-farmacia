# Ejemplo trabajado — Ejemplo 1, bundle "Ingestor Worker" (ETL)

Caso completo: la entrega `DIS 2026_AS_Ejemplo 1.pdf` declara **8 bundles** en el
Structural Canvas, de los cuales **3** tienen Functional Canvas. Uno de ellos es el
`Ingestor Worker` (prefijo `ETL`), descrito en la página 7 del PDF.

## Censo del Structural (extracto)

```yaml
- { code: "ETL",     name: "Ingestor Worker",              functional_canvas_page: 7 }
- { code: "INT",     name: "Integración consumidor de APIs", functional_canvas_page: 7 }
- { code: "CMS",     name: "CMS Gestor API",                functional_canvas_page: 7 }
- { code: "WEB-PUB", name: "Portal Web Público UI",         functional_canvas_page: null }  # sin canvas
- { code: "WEB-CMS", name: "CMS Web Backoffice UI",         functional_canvas_page: null }  # sin canvas
```

## Post-it del Functional Canvas (página 7)

| Sección            | Texto literal (post-it)                            | id        | Regla |
| ------------------ | -------------------------------------------------- | --------- | ----- |
| `Jobs`             | "Ejecucion de ingesta programada"                  | E1-FN-J01 | R4    |
| `Data imports`     | "Lectura de archivos CSV desde Storage"            | E1-FN-DI01| R2    |
| `Helpers`          | "Data-Validator ... integridad post-ingesta"       | E1-FN-H01 | R2    |
| `Data exports`     | "Escritura en BBDD"                                | E1-FN-DE01| R2    |
| `Data exports`     | "Escritura en FileSystem"                          | E1-FN-DE02| R2    |
| `Event triggers`   | "Notificaciones de alerta (si falla la ingesta)"   | E1-FN-ET01| R2    |
| `Data objects`     | "Publicación (Paper)"                              | E1-FN-OB01| R1    |
| `Data objects`     | "Documento de publicación"                         | E1-FN-OB02| R1    |
| `Data objects`     | "Registro de extracción (log)"                     | E1-FN-OB03| R1    |

Secciones vacías **coherentes** (el bundle no tiene UI):
`User inputs`, `UI-processing inputs`, `User visualizations / reports`.

## Salida del skill

### Bundle: Ingestor Worker (Functional, p. 7)

Entidades: Publicación · Documento de publicación · Registro de extracción
← Data objects (3 post-it, atributos por confirmar)

FR-ETL-001 El sistema DEBE ejecutar la ingesta de publicaciones de forma programada, sin intervención humana.
  ← functional / Jobs / "Ejecucion de ingesta programada"
  Escenario: Dado el horario de ingesta configurado, cuando se cumple, entonces se registra un nuevo registro de extracción con inicio, fin y cantidad de publicaciones incorporadas.
  [NEEDS CLARIFICATION: periodicidad no declarada en el canvas]

FR-ETL-002 El sistema DEBE leer los archivos CSV disponibles en el almacenamiento y validar su estructura antes de incorporarlos.
  ← functional / Data imports / "Lectura de archivos CSV desde Storage" + functional / Helpers / "Data-Validator ... integridad post-ingesta"
  Escenario (camino de error): Dado un archivo con estructura inválida, cuando se procesa, entonces ninguna fila se incorpora y el motivo queda en el registro.

FR-ETL-003 El sistema DEBE persistir cada publicación incorporada en el repositorio de datos y su documento en el almacenamiento de archivos.
  ← functional / Data exports / "Escritura en BBDD" + "Escritura en FileSystem"

FR-ETL-004 El sistema DEBE notificar una alerta cuando la ingesta falle.
  ← functional / Event triggers / "Notificaciones de alerta (si falla la ingesta)"
  Escenario: Dado que la ingesta termina con error, cuando finaliza el intento, entonces se emite una alerta identificando la causa y el archivo.

## Contexto para /speckit.plan (bundle Ingestor Worker)

Stack declarado: pendiente (la sección `Technology stack` del canvas Functional no tiene post-it; heredar del Structural si existe).
Constraints locales: solo software con licencia libre o académica (heredado del Architectural Context).

## Trazas (anexo)

| post_it_id  | sección         | regla | destino        | id_req                       |
| ----------- | --------------- | ----- | -------------- | ---------------------------- |
| E1-FN-J01   | Jobs            | R4    | spec.md#FR-001 | FR-ETL-001                   |
| E1-FN-DI01  | Data imports    | R2    | spec.md#FR-002 | FR-ETL-002                   |
| E1-FN-H01   | Helpers         | R2    | spec.md#FR-002 | FR-ETL-002 (fusión de calidad) |
| E1-FN-DE01  | Data exports    | R2    | spec.md#FR-003 | FR-ETL-003                   |
| E1-FN-DE02  | Data exports    | R2    | spec.md#FR-003 | FR-ETL-003                   |
| E1-FN-ET01  | Event triggers  | R2    | spec.md#FR-004 | FR-ETL-004                   |
| E1-FN-OB01  | Data objects    | R1    | Key Entities   | —                            |
| E1-FN-OB02  | Data objects    | R1    | Key Entities   | —                            |
| E1-FN-OB03  | Data objects    | R1    | Key Entities   | —                            |

`traces.length == 9 == total_stickies` → check de acceptance ✓.

## Duda agregada (a nivel de delivery, no de bundle)

Censo del Structural: `Portal Web Público UI` y `CMS Web Backoffice UI` sin Functional Canvas. Una sola duda agrupada por causa común:

> [NEEDS CLARIFICATION: falta detalle funcional de los bundles WEB-PUB y WEB-CMS]

(Las dudas se agrupan por causa común, no se duplican.)

## Balance del bundle ETL

- post-it: 9
- FR con prefijo: 4
- entidades: 3
- dudas: 1 (periodicidad del job)

## Lecciones del ejemplo

1. **El prefijo evita duplicación.** Si dos bundles leen la misma entidad `Publicación` (ETL y CMS), sus requisitos quedan distinguidos como `FR-ETL-002` y `FR-CMS-002`. Sin prefijo, `/speckit.tasks` los trata como el mismo.
2. **La fusión de calidad es la única excepción.** `FR-ETL-002` combina un `Data imports` con un `Helpers` (validador). Ambas trazas quedan citadas.
3. **Periodicidad, no frecuencia.** El job no declara periodicidad; el skill emite la duda — no escribe "cada 5 minutos".
4. **Entidades sin atributos.** El canvas da nombres; el skill no inventa campos. `/speckit.plan` los dejará abiertos.
5. **Secciones vacías, declaradas, no rellenas.** Las tres secciones de UI vacías van a `empty_sections[]` como `coherente`. La duda por los dos bundles de frontend sin canvas es **otra** duda, agrupada por causa.
