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
  clarification_answers: clarifications/<delivery>-answers.json | null
outputs:
  fragments: [mapping/<delivery>-<canvas>[-<variant>]-fragment.md]
  plan_contexts: [mapping/<delivery>-<canvas>[-<variant>]-plan_context.md]
  traces: [mapping/<delivery>-<canvas>[-<variant>]-traces.json]
  clarifications: clarifications/<delivery>-transformation.json
```

1. Validar cada COM y seleccionar reglas por `canvas` y `variant`.
2. Transformar cada post-it exactamente una vez y conservar su cita literal.
3. Mantener Front y Back separados; correlacionarlos sólo por delivery y bundle declarado.
4. Emitir requisitos observables y escenarios en fragmentos; tecnología y topología en plan_context.
5. Emitir dudas por contratos, permisos, esquemas, roles, métricas o periodicidades ausentes como preguntas con `{id, question, reason, status}`.
6. Si existen respuestas, analizarlas contra la pregunta y los COM. Marcar `resolved` sólo cuando sean suficientes; en otro caso mantener `open` y reformular una pregunta concreta.
7. No inventar datos ni consultar nuevamente el PDF.
8. No autorizar composición mientras exista una pregunta `open`.

Acceptance: cobertura de trazas 1,00; ids estables; cero tecnología en spec; todo FR con Dado/Cuando/Entonces.
