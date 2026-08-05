# Dudas agregadas — delivery E1 (Functional ×2 bundles)

> Una sola duda agrupada por causa común. La lista está ordenada por bloqueo:
> las marcadas como `[BLOQUEANTE]` requieren respuesta antes de cerrar el
> fragmento de `spec.md`; las demás quedan registradas para `/speckit.clarify`.

---

## D1 · No existe Structural Canvas formal en la entrega E1 — prefijo provisional

**[BLOQUEANTE para G2]** `7cs-functional-B` exige que el `bundle.code` venga del censo
del Structural. La entrega E1 no contiene un Structural Canvas formal (las 7 páginas
del PDF son: p1 diagrama libre, p2 Architectural, p3 System Context — extraído aparte,
p4 mix no-canónico de interfaces + stack + responsabilidades, p5 Functional Front, p6
Deployment, p7 Functional Back). El usuario autorizó usar como `bundle.code` provisional
el identificador del sub-canvas declarado en `header.canvas`:

- p5 (`header.canvas == "Functional Canvas Front"`) → `bundle.code = FRO`
- p7 (`header.canvas == "Functional Canvas Back"`) → `bundle.code = BCK`

Esta sustitución viola la guardrail G2 (prefijo del Structural) y G6 (mismatch de
censo). La auditoría `7cs-spec-audit` debe quedar notificada para tratarlas como
**aceptadas por excepción documentada** en lugar de fallas del skill.

---

## D2 · Bundles declarados inconsistentes entre los dos sub-canvas

**[BLOQUEANTE para G2]** El `header.canvas` distingue dos sub-canvas (Front y Back)
pero la sección `Bundles & components` no coincide entre los dos:

- Front (p5) declara 7 bundles: Compras, Recepción de Mercadería, Reposición,
  Inventario, Control Regulatorio, Reportes, Vencimientos.
- Back (p7) declara **8** bundles: los mismos 7 + **Módulo de Alertas y Notificaciones**
  (FNC-BC-06 en p7) + **Integración POS Venta** (FNC-BC-07 en p7), sustituyendo los
  `FNC-BC-06` "Reportes" del Front.

Lectura posible: los bundles **Reporte** (Front) y **Alertas** + **Integración POS**
(Back) son dominios distintos; el Front probablemente delega esos procesos al Back
mediante API. Sin un Structural Canvas formal, esta asignación es **inferencia del
orquestador** y no está declarada.

---

## D3 · Sección `Event handlers` vacía en el Back — inconsistencia

El Back declara `FNC-ET-01` "Cruce de umbral stock crítico → Event Handler", pero
la sección `Event handlers` está en `empty_sections[]`. El consumidor del evento no
está declarado en este canvas; la única contraparte plausible está en el Front
(`FNC-UPI-01` "Dashboard de stock") que sugiere un patrón de polling más que de
eventos. El sistema debe decidir:

- (a) ¿el Event Handler vive en el Front y consume el evento vía polling/SSE?
- (b) ¿el Event Handler vive en el Back y notifica al Front vía push?
- (c) ¿el Front hace polling sobre el stock directamente?

Sin respuesta, el flujo `ET-01 → alerta en dashboard (FRO-UV-02)` queda sin contrato
declarado.

---

## D4 · Periodicidad de jobs no declarada explícitamente

(3 dudas de periodicidad por bundle Back + 1 en Front)

- **FR-FRO-008** "Reporte semanal de próximos a vencer" (`FNC-UPI-02`): periodicidad
  "semanal" inferida del nombre; falta ventana de ejecución exacta (¿qué día de la
  semana? ¿qué hora?).
- **FR-FRO-010** "Reporte mensual de compras" (`FNC-UV-01`): periodicidad "mensual"
  inferida del nombre; falta día/hora.
- **FR-BCK-014** "Job diario revisión stock" (`FNC-J-01`): "diario" está nombrado,
  pero sin hora exacta ni política de reintento ante fallo.
- **FR-BCK-015** "Job mensual libro controlados" (`FNC-J-02`): "mensual" nombrado,
  sin día/hora exactos.
- **FR-BCK-016** "Job vencimientos" (`FNC-J-03`): **periodicidad completamente ausente**
  del canvas — solo el nombre "Job vencimientos". Es el único job sin siquiera
  adjetivo temporal.

(Estas 5 dudas cumplen el acceptance check: *"todo post-it de `Jobs` sin
periodicidad explícita produce exactamente una duda de periodicidad"*.)

---

## D5 · Atributos de entidades parcialmente declarados

`7cs-functional-B` no inventa atributos (regla R1/G4). El canvas Back da atributos
literales para 6 de las 7 entidades (`Producto`, `Lote`, `Movimiento de inventario`,
`Orden de Compra`, `Guía de despacho`, `Tipo de Movimiento`); `Informe de productos
controlados` solo cita "productos controlados en 'Vencidos'" como contexto.

Atributos abiertos (no declarados) que el plan/modelado tendrá que completar:
id, timestamps, autor, monto, número de documento, proveedor, etc. Se documentan
en el fragmento Back bajo cada entidad; esta es la duda agregada.

---

## D6 · Cabeceras de los canvas Front/Back vacías (System, Organization, Version, Date)

Los dos COM funcionales tienen los 4 campos de `header` en `null` (solo `canvas` está
poblado: "Functional Canvas Front" / "Functional Canvas Back"). Esto dificulta la
trazabilidad de la entrega (no se sabe a qué sistema ni a qué organización
pertenece, ni qué versión del canvas se está leyendo). Es un dato, no un error;
queda registrado para `/speckit.clarify`.

---

## D7 · Cabecera `template` ausente en ambos Functional

Los dos COM tienen `template: null`. El Architectural Context y el System Context sí
declaran `"7Cs v1.1 June 2026"`. La ausencia sugiere que el footer no fue impreso
en esas páginas, no que sea otra versión; se registra para auditoría.

---

## D8 · Inconsistencia entre los nombres de bundles del Front y las entidades del Back

El Front declara "Reporte" como bundle, pero no tiene sección `Data objects` para
los reportes. El Back tiene las entidades `Informe de productos controlados` y
`Libro de control` (FNC-OB-06 y FNC-DE-05). Si el bundle "Reportes" del Front se
mapea a estos outputs del Back, la asignación Front→Back no fue declarada en un
Structural formal — es inferencia.

---

## D9 · Asociación Front↔Back no declarada

`FNC-API-01` del Front ("Peticiones hacia el Backend Bundle vía API REST") y
`FNC-API-01` del Back ("Peticiones del Frontend Bundle") se emparejan por
complemento, pero ningún canvas declara explícitamente "el Front consume el
API del Back". La asociación es inferencia del orquestador.

---

## Resumen numérico de dudas

| Bundle   | Dudas | Bloqueantes |
|----------|-------|-------------|
| Front    | 6     | 3 (D1, D2, D9) |
| Back     | 7     | 3 (D1, D2, D3) |
| Delivery (agregadas) | 9 | 4 (D1, D2, D3 + D9 compartidas) |