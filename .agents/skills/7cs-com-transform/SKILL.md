---
name: 7cs-com-transform
description: Consume los COM literales generados por las siete skills lectoras y los transforma mediante reglas explícitas por canvas en fragmentos de spec, contexto de plan, trazas y dudas. Usar sólo después de completar la lectura; nunca volver al PDF.
---

# 7cs-com-transform

Los COM son la única fuente de verdad. Leer `references/mapping-contract.md`.

```yaml
inputs:
  delivery_id: string
  com_paths: [com/<delivery>-*.json]
outputs:
  fragments: [mapping/<delivery>-<canvas>[-<variant>]-fragment.md]
  plan_contexts: [mapping/<delivery>-<canvas>[-<variant>]-plan_context.md]
  traces: [mapping/<delivery>-<canvas>[-<variant>]-traces.json]
  clarifications: [string]
```

1. Validar cada COM y seleccionar reglas por `canvas` y `variant`.
2. Transformar cada post-it exactamente una vez y conservar su cita literal.
3. Mantener Front y Back separados; correlacionarlos sólo por delivery y bundle declarado.
4. Emitir requisitos observables y escenarios en fragmentos; tecnología y topología en plan_context.
5. Emitir dudas por contratos, permisos, esquemas, roles, métricas o periodicidades ausentes.
6. No inventar datos ni consultar nuevamente el PDF.

Acceptance: cobertura de trazas 1,00; ids estables; cero tecnología en spec; todo FR con Dado/Cuando/Entonces.

