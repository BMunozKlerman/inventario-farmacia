# Fragmento E1 — functional-front

> Fuente de verdad: COM literal.

## FR-FRT-GENERAL-001

Cita literal: «Registro de recepción de mercadería»

- Dado que la capacidad «Registro de recepción de mercadería» está habilitada
- Cuando un actor o integración autorizada la utiliza
- Entonces el sistema entrega un resultado observable coherente y registra el resultado

## FR-FRT-GENERAL-002

Cita literal: «Autorización y firma de guía de recepción de mercadería»

- Dado que la capacidad «Autorización y firma de guía de recepción de mercadería» está habilitada
- Cuando un actor o integración autorizada la utiliza
- Entonces el sistema entrega un resultado observable coherente y registra el resultado

## FR-FRT-GENERAL-003

Cita literal: «Registro de reposición»

- Dado que la capacidad «Registro de reposición» está habilitada
- Cuando un actor o integración autorizada la utiliza
- Entonces el sistema entrega un resultado observable coherente y registra el resultado

## FR-FRT-GENERAL-004

Cita literal: «Generación de OC (considerando pendientes de recepción)»

- Dado que la capacidad «Generación de OC (considerando pendientes de recepción)» está habilitada
- Cuando un actor o integración autorizada la utiliza
- Entonces el sistema entrega un resultado observable coherente y registra el resultado

## FR-FRT-GENERAL-005

Cita literal: «Registro de destrucción»

- Dado que la capacidad «Registro de destrucción» está habilitada
- Cuando un actor o integración autorizada la utiliza
- Entonces el sistema entrega un resultado observable coherente y registra el resultado

## FR-FRT-GENERAL-006

Cita literal: «Registro de canje»

- Dado que la capacidad «Registro de canje» está habilitada
- Cuando un actor o integración autorizada la utiliza
- Entonces el sistema entrega un resultado observable coherente y registra el resultado

## FR-FRT-GENERAL-007

Cita literal: «Respuestas del Backend Bundle vía API REST»

- Dado que la capacidad «Respuestas del Backend Bundle vía API REST» está habilitada
- Cuando un actor o integración autorizada la utiliza
- Entonces el sistema entrega un resultado observable coherente y registra el resultado

## FR-FRT-GENERAL-008

Cita literal: «Stock Critico para Dashboard»

- Dado que la capacidad «Stock Critico para Dashboard» está habilitada
- Cuando un actor o integración autorizada la utiliza
- Entonces el sistema entrega un resultado observable coherente y registra el resultado

## FR-FRT-GENERAL-009

Cita literal: «Dashboard de stock (fila roja para stock crítico)»

- Dado que la capacidad «Dashboard de stock (fila roja para stock crítico)» está habilitada
- Cuando un actor o integración autorizada la utiliza
- Entonces el sistema entrega un resultado observable coherente y registra el resultado

## FR-FRT-GENERAL-010

Cita literal: «Reporte semanal de próximos a vencer»

- Dado que la capacidad «Reporte semanal de próximos a vencer» está habilitada
- Cuando un actor o integración autorizada la utiliza
- Entonces el sistema entrega un resultado observable coherente y registra el resultado

## FR-FRT-GENERAL-011

Cita literal: «Historial de movimientos por producto/lote»

- Dado que la capacidad «Historial de movimientos por producto/lote» está habilitada
- Cuando un actor o integración autorizada la utiliza
- Entonces el sistema entrega un resultado observable coherente y registra el resultado

## FR-FRT-GENERAL-012

Cita literal: «Reporte mensual de compras»

- Dado que la capacidad «Reporte mensual de compras» está habilitada
- Cuando un actor o integración autorizada la utiliza
- Entonces el sistema entrega un resultado observable coherente y registra el resultado

## FR-FRT-GENERAL-013

Cita literal: «Alerta urgente en dashboard»

- Dado que la capacidad «Alerta urgente en dashboard» está habilitada
- Cuando un actor o integración autorizada la utiliza
- Entonces el sistema entrega un resultado observable coherente y registra el resultado

## FR-FRT-GENERAL-014

Cita literal: «Peticiones hacia el Backend Bundle vía API REST»

- Dado que la capacidad «Peticiones hacia el Backend Bundle vía API REST» está habilitada
- Cuando un actor o integración autorizada la utiliza
- Entonces el sistema entrega un resultado observable coherente y registra el resultado

## FR-FRT-GENERAL-015

Cita literal: «PDF/Excel de orden de compra»

- Dado que la capacidad «PDF/Excel de orden de compra» está habilitada
- Cuando un actor o integración autorizada la utiliza
- Entonces el sistema entrega un resultado observable coherente y registra el resultado

## FR-FRT-GENERAL-016

Cita literal: «Guía de despacho impresa (canje o destrucción)»

- Dado que la capacidad «Guía de despacho impresa (canje o destrucción)» está habilitada
- Cuando un actor o integración autorizada la utiliza
- Entonces el sistema entrega un resultado observable coherente y registra el resultado

## FR-FRT-GENERAL-017

Cita literal: «Informe de productos controlados "Vencidos"»

- Dado que la capacidad «Informe de productos controlados "Vencidos"» está habilitada
- Cuando un actor o integración autorizada la utiliza
- Entonces el sistema entrega un resultado observable coherente y registra el resultado

## FR-FRT-GENERAL-018

Cita literal: «Libro de control de productos controlados»

- Dado que la capacidad «Libro de control de productos controlados» está habilitada
- Cuando un actor o integración autorizada la utiliza
- Entonces el sistema entrega un resultado observable coherente y registra el resultado

## NFR-FRT-001

- Cita literal: «Sin soporte offline»
- Criterio: el resultado debe respetar esta condición y la evidencia aclarada aplicable.

## Aclaraciones resueltas

### Q-TRANS-001

- Pregunta: ¿Qué roles pueden crear, autorizar, firmar, consultar y exportar cada operación de compra, recepción, reposición, canje y destrucción?
- Decisión verificable: Compra: El Bodeguero, Auxiliar de Farmacia, QF Director Técnico y QF Complementario con delegación vigente pueden crear una Orden de Compra en estado Borrador; únicamente el QF Director Técnico y el QF Complementario con delegación vigente pueden autorizarla, emitirla y confirmar sus cambios de estado; la compra no requiere firma electrónica avanzada, pero su emisión exige autenticación personal y confirmación expresa del QF; los cuatro roles pueden consultar y exportar las Órdenes de Compra y reportes operacionales de compras. Recepción: Los cuatro roles pueden crear y registrar la recepción física; únicamente el QF Director Técnico y el QF Complementario con delegación vigente pueden autorizarla y firmarla mediante firma electrónica avanzada; los cuatro roles pueden consultar y exportar recepciones, guías y reportes operacionales asociados. Reposición: Los cuatro roles pueden crear y registrar una reposición; únicamente el QF Director Técnico y el QF Complementario con delegación vigente pueden autorizarla; no requiere firma electrónica avanzada; los cuatro roles pueden consultar y exportar los registros y reportes de reposición. Canje: Los cuatro roles pueden crear una solicitud de canje; únicamente el QF Director Técnico y el QF Complementario con delegación vigente pueden autorizarla y cerrar el proceso; la autorización exige autenticación personal y confirmación expresa, pero no firma electrónica avanzada; los cuatro roles pueden consultar y exportar los registros, documentos y reportes de canje. Destrucción: Los cuatro roles pueden crear una solicitud de destrucción; únicamente el QF Director Técnico y el QF Complementario con delegación vigente pueden efectuar la autorización interna, registrar y validar la autorización del ISP, aprobar la programación con la empresa externa certificada y cerrar el proceso; el cierre exige autenticación personal, confirmación expresa y validación del certificado o acta de destrucción, pero no una firma electrónica avanzada adicional salvo que el documento específico la requiera; los cuatro roles pueden consultar y exportar los antecedentes operacionales de destrucción, mientras que la exportación del libro oficial de productos controlados y de los reportes de auditoría queda reservada al QF Director Técnico y al QF Complementario con delegación vigente. Toda creación, autorización, firma, consulta y exportación deberá quedar registrada en la bitácora de auditoría con usuario, rol, fecha, hora, operación, documento o reporte afectado y resultado de la acción.

### Q-TRANS-002

- Pregunta: ¿Cuál es el contrato de la entrada de transacciones del POS, incluyendo campos obligatorios, identificador único, tipos admitidos, validaciones, errores y regla de reintento/idempotencia?
- Decisión verificable: La entrada de transacciones del POS se realizará mediante el método POST en la ruta /api/v1/pos/transacciones, utilizando HTTPS con TLS 1.2 o superior y contenido JSON UTF-8. Los tipos admitidos serán Venta, Nota de Crédito, Devolución, Reversa Total y Reversa Parcial. Los campos obligatorios de cabecera serán tipoTransaccion, idTransaccionExterna, fechaHoraTransaccion, idEstablecimiento, idLocal, idPOS, idCaja, idOperador, moneda, montoNeto, montoDescuentos, montoImpuestos, montoTotal, idempotencyKey y X-Correlation-ID; cuando corresponda restitución económica, deberá incluir además medioPago o medioDevolucion. Cada línea deberá contener idLineaExterna, codigoMaestroProducto, cantidad, unidadMedida, precioUnitario, descuento, impuesto y montoTotalLinea, además de numeroLote cuando el producto exija trazabilidad. Las Notas de Crédito, Devoluciones y Reversas deberán incluir obligatoriamente idTransaccionOriginal, idLineaOriginal por cada detalle afectado y motivo de la compensación. El identificador único de la operación en el POS será idTransaccionExterna, mientras que el sistema receptor asignará un idTransaccionInterna único e inmutable; la combinación idEstablecimiento, idLocal e idTransaccionExterna no podrá repetirse. La API validará autenticación y permisos, correspondencia de establecimiento, local, POS y caja con las credenciales, tipo de transacción admitido, presencia y formato de campos obligatorios, existencia y habilitación del código maestro del producto, cantidades mayores que cero, unidad de medida válida, consistencia aritmética entre líneas y totales, stock disponible suficiente para ventas y existencia de la transacción original para compensaciones. También validará que cada producto, lote, cantidad y monto compensado pertenezca a la transacción original y no exceda el saldo aún no compensado. La creación exitosa responderá HTTP 201 con idTransaccionInterna, idTransaccionExterna, idempotencyKey, tipoTransaccion, estado Emitida, fechaHoraRegistro, folio cuando corresponda, montos y líneas procesadas; un reintento válido de una operación ya registrada responderá HTTP 200 con la misma respuesta original y sin repetir el efecto sobre el inventario. Los errores mínimos serán HTTP 400 por campos ausentes, formatos inválidos o inconsistencias aritméticas; HTTP 401 por credenciales o token inválido; HTTP 403 por falta de permisos o ámbito no autorizado; HTTP 404 por producto, lote o transacción original inexistente; HTTP 409 por duplicidad, reutilización de idTransaccionExterna, conflicto de idempotencia o estado incompatible; HTTP 422 por stock insuficiente, producto no habilitado, cantidades o montos superiores al saldo compensable o incumplimiento de reglas de negocio; HTTP 429 por exceso de solicitudes; HTTP 500 por error interno; y HTTP 503 por indisponibilidad temporal. Cada error deberá incluir codigoError, mensaje, campoAfectado cuando corresponda, X-Correlation-ID y fechaHora. La regla de idempotencia exigirá que cada solicitud incluya una idempotencyKey única; si se reenvía la misma clave con el mismo contenido normalizado, la API devolverá la respuesta original sin crear una nueva transacción ni afectar nuevamente el inventario; si la misma clave se reutiliza con contenido diferente, responderá HTTP 409 con el código CONFLICTO_IDEMPOTENCIA. Ante errores HTTP 429, 500 o 503, el POS podrá reintentar utilizando exactamente la misma idempotencyKey y el mismo cuerpo; ante errores HTTP 400, 401, 403, 404, 409 o 422, no deberá reintentar sin corregir previamente la causa. Todas las solicitudes, reintentos, respuestas, validaciones y efectos de inventario quedarán registrados en la bitácora de auditoría.

### Q-TRANS-003

- Pregunta: ¿Cuál es el contrato de la consulta de stock del POS, incluyendo identificador de producto, alcance del saldo, respuesta, errores y autenticación?
- Decisión verificable: La consulta de stock del POS se realizará mediante el método GET en la ruta /api/v1/pos/stock/{codigoProducto}, utilizando obligatoriamente como identificador el código maestro institucional del producto y los parámetros idLocal e idUbicacion; para el delivery de un solo local, el alcance corresponderá exclusivamente al inventario de la ubicación habilitada para despacho de ese local, sin consolidar existencias de otras bodegas, locales o establecimientos. El stock disponible se calculará como stock físico menos stock reservado, comprometido, bloqueado y no apto para venta, con resultado mínimo igual a cero; los productos vencidos, en cuarentena, destinados a canje, devolución o destrucción no formarán parte del saldo disponible. Cuando la ubicación consultada sea Vencidos, las unidades se informarán como stock físico y stock no apto para venta, pero el stock disponible será igual a cero y el campo estadoDisponibilidad devolverá únicamente No disponible para venta. La respuesta exitosa HTTP 200 deberá incluir codigoProducto, descripcion, idEstablecimiento, idLocal, idUbicacion, stockFisico, stockReservado, stockComprometido, stockBloqueado, stockNoAptoVenta, stockDisponible, unidadMedida, estadoDisponibilidad, fechaHoraActualizacion y X-Correlation-ID; para productos con trazabilidad deberá incluir además numeroLote, fechaVencimiento y stockDisponibleLote, ordenando los lotes habilitados conforme al criterio FEFO. La ausencia de existencias no será un error y responderá HTTP 200 con stockDisponible igual a cero y estadoDisponibilidad Sin stock, salvo que la ubicación sea Vencidos, caso en que devolverá No disponible para venta. La autenticación se realizará mediante OAuth 2.0 con flujo Client Credentials y token JWT de vigencia máxima de 60 minutos, transmitido por HTTPS en el encabezado Authorization; se exigirá el permiso stock.read y adicionalmente stock.lot.read cuando la respuesta incluya lotes y fechas de vencimiento, y las credenciales limitarán la consulta al establecimiento, local y ubicación autorizados. Los errores mínimos serán HTTP 400 por parámetros obligatorios ausentes o inválidos, HTTP 401 por token ausente, vencido, revocado o inválido, HTTP 403 por falta de permiso o intento de consultar un ámbito no autorizado, HTTP 404 por producto, local o ubicación inexistente, HTTP 409 cuando el producto exista pero no esté habilitado para la ubicación solicitada, HTTP 422 cuando el identificador sea ambiguo o no pueda resolverse al código maestro, HTTP 429 por exceso de solicitudes, HTTP 500 por error interno y HTTP 503 por indisponibilidad temporal; cada error deberá incluir codigoError, mensaje, campoAfectado cuando corresponda, X-Correlation-ID y fechaHora. Todas las consultas, respuestas y errores quedarán registrados en la bitácora de auditoría con cliente, ámbito consultado, fecha y hora y resultado.

### Q-TRANS-004

- Pregunta: ¿Cómo se define y configura el punto de reorden y el umbral de stock crítico para cada producto?
- Decisión verificable: El punto de reorden y el umbral de stock crítico se definirán individualmente para cada producto y ubicación de inventario, expresados como números enteros en la unidad de inventario configurada para el producto, sin utilizar valores globales para todo el catálogo. El umbral de stock crítico corresponderá al stock de seguridad definido por el QF Director Técnico para asegurar la continuidad operacional y su condición se activará cuando el stock disponible sea menor o igual al valor configurado. El punto de reorden se calculará mediante la fórmula Punto de reorden igual a Demanda promedio diaria multiplicada por Plazo de reposición en días más Stock crítico; la Demanda promedio diaria se obtendrá dividiendo el consumo efectivo de los últimos 90 días corridos por 90, y el Plazo de reposición corresponderá a los días corridos transcurridos desde la emisión de la Orden de Compra hasta su recepción, configurados para cada producto y proveedor. El QF Director Técnico será el único rol autorizado para configurar o modificar el stock crítico, el plazo de reposición y los parámetros de cálculo; el sistema recalculará automáticamente el punto de reorden cuando cambie cualquiera de estos valores. Cuando el stock disponible sea menor o igual al punto de reorden, el sistema generará una alerta de reposición y calculará una propuesta de compra considerando el stock disponible y las cantidades pendientes de recepción; cuando el stock disponible sea menor o igual al stock crítico, cambiará el estado del producto a Stock Crítico, mostrará su fila en color rojo y enviará la alerta correspondiente. Toda configuración o modificación deberá registrar código del producto, ubicación, unidad de medida, valor anterior, valor nuevo, motivo, usuario responsable, fecha y hora en la bitácora de auditoría.

### Q-TRANS-005

- Pregunta: ¿Quiénes reciben las alertas por correo y la alerta urgente del dashboard, y bajo qué condición exacta se emite y se considera atendida cada una?
- Decisión verificable: Las alertas por correo electrónico serán enviadas al Bodeguero, al QF Director Técnico y al QF Complementario con delegación vigente, mientras que la alerta urgente del dashboard será visible para estos mismos roles dentro del establecimiento y ubicación afectados. La alerta por correo de Punto de Reorden se emitirá cuando, después de un movimiento de inventario o de la revisión automática diaria, el stock disponible del producto sea menor o igual al punto de reorden configurado y mayor que el umbral de stock crítico; incluirá producto, ubicación, stock disponible, punto de reorden, cantidades pendientes de recepción, fecha y hora, prioridad, acción esperada y vínculo al registro. Esta alerta se considerará atendida cuando el Bodeguero registre una propuesta de reposición o una solicitud de compra vinculada al producto y dicha acción sea validada por el QF Director Técnico o por el QF Complementario con delegación vigente; permanecerá activa mientras no exista una acción registrada o mientras el stock disponible más las cantidades pendientes de recepción continúe siendo menor o igual al punto de reorden. La alerta urgente de Stock Crítico se emitirá inmediatamente cuando el stock disponible pase desde un valor superior a un valor menor o igual al umbral de stock crítico configurado; el sistema marcará la fila del producto en color rojo, mostrará la alerta prioritaria en el dashboard y enviará simultáneamente un correo a los destinatarios definidos. Esta alerta se considerará atendida cuando un usuario autorizado registre una acción de reposición, compra, ajuste o justificación, indicando responsable, fecha, hora y observación; sin embargo, solo se cerrará automáticamente cuando el stock disponible aumente por sobre el umbral de stock crítico. Si la acción queda registrada pero el stock continúa en nivel crítico, la alerta permanecerá visible con estado Atendida Pendiente de Normalización. El sistema no generará alertas duplicadas mientras el producto permanezca continuamente bajo el mismo umbral y solo emitirá una nueva alerta después de que el stock se normalice y vuelva a cruzar posteriormente el límite configurado. Todas las emisiones, recepciones, atenciones, cierres y reaperturas quedarán registradas en la bitácora de auditoría.

### Q-TRANS-006

- Pregunta: ¿Con qué periodicidad exacta se ejecuta el job de vencimientos y qué regla temporal define que un producto está «próximo a vencer»?
- Decisión verificable: El job de vencimientos se ejecutará automáticamente todos los días a las 00:00 horas utilizando la zona horaria America/Santiago. En cada ejecución revisará todos los lotes activos del inventario y calculará los días corridos restantes entre la fecha de ejecución y la fecha de vencimiento registrada para cada lote. Un producto o lote se clasificará como Próximo a Vencer cuando resten 90 días corridos o menos para su fecha de vencimiento y dicha fecha aún no haya sido alcanzada; cuando se alcance la fecha de vencimiento, cambiará automáticamente a estado Vencido, quedará excluido del stock disponible para venta o dispensación y será trasladado lógicamente a la condición de stock no apto para venta. Si una ejecución diaria no pudiera completarse por indisponibilidad del sistema, se ejecutará automáticamente al restablecerse el servicio, garantizando una única ejecución exitosa por día calendario. Cada ejecución registrará fecha y hora programada, fecha y hora efectiva, zona horaria, lotes evaluados, cambios de estado, alertas generadas y resultado en la bitácora de auditoría.

### Q-TRANS-007

- Pregunta: ¿Qué datos, formato, orden y criterio de cierre debe contener el libro mensual de productos controlados para poder validarlo?
- Decisión verificable: El libro mensual de productos controlados deberá generarse en formato PDF no editable y contener, en el siguiente orden, número correlativo del movimiento, fecha y hora, código maestro del producto, descripción del producto, concentración, forma farmacéutica, número de lote, fecha de vencimiento, tipo de movimiento, tipo y número del documento de respaldo, cantidad de entrada, cantidad de salida, saldo resultante, unidad de medida, establecimiento, bodega o ubicación, usuario responsable de la operación y QF responsable de la autorización; los registros deberán ordenarse primero por código maestro del producto, luego por fecha y hora ascendente y, ante igualdad de fecha y hora, por número correlativo ascendente. Cada página deberá identificar el establecimiento, mes y año del período, número de página y folio correlativo, además de disponer de espacio para timbre y firma del QF Director Técnico. El período corresponderá a un mes calendario y podrá cerrarse únicamente después de finalizado el último día del mes y cuando no existan movimientos pendientes de autorización correspondientes al período; el cierre será ejecutado exclusivamente por el QF Director Técnico mediante la acción Cerrar Libro Mensual. Una vez cerrado, el libro será inmutable y cualquier regularización posterior deberá registrarse como un nuevo movimiento en el período abierto, vinculado al movimiento original. Para considerarse válido, el libro deberá contener el 100 por ciento de los movimientos del período, mantener la continuidad de los saldos, no presentar folios omitidos, duplicados ni discontinuos y conservar un identificador único, fecha y hora de generación, cantidad total de registros, cantidad de páginas y hash SHA-256 del archivo definitivo, quedando el cierre y la generación registrados en la bitácora de auditoría.

### Q-TRANS-008

- Pregunta: ¿Qué campos y formato deben contener la orden de compra, la guía de despacho y el informe de productos controlados exportados o impresos?
- Decisión verificable: La Orden de Compra deberá poder exportarse en PDF y Excel y contener, en este orden, número único de OC, estado, fecha y hora de emisión, establecimiento, razón social y RUT del proveedor, dirección y datos de contacto del proveedor, usuario solicitante, QF autorizador, fecha estimada de entrega, código maestro del producto, descripción, presentación, unidad de medida, cantidad solicitada, precio unitario, descuento, monto neto, impuesto, monto total por línea, monto neto total, impuestos totales, descuentos totales, monto total de la OC, observaciones y documentos relacionados; el PDF deberá incorporar número de página, fecha y hora de generación e identificador único del documento. La Guía de Despacho asociada a una recepción deberá poder visualizarse e imprimirse en PDF y contener número o folio de guía, fecha de emisión, proveedor, RUT del proveedor, número de OC relacionada, fecha y hora de recepción, establecimiento, bodega de destino, código maestro del producto, descripción, número de lote, fecha de vencimiento, unidad de medida, cantidad indicada en la guía, cantidad efectivamente recibida, cantidad aceptada, cantidad rechazada, motivo de diferencia cuando corresponda, usuario receptor, QF que autoriza y firma, identificador de la firma electrónica y estado de la recepción; el PDF deberá incluir número de página, fecha y hora de generación e identificador único del documento. El Informe de Productos Controlados deberá poder exportarse en PDF y Excel y contener período informado, establecimiento, bodega, código maestro del producto, descripción, concentración, forma farmacéutica, número de lote, fecha de vencimiento, stock inicial, total de entradas, total de salidas, ajustes, saldo final, unidad de medida, estado del producto, tipo y número de documentos de respaldo asociados y QF responsable; los registros deberán ordenarse por código maestro del producto, fecha de vencimiento y número de lote en orden ascendente. Los archivos PDF serán no editables y deberán incluir identificador único, período, fecha y hora de generación, usuario generador, número de páginas y hash SHA-256; los archivos Excel deberán mantener las mismas columnas y orden de datos del reporte, sin omitir registros ni totales. Toda generación, exportación e impresión deberá quedar registrada en la bitácora de auditoría con documento, formato, usuario, fecha, hora y resultado.

### Q-TRANS-009

- Pregunta: ¿Qué transiciones de estado están permitidas para una orden de compra, quién ejecuta cada transición y qué ocurre ante una transición inválida?
- Decisión verificable: La Orden de Compra utilizará los estados Borrador, Emitida, Enviada, Confirmada por Proveedor, Recepcionada Parcialmente, Recepcionada, Anulada y Cerrada. La transición Borrador a Emitida será ejecutada únicamente por el QF Director Técnico o por el QF Complementario con delegación vigente, previa validación de los campos obligatorios y confirmación expresa; la transición Emitida a Enviada será ejecutada por estos mismos roles una vez registrado el envío de la OC al proveedor; la transición Enviada a Confirmada por Proveedor será registrada por el QF Director Técnico o QF Complementario con delegación vigente cuando exista evidencia de aceptación del proveedor; la transición Confirmada por Proveedor a Recepcionada Parcialmente se producirá cuando el Bodeguero, Auxiliar de Farmacia, QF Director Técnico o QF Complementario con delegación vigente registre una recepción por una cantidad inferior a la pendiente y esta sea autorizada por un QF; desde Recepcionada Parcialmente podrá mantenerse el mismo estado ante nuevas recepciones parciales mientras existan cantidades pendientes y pasará a Recepcionada cuando la suma de las cantidades aceptadas sea igual a la cantidad total vigente de la OC; la transición Confirmada por Proveedor a Recepcionada se producirá directamente cuando se reciba y autorice la totalidad de las cantidades pendientes; la transición Recepcionada a Cerrada será ejecutada por el QF Director Técnico o QF Complementario con delegación vigente después de verificar que no existan cantidades ni documentos pendientes. La transición a Anulada podrá realizarse desde Borrador, Emitida, Enviada o Confirmada por Proveedor, únicamente con autorización del QF Director Técnico o QF Complementario con delegación vigente; si existen recepciones o movimientos de inventario asociados, estos deberán ser previamente regularizados mediante movimientos compensatorios y nunca eliminados. Anulada y Cerrada serán estados finales y no admitirán nuevas transiciones. Toda transición no definida expresamente será inválida; el sistema deberá impedir el cambio de estado sin modificar la OC ni sus documentos o movimientos relacionados, mostrar el mensaje Transición de estado no permitida y, cuando la operación se realice mediante API, responder HTTP 409 con el código TRANSICION_ESTADO_INVALIDA, informando identificador de la OC, estado actual y estado solicitado. Todas las transiciones exitosas y rechazadas deberán registrarse en la bitácora de auditoría con estado anterior, estado solicitado, usuario, rol, fecha, hora y resultado.

### Q-TRANS-010

- Pregunta: ¿Qué evidencia constituye la autorización y firma de la recepción de mercadería y qué rol debe aportarla?
- Decisión verificable: La autorización y firma de una recepción de mercadería deberá ser aportada exclusivamente por el QF Director Técnico o por el QF Complementario que mantenga una delegación vigente otorgada por el QF Director Técnico. Una vez registrada la recepción física por un usuario habilitado, el QF deberá revisar la Orden de Compra, guía de despacho, proveedor, productos, lotes, fechas de vencimiento, cantidades recibidas, cantidades aceptadas o rechazadas y diferencias registradas, y ejecutar la acción Autorizar y Firmar Recepción mediante su identidad personal autenticada y firma electrónica avanzada. La evidencia verificable estará constituida por el identificador único de la recepción, identificador de la Orden de Compra y guía asociadas, nombre e identificación del QF firmante, rol utilizado, identificador único de la firma, certificado digital empleado, fecha y hora de firma, confirmación expresa de la autorización, hash SHA-256 del documento de recepción firmado y resultado de validación de la firma electrónica. El sistema deberá conservar el documento firmado en formato no editable y verificar su integridad comparando su hash con el protegido por la firma; cualquier modificación posterior deberá invalidar la firma y marcar el documento como Integridad comprometida. Solo después de completar satisfactoriamente la autorización y firma, la recepción pasará al estado Autorizada y las cantidades aceptadas producirán el movimiento definitivo de entrada al inventario. Toda autorización, firma, validación o rechazo deberá quedar registrada en la bitácora de auditoría con usuario, rol, fecha, hora y resultado.

### Q-TRANS-011

- Pregunta: ¿Qué campos obligatorios y reglas de validación tienen Producto, Lote, Movimiento de inventario, Guía de despacho e Informe de productos controlados?
- Decisión verificable: Producto deberá registrar obligatoriamente código maestro institucional único, descripción, categoría, unidad de inventario, presentación, concentración y forma farmacéutica cuando correspondan, fabricante o laboratorio, condición de producto controlado, exigencia de trazabilidad por lote, estado activo o inactivo, stock crítico y parámetros de punto de reorden; el sistema validará que el código maestro no esté duplicado, que la descripción y unidad estén informadas, que los umbrales sean enteros iguales o mayores que cero, que el stock crítico no supere el punto de reorden y que un producto inactivo no pueda utilizarse en nuevas operaciones. Lote deberá registrar identificador interno único, código maestro del producto, número de lote del fabricante, proveedor, fecha de recepción, fecha de vencimiento, cantidad inicial, cantidad disponible, unidad de medida, establecimiento, bodega o ubicación y estado; se validará que el producto exista y esté activo, que la combinación de producto, lote, proveedor, vencimiento y ubicación no esté duplicada, que la fecha de vencimiento sea posterior a la recepción, que las cantidades no sean negativas y que los lotes vencidos, bloqueados, en cuarentena, destinados a canje o pendientes de destrucción no formen parte del stock disponible. Movimiento de inventario deberá registrar identificador único, tipo de movimiento, fecha y hora, código maestro del producto, lote cuando corresponda, cantidad, unidad de medida, establecimiento, ubicación de origen, ubicación de destino cuando aplique, documento de respaldo, identificador de la transacción relacionada, motivo, usuario responsable, estado, saldo anterior y saldo resultante; se validará que el producto, lote y ubicaciones existan y estén habilitados, que la cantidad sea mayor que cero, que exista stock suficiente para las salidas, que origen y destino sean diferentes en transferencias, que la unidad corresponda al maestro del producto, que el documento no se reutilice para duplicar el mismo movimiento y que ajustes, canjes y destrucciones incluyan autorización y motivo. Guía de despacho deberá registrar número o folio único, fecha de emisión, proveedor y RUT, Orden de Compra relacionada, establecimiento, bodega de destino, fecha y hora de recepción, código maestro y descripción de cada producto, lote, fecha de vencimiento, cantidad indicada, cantidad recibida, cantidad aceptada, cantidad rechazada, unidad de medida, motivo de diferencia, usuario receptor, QF autorizador, estado y documento digitalizado; se validará que la Orden de Compra exista y admita recepción, que el proveedor coincida, que el folio no esté duplicado para el mismo proveedor, que los productos pertenezcan a la orden, que las cantidades aceptadas y rechazadas no superen las recibidas, que las cantidades acumuladas no excedan lo pendiente sin autorización expresa y que lotes y vencimientos sean válidos. Informe de productos controlados deberá registrar período, establecimiento, bodega, código maestro, descripción, concentración, forma farmacéutica, lote, fecha de vencimiento, stock inicial, entradas, salidas, ajustes, saldo final, unidad de medida, estado, documentos de respaldo y QF responsable; se validará que el período esté definido, que incluya la totalidad de los movimientos de productos controlados, que no existan registros duplicados, que el saldo final sea igual al stock inicial más entradas más ajustes positivos menos salidas menos ajustes negativos, que los documentos y movimientos sean trazables y que los totales coincidan con el inventario al cierre. Todas las altas, modificaciones, validaciones, rechazos y movimientos deberán quedar registrados en la bitácora de auditoría con usuario, rol, fecha, hora, valores anteriores y nuevos y resultado de la operación.

### Q-TRANS-012

- Pregunta: ¿Qué criterio verificable determina que la web es «intuitiva» para personal no técnico?
- Decisión verificable: La web se considerará intuitiva para personal no técnico cuando supere una prueba formal de usabilidad realizada con 10 usuarios representativos de los perfiles QF Director Técnico, QF Complementario, Auxiliar de Farmacia y Bodeguero, sin conocimientos técnicos de administración o desarrollo del sistema. Cada participante deberá ejecutar sin asistencia las tareas de iniciar sesión, consultar el stock de un producto, localizar un lote, registrar una recepción, realizar una reposición, crear una Orden de Compra en borrador, consultar productos próximos a vencer y generar un reporte. El criterio de aceptación será que al menos el 90 por ciento de los participantes complete correctamente el 100 por ciento de las tareas, sin intervención del evaluador, con un tiempo promedio máximo de 3 minutos por tarea y una tasa máxima de errores del 5 por ciento. Se considerará error toda acción que produzca un resultado distinto al objetivo de la tarea, ingreso inválido provocado por falta de comprensión de la interfaz, navegación hacia una función incorrecta o necesidad de retroceder por selección equivocada. La evidencia de la prueba deberá registrar para cada participante su perfil, tarea realizada, resultado exitoso o fallido, tiempo empleado, cantidad y tipo de errores, solicitudes de asistencia y observaciones; el sistema solo cumplirá el criterio de interfaz intuitiva cuando alcance simultáneamente los umbrales de éxito, tiempo y tasa de errores definidos.

### Q-TRANS-013

- Pregunta: ¿Cómo se identifican y descuentan las órdenes pendientes de recepción al calcular una nueva orden de compra?
- Decisión verificable: Las órdenes pendientes de recepción se identificarán por código maestro de producto y corresponderán a todas las líneas del mismo producto incluidas en Órdenes de Compra en estado Emitida, Enviada, Confirmada por Proveedor o Recepcionada Parcialmente que mantengan unidades aún no recepcionadas; para cada línea, la cantidad pendiente se calculará como Cantidad pendiente de recepción igual a Cantidad ordenada menos Cantidad efectivamente recepcionada y aceptada, y la Cantidad pendiente total del producto será la suma de las cantidades pendientes de todas las Órdenes de Compra vigentes del mismo producto, expresadas en su unidad de inventario. Las Órdenes de Compra en estado Borrador, Anulada, Recepcionada totalmente o Cerrada no se incluirán en el cálculo. Al calcular una nueva Orden de Compra, la cantidad sugerida se determinará como Cantidad sugerida igual al máximo entre cero y Stock objetivo menos Stock disponible menos Cantidad pendiente total de recepción; adicionalmente, la generación de una propuesta de compra solo se activará cuando la suma del Stock disponible más la Cantidad pendiente total de recepción sea menor o igual al Punto de reorden del producto. En una recepción parcial solo se descontará de la cantidad pendiente la cantidad efectivamente recibida y aceptada, manteniéndose el saldo restante como pendiente hasta su recepción, anulación o cierre. Antes de generar la nueva Orden de Compra, el sistema deberá mostrar el código del producto, Stock disponible, Stock objetivo, Punto de reorden, identificadores de las Órdenes de Compra pendientes consideradas, cantidad ordenada, cantidad recepcionada, saldo pendiente de cada una, Cantidad pendiente total y Cantidad sugerida final, permitiendo verificar que las unidades ya solicitadas no sean compradas nuevamente.

### Q-TRANS-014

- Pregunta: ¿Qué pasos, responsables y evidencia verificable autorizan y confirman la destrucción de productos controlados por la empresa externa certificada?
- Decisión verificable: La destrucción de productos controlados seguirá los estados Solicitada, Autorizada por QF, Autorizada por ISP, Programada, Destruida y Cerrada; en Solicitada, el Bodeguero o Auxiliar de Farmacia registrará código maestro del producto, lote, cantidad, causal, ubicación y documentos de respaldo, quedando las unidades bloqueadas y excluidas del stock disponible pero manteniéndose en el stock físico; en Autorizada por QF, el QF Director Técnico o el QF Complementario con delegación vigente revisará y aprobará la solicitud mediante autenticación personal y confirmación expresa; en Autorizada por ISP se deberá registrar identificador o folio de la autorización, fecha de emisión, vigencia, establecimiento, productos, lotes, cantidades autorizadas y copia del documento emitido por el ISP, validándose que coincida con la solicitud; en Programada, el QF autorizador registrará la empresa externa certificada mediante razón social, RUT, identificación de su certificación o autorización, entidad emisora, vigencia, fecha y lugar programados para la destrucción, conservando el documento que acredite su habilitación; en Destruida, una vez ejecutada físicamente la destrucción, se deberá incorporar obligatoriamente el certificado o acta emitido por la empresa externa indicando identificador del proceso, fecha y hora, lugar, método utilizado, productos, lotes, cantidades efectivamente destruidas, identificación de la empresa y responsable que certifica la ejecución, y en este momento exacto se descontarán las unidades del stock físico mediante un movimiento Salida por Destrucción; finalmente, en Cerrada, el QF Director Técnico o QF Complementario con delegación vigente deberá verificar la autorización vigente del ISP, la certificación de la empresa externa, el acta o certificado de ejecución, la coincidencia entre productos, lotes y cantidades autorizadas y destruidas y el movimiento de inventario generado, registrando su confirmación final. El sistema no permitirá cerrar el proceso si falta alguna evidencia, existe una diferencia no justificada o la cantidad destruida supera la autorizada, y conservará como evidencia verificable la solicitud, autorizaciones, documentos del ISP, acreditación de la empresa, certificado o acta de destrucción, movimiento de inventario, identidad de los responsables, fechas, horas y cambios de estado en la bitácora de auditoría.

