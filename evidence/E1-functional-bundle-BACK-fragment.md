# Fragmento de `spec.md` — bundle Back (E1, p. 7)

> **Origen:** `com/E1-functional-p7.json` (header.canvas = "Functional Canvas Back")
> **Prefijo aplicado:** `BCK` (decisión documentada: no existe Structural Canvas formal
> en E1; se usa el identificador del sub-canvas como `bundle.code` provisional).
> **Traza fuente:** 32 post-it (BC=8, API=3, UPI=2, OB=7, DE=5, ET=1, H=2, J=3, TS=1).
> **Mapping skill:** `7cs-functional-B` ejecutado sobre el COM de `7cs-functional-A`.

---

## §Key Entities (Back)

El canvas Back declara **7 entidades** en `Data objects` (FNC-OB-01..07). Los
atributos se citan **tal cual aparecen** en el canvas; los atributos adicionales
quedan abiertos (regla R1: nunca inventar).

- **Producto** — atributos del canvas: `categoría, controlado sí/no`. Atributos abiertos: id, nombre, presentación, unidad de medida, precio, etc. (a decidir en `/speckit.plan`).
- **Lote** — atributos del canvas: `número, vencimiento, saldo`. Atributos abiertos: proveedor, registro sanitario, etc.
- **Movimiento de inventario** — atributos del canvas: `lote, vencimiento, saldo, ubicación`. Atributos abiertos: timestamp, autor, tipo (referencia a Tipo de Movimiento), documento asociado.
- **Orden de Compra** — atributos del canvas: `estados: emitida, enviada, confirmada por proveedor, recepcionada`. Atributos abiertos: número, items, proveedor, monto, fecha de emisión.
- **Guía de despacho** — atributos del canvas: `canje o destrucción`. Atributos abiertos: número, fecha, emisor, receptor, lotes involucrados, motivo.
- **Informe de productos controlados** — atributos del canvas: `productos controlados en "Vencidos"`. Atributos abiertos: período, totales, firma responsable.
- **Tipo de Movimiento de inventario** — atributos del canvas: `venta, compra, nota de crédito, canje, destrucción`. Atributos abiertos: descripción, signo (entrada/salida), requiere autorización.

---

## §Functional Requirements — bundle Back

FR-BCK-001 El sistema DEBE exponer una API REST que reciba peticiones del Frontend Bundle (Front).
  ← functional / API inputs / "Peticiones del Frontend Bundle"
  Regla R3: nombre del producto ("API REST") → `plan.md`; en `spec.md` se describe
  la dirección y contraparte.
  Escenario: Dada una petición válida del Front, cuando se recibe, entonces el sistema
    la procesa y responde con el recurso solicitado o un error de dominio.

FR-BCK-002 El sistema DEBE exponer una API REST que registre las transacciones originadas en el POS.
  ← functional / API inputs / "Registro de transacciones desde el POS"
  Regla R3: nombre del producto ("POS") → `plan.md`.
  Escenario: Dada una transacción POS, cuando se recibe, entonces el sistema persiste
    el movimiento de inventario inmutable asociado.
  [NEEDS CLARIFICATION: ¿qué eventos del POS se aceptan (venta, nota de crédito, devolución)?
  El canvas solo menciona "transacciones" en plural.]

FR-BCK-003 El sistema DEBE garantizar que los registros de transacciones, una vez emitidos, no
  puedan modificarse ni alterarse.
  ← functional / API inputs / "Registros de transacciones inmutables una vez emitidos"
    + functional / Data objects / "Movimiento de inventario"
  Fusión de calidad (R2 + R7): la inmutabilidad es una restricción que aplica al
  objeto "Movimiento de inventario" (FNC-OB-03); ambas trazas citadas.
  Regla R7: la inmutabilidad obliga a compensatorios explícitos (notas de crédito,
  ajustes) en lugar de borrado directo.
  Escenario (feliz): Dado un movimiento registrado, cuando el usuario intenta modificarlo,
    entonces el sistema rechaza la modificación y exige emitir el movimiento correctivo.
  Escenario (error): Dado un fallo de integridad, cuando se detecta, entonces el sistema
    registra el incidente sin alterar el movimiento original.

FR-BCK-004 El sistema DEBE permitir al usuario consultar las Ordenes de Compra pendientes.
  ← functional / UI-processing inputs / "OC pendientes"
  Escenario: Dado un usuario autorizado, cuando consulta, entonces el sistema muestra
    las OCs en estados `emitida`, `enviada` o `confirmada por proveedor` que aún no
    han sido recepcionadas.

FR-BCK-005 El sistema DEBE permitir al usuario consultar el listado de productos en ubicación "Vencidos".
  ← functional / UI-processing inputs / "Vencidos"
  Regla observada del canvas (Back, FNC-UPI-02): los productos en "Vencidos" no están
  disponibles para venta ni compra, pero cuentan en inventario.
  Escenario: Dado un producto en estado vencido, cuando el usuario consulta, entonces el
    sistema lo lista en la ubicación "Vencidos" excluyéndolo de las consultas de stock
    disponible para venta.

FR-BCK-006 El sistema DEBE exponer una API para que el POS consulte el stock disponible por
  producto.
  ← functional / Data exports / "Consulta de stock (POS)"
  Regla R3: nombre del producto ("POS") → `plan.md`.
  Escenario: Dado un producto identificable, cuando el POS consulta, entonces el sistema
    responde con el saldo disponible, lotes con saldo y ubicaciones activas.

FR-BCK-007 El sistema DEBE generar documentos PDF/Excel para Órdenes de Compra, Guías de Despacho
  e Informes de productos controlados.
  ← functional / Data exports / "PDF/Excel"
  Escenario: Dado un documento emitido (OC, guía o informe), cuando el usuario solicita
    la descarga, entonces el sistema produce el documento en el formato elegido.

FR-BCK-008 El sistema DEBE imprimir guías de despacho (canje o destrucción) en formato foliado/timbrado.
  ← functional / Data exports / "Guía despacho impresa"
  Escenario: Dada una guía de despacho emitida, cuando el usuario solicita la impresión,
    entonces el sistema imprime sobre hoja foliada/timbrada.

FR-BCK-009 El sistema DEBE generar un informe de productos controlados presentes en "Vencidos".
  ← functional / Data exports / "Informe controlados"
  Escenario: Dado un período de consulta, cuando el usuario solicita, entonces el sistema
    produce el informe agregando productos controlados en ubicación "Vencidos".

FR-BCK-010 El sistema DEBE producir mensualmente el Libro de Control de productos controlados.
  ← functional / Data exports / "Libro de control"
  Regla R4 + Data export: el libro es a la vez exportación (artefacto final) y job mensual.
  Escenario: Dado el cierre mensual, cuando se cumple, entonces el sistema produce el libro
    foliado/timbrado del período para fiscalización.

FR-BCK-011 El sistema DEBE emitir un evento cuando un producto cruza el umbral de stock crítico.
  ← functional / Event triggers / "Cruce de umbral stock crítico → Event Handler"
  Escenario: Dado un producto con umbral configurado, cuando su saldo cae bajo el umbral,
    entonces se emite el evento para que el Event Handler active la alerta al Front.

FR-BCK-012 El sistema DEBE enviar alertas por correo electrónico cuando el Event Handler
  se activa por cruce de umbral o vencimiento próximo.
  ← functional / Helpers / "Servicio envío correo (alertas)"
  Regla R2 (calidad de datos / soporte): el helper se convierte en FR de soporte visible
  por tener contraparte en el Front (`FNC-UV-02` "Alerta urgente en dashboard").
  Escenario: Dado un evento de stock crítico o vencimiento próximo, cuando el Event Handler
    se activa, entonces el sistema envía el correo al destinatario configurado.

FR-BCK-013 El sistema DEBE generar los archivos PDF para Órdenes de Compra, Guías de Despacho
  e Informes de productos controlados.
  ← functional / Helpers / "Servicio generación PDF"
  Regla R2 (soporte): helper al servicio de Data exports (`FR-BCK-007`/`008`/`009`).
  Escenario: Dado un documento emitido, cuando se solicita la versión PDF, entonces el
    sistema lo produce con el formato institucional.

FR-BCK-014 El sistema DEBE ejecutar diariamente la revisión de stock contra los puntos de reorden.
  ← functional / Jobs / "Job diario revisión stock"
  Escenario: Dado el calendario diario configurado, cuando se cumple la ventana, entonces
    el sistema evalúa cada producto contra su punto de reorden y, si corresponde, emite
    el evento de cruce de umbral.
  [NEEDS CLARIFICATION: periodicidad declarada como "diario" pero sin hora exacta ni
  ventana de tolerancia ante fallo. ¿Se reintenta si la corrida falla?]

FR-BCK-015 El sistema DEBE ejecutar mensualmente la generación del libro de control de productos
  controlados.
  ← functional / Jobs / "Job mensual libro controlados"
  Escenario: Dado el cierre mensual, cuando se cumple la ventana, entonces el sistema
    produce el libro de control del período.
  [NEEDS CLARIFICATION: periodicidad declarada como "mensual" sin día/hora exactos.]

FR-BCK-016 El sistema DEBE ejecutar de forma recurrente el job de vencimientos.
  ← functional / Jobs / "Job vencimientos"
  Escenario: Dado el calendario configurado, cuando se cumple la ventana, entonces el
    sistema identifica productos con vencimiento próximo y, si corresponde, los mueve a
    la ubicación "Vencidos".
  [NEEDS CLARIFICATION: el canvas no declara periodicidad del job de vencimientos — solo
  el nombre "Job vencimientos". Se requiere periodicidad y ventana de ejecución.]

---

## §Constraints heredadas del Architectural Context Canvas

(no del Functional Back, pero declaradas en `com/E1-architectural_context-p2.json`)

- `ACC-TPR-01` "Sistema intuitivo" — el sistema DEBE ser operable por personal no técnico
  (ver `ACC-SC-04` "Personal no técnico operando el sistema").
- `ACC-TPR-02` "Integridad de los registros" — el sistema DEBE preservar la integridad de
  los registros; ver `FR-BCK-003`.
- `ACC-TPR-03` "no alteración de registros de transacciones una vez emitidos" — refuerza
  `FR-BCK-003`.
- `ACC-SC-03` "Los registros de transacciones, una vez emitidos, no se pueden modificar
  ni alterar" — refuerza `FR-BCK-003`.
- `ACC-SC-05` "Autorización ISP y ejecución de destrucción por empresa externa certificada"
  — el sistema DEBE exigir evidencia de autorización ISP y ejecución por empresa certificada
  para `FR-FRO-006` (registro de destrucción).