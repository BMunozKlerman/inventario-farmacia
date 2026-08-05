# Contrato transversal 7Cs -> entregable

## Flujo

1. **Separación:** un PDF inmutable dentro de `resources/` se renderiza y divide en candidatos.
2. **Lectura selectiva:** cada skill recibe candidatos, acepta sólo su canvas, ignora los demás y genera un COM literal.
3. **Fuente de verdad:** una vez persistidos, sólo los COM alimentan las fases posteriores; nunca se vuelve al PDF para completar datos.
4. **Transformación:** `7cs-com-transform` aplica reglas explícitas por tipo de COM y produce fragmentos, contexto de plan, trazas y dudas.
5. **Composición y auditoría:** se construye el entregable y se valida antes de plan, tareas o código.

## Propiedad exclusiva

| título aceptado | lector | canvas COM | código |
|---|---|---|---|
| Business Context Canvas | 7cs-business-context | business_context | BUS |
| Architectural Context Canvas | 7cs-architectural-context | architectural_context | ACC |
| System Context Canvas | 7cs-system-context | system_context | SCC |
| Structural Canvas | 7cs-structural | structural | STR |
| Functional Canvas Front | 7cs-functional-A | functional/front | FNC-FRT |
| Functional Canvas Back | 7cs-functional-B | functional/back | FNC-BCK |
| Deployment Canvas | 7cs-deployment | deployment | DEP |

## Invariantes

- El COM copia; no interpreta.
- Un lector ajeno devuelve `ignored` y no escribe archivo.
- Cada post-it conserva texto literal, sección, `bbox`, `parent` e id estable.
- Toda ambigüedad usa `[NEEDS CLARIFICATION]`; nunca se adivina.
- Cada post-it aceptado debe tener exactamente una traza después de transformación.
- Tecnología y topología van a plan; comportamiento observable a spec.

## Archivos

- Entrada: `resources/<archivo>.pdf`
- Evidencia: `evidence/<delivery>-pNN[-cNN].png`
- COM: `com/<delivery>-<canvas>[-<variant>]-pNN.json`
- Transformación: `mapping/<delivery>-<canvas>[-<variant>]-{fragment.md,plan_context.md,traces.json}`
- Composición: `composed/<delivery>-*`
- Auditoría: `audit/<delivery>-*`

