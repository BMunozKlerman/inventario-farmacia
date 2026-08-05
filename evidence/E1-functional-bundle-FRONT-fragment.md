# Fragmento de `spec.md` — bundle Front (E1, p. 5)

> **Origen:** `com/E1-functional-p5.json` (header.canvas = "Functional Canvas Front")
> **Prefijo aplicado:** `FRO` (decisión documentada: no existe Structural Canvas formal
> en E1; se usa el identificador del sub-canvas como `bundle.code` provisional).
> **Traza fuente:** 26 post-it (BC=7, UI=6, UPI=3, UV=6, CT=3, API=1).
> **Mapping skill:** `7cs-functional-B` ejecutado sobre el COM de `7cs-functional-A`.

---

## §Key Entities (Front)

El canvas Front **no contiene** una sección `Data objects` (registrada como vacía
en `empty_sections`). Las entidades las emite íntegramente el Back canvas
(`evidence/E1-functional-bundle-BACK-fragment.md`) — este fragmento **no las
duplica**.

---

## §Functional Requirements — bundle Front

FR-FRO-001 El sistema DEBE registrar la recepción de mercadería ingresada por el usuario.
  ← functional / User inputs / "Registro de recepción de mercadería"
  Escenario (feliz): Dado una mercadería recibida con productos, lotes y vencimientos,
    cuando el usuario confirma el registro, entonces la entrada queda persistida con su
    número de guía y los lotes asociados.
  Escenario (error): Dado un producto que no existe en el catálogo, cuando se intenta
    registrar, entonces el sistema rechaza la línea y exige alta previa.

FR-FRO-002 El sistema DEBE permitir al usuario autorizado firmar electrónicamente la guía de recepción.
  ← functional / User inputs / "Autorización y firma de guía de recepción"
  Escenario: Dado un usuario con rol habilitado, cuando registra su firma, entonces la guía
    queda marcada como autorizada y no puede modificarse sin re-firma.

FR-FRO-003 El sistema DEBE permitir al usuario registrar una reposición de inventario.
  ← functional / User inputs / "Registro de reposición"
  Escenario: Dado un producto con ubicación y cantidad definidos, cuando el usuario confirma
    la reposición, entonces el saldo por lote y ubicación queda actualizado.

FR-FRO-004 El sistema DEBE permitir al usuario generar una Orden de Compra (OC).
  ← functional / User inputs / "Generación de OC"
  Escenario: Dado productos candidatos y cantidades sugeridas, cuando el usuario confirma la
    OC, entonces se emite un documento con número, items y proveedor.
  [NEEDS CLARIFICATION: ¿la OC debe considerar las OC pendientes de recepción del mismo
  producto antes de emitir? (post-it declarado en el canvas Back, sección UI-processing inputs).]

FR-FRO-005 El sistema DEBE permitir al usuario registrar un canje de mercadería.
  ← functional / User inputs / "Registro de canje"
  Escenario: Dado un lote a canjear y su contraparte, cuando el usuario confirma, entonces
    se emite una guía de despacho (canje) y el lote original queda marcado como canjeado.

FR-FRO-006 El sistema DEBE permitir al usuario registrar una destrucción de producto controlado.
  ← functional / User inputs / "Registro de destrucción"
  Escenario: Dado un producto controlado y autorización vigente, cuando el usuario confirma,
    entonces se emite una guía de despacho (destrucción) y el lote queda marcado como
    destruido.
  [NEEDS CLARIFICATION: ¿la destrucción requiere adjuntar evidencia (certificado de la
  empresa externa autorizada)?]

FR-FRO-007 El sistema DEBE presentar al usuario un dashboard de stock con marca visual de fila roja
  para los productos con stock crítico.
  ← functional / UI-processing inputs / "Dashboard de stock (fila roja para stock crítico)"
  Escenario: Dado un producto cuyo saldo actual cae bajo el umbral configurado, cuando el
    usuario abre el dashboard, entonces la fila correspondiente aparece en rojo.

FR-FRO-008 El sistema DEBE generar de forma automática un reporte semanal de productos próximos a vencer.
  ← functional / UI-processing inputs / "Reporte semanal de próximos a vencer"
  Escenario: Dado el calendario semanal configurado, cuando se cumple la ventana, entonces
    el reporte queda disponible para consulta y descarga.
  [NEEDS CLARIFICATION: periodicidad no declarada explícitamente — "semanal" es
  inferido del nombre del post-it; falta ventana de ejecución exacta.]

FR-FRO-009 El sistema DEBE permitir al usuario consultar el historial de movimientos por producto y lote.
  ← functional / UI-processing inputs / "Historial de movimientos"
  Escenario: Dado un producto y lote seleccionados, cuando el usuario consulta, entonces
    ve la lista cronológica de movimientos (entradas, salidas, canjes, destrucción).

FR-FRO-010 El sistema DEBE generar de forma automática un reporte mensual de compras.
  ← functional / User visualizations / reports / "Reporte mensual de compras"
  Escenario: Dado el cierre mensual, cuando se cumple, entonces el reporte agrega OCs
    emitidas, confirmadas y recepcionadas durante el período.
  [NEEDS CLARIFICATION: periodicidad no declarada explícitamente — "mensual" es
  inferido del nombre del post-it; falta ventana de ejecución.]

FR-FRO-011 El sistema DEBE mostrar al usuario una alerta urgente visible en el dashboard cuando se
  detecta un evento crítico (stock crítico, vencimiento próximo o falla operativa).
  ← functional / User visualizations / reports / "Alerta urgente en dashboard"
  Escenario: Dado un evento crítico emitido por el Back, cuando se publica, entonces la
    alerta aparece de forma destacada en el dashboard del usuario autorizado.

FR-FRO-012 El sistema DEBE generar una Orden de Compra en formato PDF/Excel descargable.
  ← functional / User visualizations / reports / "PDF/Excel de orden de compra"
  Escenario: Dada una OC emitida, cuando el usuario solicita la descarga, entonces el
    sistema produce el documento en el formato elegido.

FR-FRO-013 El sistema DEBE imprimir la guía de despacho (canje o destrucción) en formato físico foliado.
  ← functional / User visualizations / reports / "Guía de despacho impresa"
  Escenario: Dada una guía de despacho emitida, cuando el usuario solicita la impresión,
    entonces el documento se imprime sobre hoja foliada/timbrada.

FR-FRO-014 El sistema DEBE generar un informe de productos controlados a partir de la información
  registrada.
  ← functional / User visualizations / reports / "Informe de productos controlados"
  Escenario: Dado un período y un conjunto de productos controlados, cuando el usuario
    solicita, entonces el sistema produce el informe con los movimientos del período.

FR-FRO-015 El sistema DEBE mantener el libro de control de productos controlados actualizado
  y disponible para fiscalización.
  ← functional / User visualizations / reports / "Libro de control de productos controlados"
  Escenario: Dado un registro de producto controlado, cuando se confirma, entonces el
    libro refleja la entrada/salida con fecha, lote y responsable.

FR-FRO-016 El sistema DEBE exponer una interfaz web responsiva (SPA) para el usuario de farmacia.
  ← functional / Constraints / "Frontend SPA responsiva"
  Regla R6 (anonimización): el nombre de tecnología "SPA" se traslada a `plan.md`;
  en `spec.md` se describe su función (interfaz web responsiva).
  [NEEDS CLARIFICATION: ¿la SPA cubre exclusivamente usuarios internos (QF, Bodeguero) o
  también al cliente final? El canvas SCC declara QF DT, QF Complementario y Bodeguero
  como únicos Source users.]

FR-FRO-017 El sistema NO DEBE requerir conexión para ejecutar las operaciones de farmacia.
  ← functional / Constraints / "Sin soporte offline"
  Regla R7: restricción externa — el sistema no funciona offline, lo que obliga a un FR
  compensatorio: las operaciones que asumen conexión deben fallar explícitamente y no
  corromper estado.

FR-FRO-018 El sistema DEBE evaluar el cruce del umbral de stock crítico como disparador de
  alerta para el dashboard.
  ← functional / Constraints / "Stock Crítico para Dashboard"
  Escenario: Dado un producto con umbral de stock crítico configurado, cuando su saldo cae
    bajo el umbral, entonces se emite el evento que activa la alerta en el dashboard.
  [NEEDS CLARIFICATION: ¿el umbral se declara por producto, por categoría o global? El
  canvas no lo especifica.]

FR-FRO-019 El sistema DEBE exponer una API REST para que el Frontend Bundle del Front canvas
  reciba peticiones del usuario.
  ← functional / API inputs / "Peticiones hacia el Backend Bundle vía API REST"
  Regla R3 (integración): el nombre del producto ("API REST") se traslada a `plan.md`;
  en `spec.md` se describe la dirección y la contraparte.
  [NEEDS CLARIFICATION: la entrega tiene dos sub-canvas ("Front" y "Back"); el Front declara
  este API hacia el Backend Bundle y el Back declara su contraparte en `FNC-API-01`
  "Peticiones del Frontend Bundle". La asociación Front↔Back como un mismo bundle técnico
  es inferencia del orquestador — no fue declarada en un Structural Canvas formal.]