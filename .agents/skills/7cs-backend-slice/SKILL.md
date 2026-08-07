---
name: 7cs-backend-slice
description: Genera un bundle backend mínimo y ejecutable a partir de COM, especificación, trazas y aclaraciones cerradas de un delivery 7Cs. Usar después de auditoría para implementar exactamente una funcionalidad proveniente de un único post-it Functional Back, con código fuente, prueba, trazabilidad y ejecución local o Docker.
---

# 7cs-backend-slice

1. Leer sólo `com/<delivery>-functional-back-*.json`, `composed/<delivery>-specify.md`, `composed/<delivery>-traceability.json` y `clarifications/<delivery>-answers.json`.
2. Verificar que no existan preguntas abiertas y seleccionar exactamente un post-it funcional backend con contrato suficiente.
3. Mantener la tecnología declarada en Structural, Functional Back y Deployment; no inventar otro stack.
4. Generar `implementation/<delivery>/backend-<capability>/` con código fuente, prueba automatizada, `Dockerfile`, lanzadores locales multiplataforma (`run.sh` y `run.bat`) y README de ejecución con comandos POSIX.
5. Implementar únicamente la capacidad del post-it elegido. Permitir infraestructura mínima, health check y adaptadores necesarios, sin incorporar otra regla de negocio.
6. Crear `traceability.json` con `{delivery_id, sticky_id, requirement_id, literal_text, source_files, implemented_files}`.
7. No modificar COM, mapping, composed, clarifications ni recursos.

Acceptance: una sola funcionalidad trazada, prueba ejecutable, imagen Docker construible, cero dependencia cloud obligatoria para la demostración local.
