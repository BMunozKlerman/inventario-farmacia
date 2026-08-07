---
name: 7cs-spec-audit
description: Audita el entregable 7Cs recontando post-its desde los COM y verificando cobertura, ambigüedad, contaminación técnica, verificabilidad, ids y falsabilidad. Usar antes de plan, tareas o implementación.
---

# 7cs-spec-audit

- `C = post-its con traza válida / post-its COM`; debe ser 1,00.
- `A = dudas abiertas / obligaciones`; se informa.
- `T = tecnologías concretas en specify`; debe ser 0.
- `V = FR con escenario Dado/Cuando/Entonces / FR`; debe ser 1,00.

Ejecutar `scripts/audit_pipeline.py`. Recontar desde COM, no confiar en balances declarados. La falsabilidad retira una traza sólo en memoria y debe provocar rechazo.

Bloquear si C, T o V fallan. Rechazar la auditoría si queda cualquier aclaración abierta; el pipeline debe haber pausado antes de composición.
