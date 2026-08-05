---
name: 7cs-functional
description: Skill de mapeo del pipeline 7Cs→Spec Kit (Etapa B · paralelizable). Convierte cada COM de un Functional Canvas (uno por bundle; puede haber varios por entrega) en requisitos funcionales FR con prefijo de bundle, entidades, escenarios Dado/Cuando/Entonces y dudas para /speckit.specify, más stack por bundle para /speckit.plan. Usar cuando exista un COM con canvas == "functional" dentro del pipeline 7Cs, o cuando el usuario pida derivar requisitos funcionales desde Functional Canvas.
---

# 7cs-functional — Mapeo · Functional Canvas (×N bundles)

**El skill itera, no promedia.** Se ejecuta **una vez por cada Functional Canvas** y
prefija los identificadores con el bundle (`FR-ETL-001`, `FR-CMS-001`, `FR-INT-001`).
Sin ese prefijo, dos bundles que leen la misma entidad producen requisitos
indistinguibles y `/speckit.tasks` genera trabajo duplicado. Los prefijos vienen del
censo del Structural Canvas.

**Geometría del canvas = forma del requisito.** Cada sección genera un requisito
funcional de una naturaleza particular (ver tabla).

> Antes de emitir salida, leer:
> - `references/reglas-reescritura.md` — las 7 reglas R1–R7 con prohibiciones, forma canónica del FR y justificación.
> - `references/com-schema.md` — esquema del Canvas Object Model y convenciones (bbox, parent, empty_sections, idempotencia).
> - `references/ejemplo-trabajado-etl.md` — caso completo del bundle ETL de Ejemplo 1, con post-it tabulados, salida, trazas y balance.

---

## Contrato

```yaml
name: 7cs-functional
when_to_use: >
  El COM tiene canvas == "functional". Ejecutar una vez por instancia
  (una por bundle), con el censo del Structural como referencia de prefijos.
inputs:
  com: CanvasObjectModel        # única fuente de verdad; prohibido volver al PDF
  delivery_id: string
  bundle_census: [ string ]     # del skill 7cs-structural, para prefijos y chequeo
outputs:
  fragment: markdown            # §FR del bundle, §Key Entities, escenarios
  plan_context: markdown        # Technology stack + constraints locales, para /speckit.plan
  traces: [ {sticky_id, section, target_id} ]
  clarifications: [ string ]
procedure:
  1. Identificar el bundle (Bundles & components) y su prefijo desde el censo.
  2. Verificar secciones esperadas. Vacías → registrar (pueden ser coherentes).
  3. Para cada sección aplicar SU regla de mapeo (tabla fija).
  4. Normalizar cada post-it a la forma canónica (R1–R7); escenario por FR.
  5. Emitir traza por post-it. Nunca fusionar, salvo la excepción de calidad.
guardrails:
  - Prohibido inventar atributos de entidades, periodicidades o esquemas.
  - Prohibido escribir stack en el fragmento de spec (va a plan_context).
  - Texto literal del post-it siempre citado entre comillas.
acceptance:
  - traces.length == total_stickies
  - todo FR de comportamiento tiene al menos un escenario Dado/Cuando/Entonces
  - todos los FR llevan el prefijo del bundle
```

---

## Tabla de mapeo (una fila por sección; destino único)

| Sección | Qué produce el skill |
|---|---|
| Bundles & components | Agrupador del bloque de FR; se enlaza con el censo del Structural |
| Data objects | **§Key Entities** con atributos por confirmar |
| User inputs · UI-processing inputs | FR iniciados por persona; si están vacíos y el bundle no tiene interfaz humana, se reportan como **coherentes, no como omisión** |
| API inputs | FR de recepción por contrato (query requests, command endpoints, callback) |
| Data imports · exports | FR de lectura y de persistencia observables |
| Jobs | **FR con disparador temporal**: un FR por job + duda de periodicidad si no está declarada |
| Event handlers · Event triggers | FR reactivos y notificaciones |
| Helpers | Reglas de validación y cálculo → FR de calidad de datos |
| User visualizations / reports | FR de visualización; si está vacío → duda de alcance de UI |
| Technology stack · Constraints | `plan.md` por bundle + restricciones locales. Fuera de `spec.md` |

### Clasificación de secciones vacías (referencia rápida)

| Sección                              | Vacía es coherente cuando…                                  | Vacía es inconsistencia cuando…                       |
| ------------------------------------ | ----------------------------------------------------------- | ----------------------------------------------------- |
| `User inputs` / `UI-processing`      | el bundle no expone UI (p.ej. ETL worker)                   | el bundle es de UI según el Structural                |
| `User visualizations / reports`      | el bundle no expone UI                                      | el bundle declara pantallas o reportes en el Structural |
| `API inputs`                         | el bundle no recibe llamadas                                | el bundle es servidor o worker expuesto               |
| `Data imports` / `Data exports`      | (raro) el bundle es stateless                               | existe cualquier flujo de datos en el resto del canvas |
| `Jobs`                               | el bundle es reactivo puro (event-driven)                   | hay persistencia que requiere conciliación periódica  |
| `Event handlers` / `Event triggers`  | el bundle no reacciona a eventos                            | el bundle declara watchers, notificaciones o alertas  |
| `Helpers`                            | el bundle no transforma datos                               | el bundle importa o exporta datos                     |
| `Technology stack` / `Constraints`   | (aceptable) el stack se decidirá en `plan.md`               | el bundle declara integraciones que sí fijan stack    |
| `Bundles & components`               | (nunca) — la sección debe existir como mínimo con el nombre | siempre                                              |

Una sección vacía se reporta siempre; la clasificación (coherente / inconsistencia) decide si la duda resultante bloquea la corrida o solo la registra para `/speckit.clarify`.

---

## Reglas específicas de este skill

- **Fusión permitida, con regla.** Se permite combinar dos post-it en un FR **solo**
  cuando uno es condición de calidad del otro (p.ej. un import de datos + su validador),
  y **ambas trazas quedan citadas**. Fuera de ese caso: un post-it → un requisito.
- **Los jobs son la mina de NFR.** Todo job implica periodicidad, ventana de ejecución y
  comportamiento ante fallo. El canvas casi nunca los declara: emitir
  `[NEEDS CLARIFICATION: periodicidad no declarada en el canvas]` por cada uno.
  **Nunca** escribir una frecuencia inventada.
- **Entidades sin atributos.** Un nombre no es un esquema. Declarar la entidad y dejar
  los atributos abiertos: inventarlos es el modo de falla más costoso, porque
  `/speckit.plan` los convierte en tablas.
- **Secciones vacías con sentido.** Evaluar coherencia: un bundle sin interfaz humana con
  *User inputs* vacío es coherente; un bundle de UI con *User visualizations* vacío es una
  duda de alcance.

Las 7 reglas de reescritura (R1–R7) con sus prohibiciones, la forma canónica del FR y
la justificación de "función total" están en `references/reglas-reescritura.md`.

El esquema del COM, las convenciones de `id`, `bbox`, `parent`, `empty_sections` y la
regla "el COM no interpreta" están en `references/com-schema.md`.

---

## Reglas del prefijo de bundle

- El prefijo es **siempre** el `bundle.code` del censo del Structural — nunca derivado del texto del post-it.
- Formato del identificador: `FR-{bundle.code}-{NNN}` con `NNN` zero-padded a 3 dígitos.
- Dos bundles pueden compartir el sufijo numérico (`FR-ETL-001` y `FR-CMS-001`); el prefijo es lo que los hace distintos.
- Si el post-it no permite identificar el bundle (p.ej. dice "el worker" sin nombre), el prefijo se obtiene del `Bundles & components` del propio canvas; si también ahí falta, se emite duda.
- Los `Helpers` y otras reglas de soporte pueden usar el prefijo `HE-{bundle.code}-{NNN}` para traceability, pero no se emiten como requisitos visibles para el usuario.

---

## Formato de salida

```markdown
### Bundle: {nombre} (Functional, p. {n})

Entidades: {lista} ← Data objects ({n} post-it, atributos por confirmar)

FR-{PREFIJO}-001 El sistema DEBE {verbo observable} {objeto} {condición}.
  ← {sección} "{texto literal}" [+ "{segundo post-it}" si fusión de calidad]
  Escenario: Dado ..., cuando ..., entonces ...
  [NEEDS CLARIFICATION: ...]
...

## contexto para /speckit.plan (bundle {nombre})
Stack declarado: {tecnologías literales} · Constraints locales: {lista}
```

Cerrar con el balance de los Functional de la entrega: post-it, FR con prefijo,
entidades, dudas; y si el censo del Structural indica bundles sin canvas, repetir la
duda de alcance correspondiente.

El caso completo (Ejemplo 1, bundle ETL) con post-it tabulados, salida, trazas y
balance está en `references/ejemplo-trabajado-etl.md`.

---

## Guardrails (numerados, auditables)

- **G1 — Iteración, no fusión.** El skill corre una vez por Functional Canvas. Nunca produce un FR que abarque dos bundles.
- **G2 — Prefijo de bundle obligatorio.** Un FR sin `{bundle.code}-` en su identificador es un defecto; el skill lo rechaza antes de emitir.
- **G3 — Coherencia con el censo.** Si el Structural declara un bundle con `functional_canvas_page` no nula y el COM no tiene la página, el skill se detiene y emite una sola duda agrupada que cubre **todos** los bundles afectados. No inventa Functional Canvases.
- **G4 — Sin entidades inventadas.** Los nombres de `Data objects` van a `Key Entities`; los atributos quedan abiertos. Inventar campos es el modo de falla más caro (el plan los convierte en tablas).
- **G5 — Secciones vacías son hallazgos.** Una sección sin post-it se registra en `empty_sections[]` y se clasifica como `coherente` o `inconsistencia`. En ambos casos produce una duda; solo el primero es no bloqueante.
- **G6 — Falla por mismatch de censo.** Si el número de Functional Canvases del COM no coincide con el conteo de bundles con `functional_canvas_page` no nula, el skill aborta y reporta la discrepancia. El orquestador decide si continúa.
- **G7 — Nombres de tecnología, solo en plan.md.** Cualquier tecnología de la lista negra del corpus (Java Spring, Python, Node.js, PostgreSQL, Nginx, Docker, Linux…) queda prohibida en el fragmento de `spec.md`. El skill greps su propia salida antes de emitir.
- **G8 — Texto literal citado.** Cada traza cita el texto del post-it entre comillas dobles, **exactamente** como aparece en el COM. Sin paráfrasis.

---

## Acceptance (chequeos que el skill de auditoría ejecuta)

La corrida se declara válida por `7cs-spec-audit` si y solo si:

- [ ] `traces.length == total_stickies` para cada Functional Canvas del delivery.
- [ ] Todo identificador de FR cumple `^FR-[A-Z0-9]+-[0-9]{3}$`.
- [ ] Todo FR de comportamiento (R2/R3/R4/R7) tiene al menos un escenario `Dado/Cuando/Entonces`.
- [ ] El número de Functional Canvases procesados es igual al número de bundles con `functional_canvas_page` no nula en el censo.
- [ ] Ningún nombre de tecnología de la denylist aparece en el fragmento de `spec.md`.
- [ ] Todo post-it de `Jobs` sin periodicidad explícita produce exactamente una duda de periodicidad.
- [ ] `empty_sections[]` no es vacío **si y solo si** el canvas tiene al menos una sección sin post-it; ambas clasificaciones (`coherente`, `inconsistencia`) deben aparecer en `clarifications` cuando correspondan.
- [ ] `balance.fr_count + balance.clarification_count` del delivery coincide con la fila de la tabla de auditoría para el tipo Functional.

Si cualquier check falla, la auditoría bloquea la corrida y el orquestador pide reejecución de `7cs-functional` con un COM corregido o un censo aclarado.

---

## Cross-references (con el resto del pipeline)

- **Vocabulario cerrado** de las 6 tipos de canvas y sus secciones — plantilla 7Cs v1.1 (June 2026).
- **Censo de bundles** — producido por `7cs-structural`; este skill lo consume, no lo produce.
- **Reglas R1–R7** — compartidas con `7cs-system-context` y `7cs-business-context`; la tabla de mapeo por sección es lo que difiere.
- **Composición y deduplicación** entre canvas → `7cs-spec-compose`.
- **Métricas de cobertura (C), ambigüedad (A), contaminación técnica (T) y verificabilidad (V)** → `7cs-spec-audit`.

---

## Etapa y reglas del pipeline (transversales)

Este skill pertenece a la **Etapa B · Mapeo** y se ejecuta en paralelo con
`7cs-business-context`, `7cs-architectural-context`, `7cs-system-context`,
`7cs-structural` y `7cs-deployment` (todos ven únicamente su COM por tipo).
Tres reglas del pipeline lo gobiernan:

- **Aislamiento.** Solo consume el COM con `canvas == "functional"` de la entrega
  y el censo de bundles producido por `7cs-structural`. No lee otros canvas
  directamente; si necesita un dato que no está, emite `[NEEDS CLARIFICATION]`.
- **Idempotencia.** Con el mismo COM y el mismo censo, emite los mismos
  `FR-{bundle.code}-{NNN}` y las mismas trazas; los identificadores de post-it
  (`E1-FN-J01`, etc.) son estables entre corridas.
- **Fallo explícito.** Ante ambigüedad o dato faltante, **no elige**: emite
  `[NEEDS CLARIFICATION: ...]` y deja la decisión para `/speckit.clarify`.
  No inventa periodicidades de jobs, atributos de entidades ni nombres de bundles.
