# Plan context — bundle Front (E1, p. 5)

> Stack y restricciones **locales** del bundle Front, derivados del COM
> `com/E1-functional-p5.json`. Se traslada a `/speckit.plan` y **no** se incluye
> en `spec.md` (regla R6).

## Stack declarado (texto literal de los post-it)

- **Interfaz de usuario:** "Frontend SPA responsiva" — `FNC-CT-01`.
  - Decisión de stack para el plan: SPA web con diseño responsivo (Framework UI a
    decidir en `/speckit.plan`; este skill no nombra productos).
- **Integración:** "Peticiones hacia el Backend Bundle vía API REST" — `FNC-API-01`.

## Constraints locales

- **Sin soporte offline** (`FNC-CT-02`): el sistema no debe funcionar offline.
  Implicación para el plan: la infraestructura debe garantizar disponibilidad de red
  en el local; las operaciones críticas (registro de recepción, OC, registro de
  destrucción, alerta de stock crítico) no pueden ejecutarse sin conexión.
- **Stock crítico para dashboard** (`FNC-CT-03`): el dashboard debe mostrar de forma
  visible (fila roja) los productos cuyo saldo está bajo el umbral. Implicación para
  el plan: el pipeline de cálculo de stock crítico debe ejecutarse con periodicidad
  suficiente para que la alerta sea oportuna; revisar latencia de los Jobs del Back
  (`FR-BCK-006` "Job diario revisión stock") que es la fuente.

## Pendientes para `/speckit.plan`

- Definir el framework concreto de la SPA (R6: nombre reservado para plan, no para spec).
- Definir el umbral de stock crítico (FRO lo cita pero no lo numera).
- Decidir periodicidad exacta de los reportes semanales (FNC-UPI-02) y mensuales (FNC-UV-01),
  que el canvas solo declara por nombre.