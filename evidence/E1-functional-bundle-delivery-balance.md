# Balance — delivery E1 (Functional ×2 bundles)

## Resumen ejecutivo

| Indicador                                              | Front (p5) | Back (p7) | Delivery |
|--------------------------------------------------------|------------|-----------|----------|
| COM fuente                                             | `com/E1-functional-p5.json` | `com/E1-functional-p7.json` | 2 archivos |
| `bundle.code` aplicado                                 | `FRO`      | `BCK`     | 2 prefijos provisionales |
| Post-it totales                                        | 26         | 32        | **58**   |
| Post-it en `Bundles & components` (no cuentan como FR) | 7          | 8         | 15       |
| Post-it útiles para mapping                            | 19         | 24        | 43       |
| FR emitidos con prefijo                                | 19         | 16        | **35**   |
| Entidades en §Key Entities                             | 0 (vacía)  | 7         | **7**    |
| Escenarios `Dado/Cuando/Entonces`                      | 19         | 19        | **38**   |
| Dudas emitidas                                         | 6          | 7         | **9** agregadas |
| Secciones vacías → `coherente`                         | 8          | 4         | 12       |
| Secciones vacías → `inconsistencia`                    | 0          | 1         | 1        |
| Fusiones de calidad aplicadas                          | 0          | 1         | 1        |

## Acceptance checks (per SKILL.md §"Acceptance")

- [x] `traces.length == total_stickies` por canvas (Front: 26/26, Back: 32/32).
- [x] Todo FR cumple `^FR-[A-Z0-9]+-[0-9]{3}$` (formato `FR-FRO-001..019`, `FR-BCK-001..016`).
- [x] Todo FR de comportamiento (R2/R3/R4/R7) tiene al menos un escenario `Dado/Cuando/Entonces`.
- [ ] **G2 — Prefijo de bundle obligatorio:** **aceptado por excepción documentada**
  (no existe Structural Canvas formal en E1; decisión del usuario registrada en D1).
- [ ] **G3 — Coherencia con el censo:** **violación registrada** — el "censo"
  se sustituyó por los `header.canvas` ("Front"/"Back") de los dos COM.
- [ ] **G6 — Mismatch de censo:** **violación registrada** — los bundles declarados
  no coinciden entre Front y Back (D2).
- [x] Ningún nombre de tecnología de la denylist en el fragmento de `spec.md`
    (revisado: las menciones "Node.js", "PostgreSQL", "GCP", "SPA", "POS", "API REST"
    viven en `plan_context`, no en `spec.md`).
- [x] Todo post-it de `Jobs` sin periodicidad explícita produce exactamente una duda
    de periodicidad (5 dudas: FRO-008, FRO-010, BCK-014, BCK-015, BCK-016).
- [x] `empty_sections[]` no es vacío (lo es) **y** el canvas tiene secciones sin
    post-it; las clasificaciones `coherente` / `inconsistencia` aparecen en
    `E1-functional-bundle-BACK-traces.md` y en `E1-functional-bundle-FRONT-traces.md`.
- [ ] **`balance.fr_count + balance.clarification_count` del delivery coincide
  con la fila de la tabla de auditoría para el tipo Functional.** El skill
  `7cs-spec-audit` aún no existe; este acceptance queda pendiente para la
  Etapa de auditoría.

## Guardrails invocados como violación aceptada

| Guardrail | Estado | Razón |
|-----------|--------|-------|
| G1 — Iteración, no fusión                                | ✓ | Una corrida por COM (Front y Back son dos corridas separadas). |
| G2 — Prefijo de bundle obligatorio                       | ⚠️ | Sustituido por `FRO`/`BCK` por falta de Structural Canvas. |
| G3 — Coherencia con el censo                             | ⚠️ | Sustituido por los `header.canvas`. |
| G4 — Sin entidades inventadas                            | ✓ | Atributos abiertos, no inventados. |
| G5 — Secciones vacías son hallazgos                      | ✓ | 12 coherentes + 1 inconsistencia, todas clasificadas. |
| G6 — Falla por mismatch de censo                         | ⚠️ | Mismatch detectado y registrado (D2). |
| G7 — Nombres de tecnología solo en plan.md               | ✓ | Verificado: "Node.js", "PostgreSQL", "GCP", "SPA", "POS", "API REST" solo en `plan_context`. |
| G8 — Texto literal citado                                | ✓ | Todas las trazas citan el texto exacto entre comillas. |

## Artefactos emitidos en esta corrida

```
evidence/E1-functional-bundle-FRONT-fragment.md          ← spec.md §FR + §Key Entities (Front)
evidence/E1-functional-bundle-FRONT-traces.md            ← tabla 1-a-1 post-it → FR + secciones vacías
evidence/E1-functional-bundle-FRONT-plan_context.md      ← stack + constraints para /speckit.plan
evidence/E1-functional-bundle-BACK-fragment.md           ← spec.md §FR + §Key Entities (Back) + Constraints ACC heredadas
evidence/E1-functional-bundle-BACK-traces.md             ← tabla 1-a-1 post-it → FR + secciones vacías
evidence/E1-functional-bundle-BACK-plan_context.md       ← stack + constraints para /speckit.plan
evidence/E1-functional-bundle-delivery-clarifications.md ← 9 dudas agregadas (D1..D9)
evidence/E1-functional-bundle-delivery-balance.md        ← este archivo
```

## Próximos pasos sugeridos

1. **Resolver dudas bloqueantes** (D1, D2, D3, D9) antes de ejecutar
   `7cs-spec-compose` y `7cs-spec-audit`.
2. **Decidir periodicidad de los jobs** (D4) en `/speckit.clarify`.
3. **Una vez creado el Structural Canvas formal** (futura página o re-trabajo del PDF),
   reejecutar `7cs-functional-B` con el `bundle.code` correcto y consolidar los dos
   fragmentos Front/Back en un único fragmento por bundle real (no por sub-canvas).
4. **Ejecutar `7cs-spec-compose`** sobre los dos fragmentos para deduplicar y
   componer el `spec.md` final del delivery E1.