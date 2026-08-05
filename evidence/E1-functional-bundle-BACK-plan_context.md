# Plan context — bundle Back (E1, p. 7)

> Stack y restricciones **locales** del bundle Back, derivados del COM
> `com/E1-functional-p7.json`. Se traslada a `/speckit.plan` y **no** se incluye
> en `spec.md` (regla R6).

## Stack declarado (texto literal del post-it)

- `FNC-TS-01`: "Backend: monolito Node.js / DB: PostgreSQL / Infra: GCP".
  - Decisión de stack para el plan: monolito server-side en Node.js, base de datos
    PostgreSQL administrada (Cloud SQL en GCP), infraestructura GCP.
  - Regla R6: los nombres de productos concretos (Node.js, PostgreSQL, GCP) van a
    `plan.md`; en `spec.md` se describe su función (procesamiento, persistencia
    relacional, plataforma en la nube).

## Constraints locales (Back)

- `FNC-H-01` "Servicio envío correo (alertas)" — infraestructura debe incluir un
  servicio de envío de correo transaccional (SMTP relay, proveedor de email).
- `FNC-H-02` "Servicio generación PDF" — dependencia en una librería o servicio de
  generación de PDF.
- `FNC-API-03` (inmutabilidad) — la persistencia debe garantizar que los registros
  insertados no se actualicen ni borren; patrón append-only o equivalente.

## Pendientes para `/speckit.plan`

- Decidir framework concreto del monolito Node.js (Express, NestJS, Fastify, etc.) —
  nombre reservado para plan, no para spec.
- Decidir periodicidad exacta del Job de vencimientos (`FR-BCK-016`) — el canvas solo
  nombra el job.
- Decidir ventana horaria y política de reintento de los Jobs (`FR-BCK-014`, `015`).
- Definir los **atributos abiertos** de las 7 entidades listadas en §Key Entities
  (atributos del canvas ya están citados; los demás se llenan en plan/modelado).
- Decidir el evento exacto que se intercambia entre el Event Trigger y el Event Handler
  (en este COM el `Event handlers` está vacío y se declara como `empty_sections[]`; queda
  como duda de orquestación ver `evidence/E1-functional-bundle-delivery-clarifications.md`).