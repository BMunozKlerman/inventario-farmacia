---
name: 7cs-spec-compose
description: Compone fragmentos, contexto de plan, trazas y dudas generados por 7cs-com-transform en entradas para Spec Kit y un entregable trazable. Usar sólo después de transformar todos los COM.
---

# 7cs-spec-compose

1. Leer únicamente `mapping/<delivery>-*`; no leer PDF ni completar COM.
2. Verificar que cada traza apunte a un destino existente.
3. Deduplicar sólo mediante una regla y conservar todos los ids fuente.
4. Generar constitution, specify, plan y anexo de trazabilidad en `composed/`.
5. Con dudas bloqueantes, conservar contexto pero marcar plan como `BLOCKED`.

Acceptance: ninguna evidencia perdida, ids únicos, trazas sin huérfanos y tecnología fuera de specify.

