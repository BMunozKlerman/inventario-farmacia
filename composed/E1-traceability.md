# Anexo de trazabilidad E1

| sticky_id | canvas | sección | regla | destino | target_id | texto literal |
|---|---|---|---|---|---|---|
| ACC-ST-01 | architectural_context | Stakeholders | contexto | fragment | CTX-ARCHITECTURAL_CONTEXT-001 | QF DT |
| ACC-ST-02 | architectural_context | Stakeholders | contexto | fragment | CTX-ARCHITECTURAL_CONTEXT-002 | QF Complementario |
| ACC-ST-03 | architectural_context | Stakeholders | contexto | fragment | CTX-ARCHITECTURAL_CONTEXT-003 | Auxiliar de Farmacia |
| ACC-ST-04 | architectural_context | Stakeholders | contexto | fragment | CTX-ARCHITECTURAL_CONTEXT-004 | Bodeguero |
| ACC-ST-05 | architectural_context | Stakeholders | contexto | fragment | CTX-ARCHITECTURAL_CONTEXT-005 | Laboratorio / Droguería |
| ACC-ST-06 | architectural_context | Stakeholders | contexto | fragment | CTX-ARCHITECTURAL_CONTEXT-006 | SEREMI |
| ACC-ST-07 | architectural_context | Stakeholders | contexto | fragment | CTX-ARCHITECTURAL_CONTEXT-007 | ISP |
| ACC-ST-08 | architectural_context | Stakeholders | contexto | fragment | CTX-ARCHITECTURAL_CONTEXT-008 | Cliente |
| ACC-ST-09 | architectural_context | Stakeholders | contexto | fragment | CTX-ARCHITECTURAL_CONTEXT-009 | MINSAL |
| ACC-ST-10 | architectural_context | Stakeholders | contexto | fragment | CTX-ARCHITECTURAL_CONTEXT-010 | Empresa externa certificada (destrucción de productos controlados) |
| ACC-BS-01 | architectural_context | Business strategy | contexto | fragment | CTX-ARCHITECTURAL_CONTEXT-011 | Resolver el problema de inventario |
| ACC-BS-02 | architectural_context | Business strategy | contexto | fragment | CTX-ARCHITECTURAL_CONTEXT-012 | Prevenir Quiebre de Stock |
| ACC-BS-03 | architectural_context | Business strategy | contexto | fragment | CTX-ARCHITECTURAL_CONTEXT-013 | Minimizar Merma |
| ACC-IT-01 | architectural_context | IT strategy | decision_de_plan | plan_context | PLAN-ARCHITECTURAL_CONTEXT-014 | Plataforma web responsivo |
| ACC-IT-02 | architectural_context | IT strategy | decision_de_plan | plan_context | PLAN-ARCHITECTURAL_CONTEXT-015 | Integración con el POS |
| ACC-BG-01 | architectural_context | Business goals & drivers | restriccion | fragment | NFR-ARCHITECTURAL_CONTEXT-001 | Reducción de pérdidas económicas por merma |
| ACC-BG-02 | architectural_context | Business goals & drivers | restriccion | fragment | NFR-ARCHITECTURAL_CONTEXT-002 | Maximización de ventas disponibles |
| ACC-BG-03 | architectural_context | Business goals & drivers | restriccion | fragment | NFR-ARCHITECTURAL_CONTEXT-003 | Eficiencia operativa |
| ACC-TG-01 | architectural_context | Technology goals & drivers | decision_de_plan | plan_context | PLAN-ARCHITECTURAL_CONTEXT-016 | Reducir errores derivados del registro manual/paralelo |
| ACC-TG-02 | architectural_context | Technology goals & drivers | decision_de_plan | plan_context | PLAN-ARCHITECTURAL_CONTEXT-017 | Eliminar la doble digitación entre POS e inventario |
| ACC-BP-01 | architectural_context | Business standards & policies | restriccion | fragment | NFR-ARCHITECTURAL_CONTEXT-004 | Norma Técnica N°147 |
| ACC-BP-02 | architectural_context | Business standards & policies | restriccion | fragment | NFR-ARCHITECTURAL_CONTEXT-005 | Decreto Supremo N°404, 405, 466 |
| ACC-BP-03 | architectural_context | Business standards & policies | restriccion | fragment | NFR-ARCHITECTURAL_CONTEXT-006 | Exigencia del ISP de llevar libro de control físico para productos controlados |
| ACC-BP-04 | architectural_context | Business standards & policies | restriccion | fragment | NFR-ARCHITECTURAL_CONTEXT-007 | Fiscalización y normativa aplicada por MINSAL, SEREMI, ISP |
| ACC-BP-05 | architectural_context | Business standards & policies | restriccion | fragment | NFR-ARCHITECTURAL_CONTEXT-008 | Autorización ISP de destrucción de productos controlados |
| ACC-TP-01 | architectural_context | Technology standards & policies | decision_de_plan | plan_context | PLAN-ARCHITECTURAL_CONTEXT-018 | APIs para que el POS registre transacciones (venta, notas de crédito, entre otras) y consulta stock disponible |
| ACC-SC-01 | architectural_context | Situational constraints | restriccion | fragment | NFR-ARCHITECTURAL_CONTEXT-009 | Un solo local |
| ACC-SC-02 | architectural_context | Situational constraints | restriccion | fragment | NFR-ARCHITECTURAL_CONTEXT-010 | Sin integración con proveedores externos |
| ACC-SC-03 | architectural_context | Situational constraints | restriccion | fragment | NFR-ARCHITECTURAL_CONTEXT-011 | Los registros de transacciones, una vez emitidos, no se pueden modificar ni alterar |
| ACC-SC-04 | architectural_context | Situational constraints | restriccion | fragment | NFR-ARCHITECTURAL_CONTEXT-012 | Personal no técnico operando el sistema. |
| ACC-SC-05 | architectural_context | Situational constraints | restriccion | fragment | NFR-ARCHITECTURAL_CONTEXT-013 | Autorización ISP y ejecución de destrucción por empresa externa certificada |
| ACC-BPR-01 | architectural_context | Business principles | restriccion | fragment | NFR-ARCHITECTURAL_CONTEXT-014 | Trazabilidad completa de los productos |
| ACC-TPR-01 | architectural_context | Technical principles | decision_de_plan | plan_context | PLAN-ARCHITECTURAL_CONTEXT-019 | Sistema intuitivo |
| ACC-TPR-02 | architectural_context | Technical principles | decision_de_plan | plan_context | PLAN-ARCHITECTURAL_CONTEXT-020 | Integridad de los registros |
| ACC-TPR-03 | architectural_context | Technical principles | decision_de_plan | plan_context | PLAN-ARCHITECTURAL_CONTEXT-021 | no alteración de registros de transacciones una vez emitidos. |
| BUS-BPS-01 | business_context | Business products & services | contexto | fragment | CTX-BUSINESS_CONTEXT-001 | Productos farmacológicos (medicamentos) |
| BUS-BPS-02 | business_context | Business products & services | contexto | fragment | CTX-BUSINESS_CONTEXT-002 | Vitaminas |
| BUS-BPS-03 | business_context | Business products & services | contexto | fragment | CTX-BUSINESS_CONTEXT-003 | Suplementos alimenticios |
| BUS-BPS-04 | business_context | Business products & services | contexto | fragment | CTX-BUSINESS_CONTEXT-004 | Insumos médicos |
| BUS-BPS-05 | business_context | Business products & services | contexto | fragment | CTX-BUSINESS_CONTEXT-005 | Dispensación de medicamentos con receta |
| BUS-BPS-06 | business_context | Business products & services | contexto | fragment | CTX-BUSINESS_CONTEXT-006 | Asesoría farmacológica a clientes |
| BUS-BUA-01 | business_context | Business units & actors | contexto | fragment | CTX-BUSINESS_CONTEXT-007 | Farmacia (unidad de negocio) |
| BUS-BUA-02 | business_context | Business units & actors | contexto | fragment | CTX-BUSINESS_CONTEXT-008 | Cliente (comprador final) |
| BUS-BUA-03 | business_context | Business units & actors | contexto | fragment | CTX-BUSINESS_CONTEXT-009 | Laboratorio (fabricante) |
| BUS-BUA-04 | business_context | Business units & actors | contexto | fragment | CTX-BUSINESS_CONTEXT-010 | Droguería (distribuidor mayorista intermedio) |
| BUS-BUA-05 | business_context | Business units & actors | contexto | fragment | CTX-BUSINESS_CONTEXT-011 | SEREMI de Salud (autoridad sanitaria regional) |
| BUS-BUA-06 | business_context | Business units & actors | contexto | fragment | CTX-BUSINESS_CONTEXT-012 | ISP (Instituto de Salud Pública) |
| BUS-BUA-07 | business_context | Business units & actors | contexto | fragment | CTX-BUSINESS_CONTEXT-013 | Empresa externa certificada (destrucción de productos controlados) |
| BUS-BUA-08 | business_context | Business units & actors | contexto | fragment | CTX-BUSINESS_CONTEXT-014 | MINSAL |
| BUS-BR-01 | business_context | Business roles | contexto | fragment | CTX-BUSINESS_CONTEXT-015 | QF Director Técnico (QF DT) |
| BUS-BR-02 | business_context | Business roles | contexto | fragment | CTX-BUSINESS_CONTEXT-016 | QF Complementario |
| BUS-BR-03 | business_context | Business roles | contexto | fragment | CTX-BUSINESS_CONTEXT-017 | Auxiliar de Farmacia (AF) |
| BUS-BR-04 | business_context | Business roles | contexto | fragment | CTX-BUSINESS_CONTEXT-018 | Bodeguero |
| BUS-BO-01 | business_context | Business objects | entidad | fragment | ENT-BUSINESS_CONTEXT-001 | Producto (con lote, vencimiento, categoría, condición de controlado) |
| BUS-BO-02 | business_context | Business objects | entidad | fragment | ENT-BUSINESS_CONTEXT-002 | Receta médica |
| BUS-BO-03 | business_context | Business objects | entidad | fragment | ENT-BUSINESS_CONTEXT-003 | Orden de compra (estados: emitida, enviada, confirmada por proveedor, recepcionada) |
| BUS-BO-04 | business_context | Business objects | entidad | fragment | ENT-BUSINESS_CONTEXT-004 | Informe/registro de destrucción de productos controlados |
| BUS-BO-05 | business_context | Business objects | entidad | fragment | ENT-BUSINESS_CONTEXT-005 | Registro de movimiento de inventario (venta, compra, nota de crédito, canje, destrucción) |
| BUS-BO-06 | business_context | Business objects | entidad | fragment | ENT-BUSINESS_CONTEXT-006 | Boleta de venta |
| BUS-BO-07 | business_context | Business objects | entidad | fragment | ENT-BUSINESS_CONTEXT-007 | Guía de despacho (canje o destrucción) |
| BUS-BP-01 | business_context | Business processes | contexto | fragment | CTX-BUSINESS_CONTEXT-019 | Compra/reabastecimiento: orden de compra según puntos de stock |
| BUS-BP-02 | business_context | Business processes | contexto | fragment | CTX-BUSINESS_CONTEXT-020 | Recepción de mercadería |
| BUS-BP-03 | business_context | Business processes | contexto | fragment | CTX-BUSINESS_CONTEXT-021 | Dispensación / venta |
| BUS-BP-04 | business_context | Business processes | contexto | fragment | CTX-BUSINESS_CONTEXT-022 | Gestión de vencimientos: canje o destrucción |
| BUS-BP-05 | business_context | Business processes | contexto | fragment | CTX-BUSINESS_CONTEXT-023 | Reposición (bodega -> sala de venta) |
| BUS-BP-06 | business_context | Business processes | contexto | fragment | CTX-BUSINESS_CONTEXT-024 | Inventario |
| BUS-BF-01 | business_context | Business functions | contexto | fragment | CTX-BUSINESS_CONTEXT-025 | Custodia y control de medicamentos |
| BUS-BF-02 | business_context | Business functions | contexto | fragment | CTX-BUSINESS_CONTEXT-026 | Asesoría/atención farmacológica |
| BUS-BIE-01 | business_context | Business infrastructure & equipment | contexto | fragment | CTX-BUSINESS_CONTEXT-027 | Sistema POS (registra venta, pago e IVA, emite boleta) |
| BUS-BIE-02 | business_context | Business infrastructure & equipment | contexto | fragment | CTX-BUSINESS_CONTEXT-028 | Un computador por Auxiliar de Farmacia |
| BUS-BIE-03 | business_context | Business infrastructure & equipment | contexto | fragment | CTX-BUSINESS_CONTEXT-029 | Un computador compartido para los 2 QF |
| BUS-BIE-04 | business_context | Business infrastructure & equipment | contexto | fragment | CTX-BUSINESS_CONTEXT-030 | Tablet o celular para el Bodeguero |
| BUS-BIE-05 | business_context | Business infrastructure & equipment | contexto | fragment | CTX-BUSINESS_CONTEXT-031 | Registros de inventario en papel impreso y hojas de cálculos |
| BUS-BL-01 | business_context | Business locations | contexto | fragment | CTX-BUSINESS_CONTEXT-032 | Un único local |
| BUS-BFA-01 | business_context | Business facilities | contexto | fragment | CTX-BUSINESS_CONTEXT-033 | Bodega |
| BUS-BFA-02 | business_context | Business facilities | contexto | fragment | CTX-BUSINESS_CONTEXT-034 | Sala de venta |
| BUS-BFA-03 | business_context | Business facilities | contexto | fragment | CTX-BUSINESS_CONTEXT-035 | Ubicación física "Vencidos" |
| BUS-SFA-01 | business_context | System’s functional areas | contexto | fragment | CTX-BUSINESS_CONTEXT-036 | Gestión de productos y stock |
| BUS-SFA-02 | business_context | System’s functional areas | contexto | fragment | CTX-BUSINESS_CONTEXT-037 | Gestión de entradas y salidas |
| BUS-SFA-03 | business_context | System’s functional areas | contexto | fragment | CTX-BUSINESS_CONTEXT-038 | Gestión de compras |
| BUS-SFA-04 | business_context | System’s functional areas | contexto | fragment | CTX-BUSINESS_CONTEXT-039 | Alertas y monitoreo (stock mínimo, vencimientos) |
| BUS-SFA-05 | business_context | System’s functional areas | contexto | fragment | CTX-BUSINESS_CONTEXT-040 | Trazabilidad e historial de movimientos |
| BUS-SFA-06 | business_context | System’s functional areas | contexto | fragment | CTX-BUSINESS_CONTEXT-041 | Gestión de vencimientos: canje y destrucción de productos |
| BUS-SFA-07 | business_context | System’s functional areas | contexto | fragment | CTX-BUSINESS_CONTEXT-042 | Generación de libro de control de controlados |
| DEP-ENV-01 | deployment | Environments | decision_de_plan | plan_context | PLAN-DEPLOYMENT-001 | Desarrollo |
| DEP-ENV-02 | deployment | Environments | decision_de_plan | plan_context | PLAN-DEPLOYMENT-002 | Producción |
| DEP-BUN-01 | deployment | Bundles | decision_de_plan | plan_context | PLAN-DEPLOYMENT-003 | Frontend: SPA (aplicación web con diseño responsivo) |
| DEP-BUN-02 | deployment | Bundles | decision_de_plan | plan_context | PLAN-DEPLOYMENT-004 | Backend: monolito (Node.js) |
| DEP-MID-01 | deployment | Middleware | decision_de_plan | plan_context | PLAN-DEPLOYMENT-005 | Cloud SQL for PostgreSQL |
| DEP-RUN-01 | deployment | Runtime | decision_de_plan | plan_context | PLAN-DEPLOYMENT-006 | Node.js |
| DEP-OS-01 | deployment | Orchestration & scheduling | decision_de_plan | plan_context | PLAN-DEPLOYMENT-007 | Cloud Run (backend) |
| DEP-OS-02 | deployment | Orchestration & scheduling | decision_de_plan | plan_context | PLAN-DEPLOYMENT-008 | Cloud Scheduler (Jobs) |
| DEP-CR-01 | deployment | Container runtimes | decision_de_plan | plan_context | PLAN-DEPLOYMENT-009 | Docker |
| DEP-CR-02 | deployment | Container runtimes | decision_de_plan | plan_context | PLAN-DEPLOYMENT-010 | GCP: Cloud Run, Cloud SQL, Cloud Scheduler, Cloud Storage |
| DEP-NET-01 | deployment | Networks | decision_de_plan | plan_context | PLAN-DEPLOYMENT-011 | Acceso vía HTTPS |
| DEP-INS-01 | deployment | Installation | decision_de_plan | plan_context | PLAN-DEPLOYMENT-012 | Despliegue en GCP a cargo del equipo de desarrollo/implementación |
| DEP-OPE-01 | deployment | Operation | decision_de_plan | plan_context | PLAN-DEPLOYMENT-013 | Soporte y operación en producción a cargo de personal de soporte del cliente |
| DEP-CON-01 | deployment | Constraints | restriccion | fragment | NFR-DEPLOYMENT-001 | Inmutabilidad de registros de transacciones |
| DEP-CON-02 | deployment | Constraints | restriccion | fragment | NFR-DEPLOYMENT-002 | Sin soporte offline |
| FNC-BCK-BC-01 | functional | Bundles & components | decision_de_plan | plan_context | PLAN-FUNCTIONAL-BACK-001 | Compras |
| FNC-BCK-BC-02 | functional | Bundles & components | decision_de_plan | plan_context | PLAN-FUNCTIONAL-BACK-002 | Recepción de Mercadería |
| FNC-BCK-BC-03 | functional | Bundles & components | decision_de_plan | plan_context | PLAN-FUNCTIONAL-BACK-003 | Reposición |
| FNC-BCK-BC-04 | functional | Bundles & components | decision_de_plan | plan_context | PLAN-FUNCTIONAL-BACK-004 | Inventario (stock, lotes, ubicaciones) |
| FNC-BCK-BC-05 | functional | Bundles & components | decision_de_plan | plan_context | PLAN-FUNCTIONAL-BACK-005 | Control Regulatorio (libro de productos controlados) |
| FNC-BCK-BC-06 | functional | Bundles & components | decision_de_plan | plan_context | PLAN-FUNCTIONAL-BACK-006 | Módulo de Alertas y Notificaciones |
| FNC-BCK-BC-07 | functional | Bundles & components | decision_de_plan | plan_context | PLAN-FUNCTIONAL-BACK-007 | Integración POS Venta |
| FNC-BCK-BC-08 | functional | Bundles & components | decision_de_plan | plan_context | PLAN-FUNCTIONAL-BACK-008 | Vencimientos (canje/destrucción) |
| FNC-BCK-AI-01 | functional | API inputs | requisito_funcional | fragment | FR-BCK-GENERAL-001 | Registro de transacciones desde el POS |
| FNC-BCK-AI-02 | functional | API inputs | requisito_funcional | fragment | FR-BCK-GENERAL-002 | Peticiones del Frontend Bundle |
| FNC-BCK-DO-01 | functional | Data objects | entidad | fragment | ENT-BCK-001 | Producto (categoría, controlado: sí/no) |
| FNC-BCK-DO-02 | functional | Data objects | entidad | fragment | ENT-BCK-002 | Lote (número, vencimiento, saldo) |
| FNC-BCK-DO-03 | functional | Data objects | entidad | fragment | ENT-BCK-003 | Informe de productos controlados en "Vencidos" |
| FNC-BCK-DO-04 | functional | Data objects | entidad | fragment | ENT-BCK-004 | Guía de despacho (canje o destrucción) |
| FNC-BCK-DO-05 | functional | Data objects | entidad | fragment | ENT-BCK-005 | Movimiento de inventario (lote, vencimiento, saldo, ubicación) |
| FNC-BCK-DO-06 | functional | Data objects | entidad | fragment | ENT-BCK-006 | Tipo de Movimiento de inventario (venta, compra, nota de crédito, canje, destrucción) |
| FNC-BCK-DO-07 | functional | Data objects | entidad | fragment | ENT-BCK-007 | Orden de Compra (estados: emitida, enviada, confirmada por proveedor, recepcionada) |
| FNC-BCK-AO-01 | functional | API outputs | requisito_funcional | fragment | FR-BCK-GENERAL-003 | Consulta de stock disponible por producto (POS) |
| FNC-BCK-DE-01 | functional | Data exports | requisito_funcional | fragment | FR-BCK-GENERAL-004 | PDF/Excel de orden de compra |
| FNC-BCK-DE-02 | functional | Data exports | requisito_funcional | fragment | FR-BCK-GENERAL-005 | Guía de despacho impresa (canje o destrucción) |
| FNC-BCK-DE-03 | functional | Data exports | requisito_funcional | fragment | FR-BCK-GENERAL-006 | Informe de productos controlados "Vencidos" |
| FNC-BCK-DE-04 | functional | Data exports | requisito_funcional | fragment | FR-BCK-GENERAL-007 | Libro de control de productos controlados |
| FNC-BCK-ET-01 | functional | Event triggers | requisito_funcional | fragment | FR-BCK-GENERAL-008 | Cruce de umbral de stock crítico → Event Handler |
| FNC-BCK-H-01 | functional | Helpers | requisito_funcional | fragment | FR-BCK-GENERAL-009 | Servicio de envío de correo (alertas) |
| FNC-BCK-H-02 | functional | Helpers | requisito_funcional | fragment | FR-BCK-GENERAL-010 | Servicio de generación de PDF (OC, guías, informes) |
| FNC-BCK-J-01 | functional | Jobs | requisito_funcional | fragment | FR-BCK-GENERAL-011 | Job diario - Revisión de Stock vs. punto de reorden → alerta por correo |
| FNC-BCK-J-02 | functional | Jobs | requisito_funcional | fragment | FR-BCK-GENERAL-012 | Job de vencimientos: revisión periódica de productos próximos a vencer → reporte semanal y traslado a "Vencidos" |
| FNC-BCK-J-03 | functional | Jobs | requisito_funcional | fragment | FR-BCK-GENERAL-013 | Job mensual: genera e imprime el libro de control de productos controlados |
| FNC-BCK-C-01 | functional | Constraints | restriccion | fragment | NFR-BCK-001 | Registros de transacciones inmutables una vez emitidos |
| FNC-BCK-C-02 | functional | Constraints | restriccion | fragment | NFR-BCK-002 | Antes de emitir una OC se deben considerar las OC pendientes de recepción del mismo producto |
| FNC-BCK-C-03 | functional | Constraints | restriccion | fragment | NFR-BCK-003 | Descuento de stock real ocurre solo al emitir guía de despacho (canje) o al ejecutar destrucción |
| FNC-BCK-C-04 | functional | Constraints | restriccion | fragment | NFR-BCK-004 | Productos en ubicación "Vencidos" no disponibles para venta ni compra, pero sí cuentan en inventario |
| FNC-BCK-TS-01 | functional | Technology stack | decision_de_plan | plan_context | PLAN-FUNCTIONAL-BACK-009 | Backend: monolito Node.js / DB: PostgreSQL / Infra: GCP |
| FNC-FRT-BC-01 | functional | Bundles & components | decision_de_plan | plan_context | PLAN-FUNCTIONAL-FRONT-001 | Compras |
| FNC-FRT-BC-02 | functional | Bundles & components | decision_de_plan | plan_context | PLAN-FUNCTIONAL-FRONT-002 | Recepción de Mercadería |
| FNC-FRT-BC-03 | functional | Bundles & components | decision_de_plan | plan_context | PLAN-FUNCTIONAL-FRONT-003 | Reposición |
| FNC-FRT-BC-04 | functional | Bundles & components | decision_de_plan | plan_context | PLAN-FUNCTIONAL-FRONT-004 | Inventario (stock, lotes, ubicaciones) |
| FNC-FRT-BC-05 | functional | Bundles & components | decision_de_plan | plan_context | PLAN-FUNCTIONAL-FRONT-005 | Control Regulatorio (libro de productos controlados) |
| FNC-FRT-BC-06 | functional | Bundles & components | decision_de_plan | plan_context | PLAN-FUNCTIONAL-FRONT-006 | Reportes |
| FNC-FRT-BC-07 | functional | Bundles & components | decision_de_plan | plan_context | PLAN-FUNCTIONAL-FRONT-007 | Vencimientos (canje/destrucción) |
| FNC-FRT-UI-01 | functional | User inputs | requisito_funcional | fragment | FR-FRT-GENERAL-001 | Registro de recepción de mercadería |
| FNC-FRT-UI-02 | functional | User inputs | requisito_funcional | fragment | FR-FRT-GENERAL-002 | Autorización y firma de guía de recepción de mercadería |
| FNC-FRT-UI-03 | functional | User inputs | requisito_funcional | fragment | FR-FRT-GENERAL-003 | Registro de reposición |
| FNC-FRT-UI-04 | functional | User inputs | requisito_funcional | fragment | FR-FRT-GENERAL-004 | Generación de OC (considerando pendientes de recepción) |
| FNC-FRT-UI-05 | functional | User inputs | requisito_funcional | fragment | FR-FRT-GENERAL-005 | Registro de destrucción |
| FNC-FRT-UI-06 | functional | User inputs | requisito_funcional | fragment | FR-FRT-GENERAL-006 | Registro de canje |
| FNC-FRT-AI-01 | functional | API inputs | requisito_funcional | fragment | FR-FRT-GENERAL-007 | Respuestas del Backend Bundle vía API REST |
| FNC-FRT-EH-01 | functional | Event handlers | requisito_funcional | fragment | FR-FRT-GENERAL-008 | Stock Critico para Dashboard |
| FNC-FRT-UV-01 | functional | User visualizations, reports & notifications | requisito_funcional | fragment | FR-FRT-GENERAL-009 | Dashboard de stock (fila roja para stock crítico) |
| FNC-FRT-UV-02 | functional | User visualizations, reports & notifications | requisito_funcional | fragment | FR-FRT-GENERAL-010 | Reporte semanal de próximos a vencer |
| FNC-FRT-UV-03 | functional | User visualizations, reports & notifications | requisito_funcional | fragment | FR-FRT-GENERAL-011 | Historial de movimientos por producto/lote |
| FNC-FRT-UV-04 | functional | User visualizations, reports & notifications | requisito_funcional | fragment | FR-FRT-GENERAL-012 | Reporte mensual de compras |
| FNC-FRT-UV-05 | functional | User visualizations, reports & notifications | requisito_funcional | fragment | FR-FRT-GENERAL-013 | Alerta urgente en dashboard |
| FNC-FRT-AO-01 | functional | API outputs | requisito_funcional | fragment | FR-FRT-GENERAL-014 | Peticiones hacia el Backend Bundle vía API REST |
| FNC-FRT-DE-01 | functional | Data exports | requisito_funcional | fragment | FR-FRT-GENERAL-015 | PDF/Excel de orden de compra |
| FNC-FRT-DE-02 | functional | Data exports | requisito_funcional | fragment | FR-FRT-GENERAL-016 | Guía de despacho impresa (canje o destrucción) |
| FNC-FRT-DE-03 | functional | Data exports | requisito_funcional | fragment | FR-FRT-GENERAL-017 | Informe de productos controlados "Vencidos" |
| FNC-FRT-DE-04 | functional | Data exports | requisito_funcional | fragment | FR-FRT-GENERAL-018 | Libro de control de productos controlados |
| FNC-FRT-C-01 | functional | Constraints | restriccion | fragment | NFR-FRT-001 | Sin soporte offline |
| FNC-FRT-TS-01 | functional | Technology stack | decision_de_plan | plan_context | PLAN-FUNCTIONAL-FRONT-008 | Frontend: SPA responsiva |
| STR-DIF-01 | structural | Data input interfaces to frontend bundles | decision_de_plan | plan_context | PLAN-STRUCTURAL-001 | Interfaz web |
| STR-FB-01 | structural | Frontend bundles | decision_de_plan | plan_context | PLAN-STRUCTURAL-002 | Single Page Application (SPA) web con diseño responsivo |
| STR-DOF-01 | structural | Data output interfaces from frontend bundles | decision_de_plan | plan_context | PLAN-STRUCTURAL-003 | UI WEB (SPA) responsiva |
| STR-DIB-01 | structural | Data input interfaces to backend bundles | decision_de_plan | plan_context | PLAN-STRUCTURAL-004 | API REST |
| STR-BB-01 | structural | Backend bundles | decision_de_plan | plan_context | PLAN-STRUCTURAL-005 | Aplicación monolítica server-side (Node.js), con posible evolución futura a microservicios |
| STR-DOB-01 | structural | Data output interfaces from backend bundles | decision_de_plan | plan_context | PLAN-STRUCTURAL-006 | API REST |
| STR-RB-01 | structural | Repository bundles | decision_de_plan | plan_context | PLAN-STRUCTURAL-007 | PostgreSQL (Cloud SQL) |
| STR-PIB-01 | structural | Platform & Infrastructure bundles | decision_de_plan | plan_context | PLAN-STRUCTURAL-008 | Google Cloud Platform (GCP) |
| STR-DID-01 | structural | Data input interfaces to device bundles | decision_de_plan | plan_context | PLAN-STRUCTURAL-009 | Lectura de código de barras |
| STR-DB-01 | structural | Device bundles | decision_de_plan | plan_context | PLAN-STRUCTURAL-010 | Lector de código de barras |
| STR-DB-02 | structural | Device bundles | decision_de_plan | plan_context | PLAN-STRUCTURAL-011 | Impresora |
| STR-DOD-01 | structural | Data output interfaces from device bundles | decision_de_plan | plan_context | PLAN-STRUCTURAL-012 | Libro de control mensual |
| STR-DOD-02 | structural | Data output interfaces from device bundles | decision_de_plan | plan_context | PLAN-STRUCTURAL-013 | PDF/Excel OC |
| STR-C-01 | structural | Constraints | restriccion | fragment | NFR-STRUCTURAL-001 | Registros de transacciones inmutables una vez emitidos |
| STR-C-02 | structural | Constraints | restriccion | fragment | NFR-STRUCTURAL-002 | Sistema no debe funcionar offline |
| STR-C-03 | structural | Constraints | restriccion | fragment | NFR-STRUCTURAL-003 | web intuitiva para personal no técnico |
| SCC-SU-01 | system_context | Source users | contexto | fragment | CTX-SYSTEM_CONTEXT-001 | QF DT |
| SCC-SU-02 | system_context | Source users | contexto | fragment | CTX-SYSTEM_CONTEXT-002 | QF Complementario |
| SCC-SU-03 | system_context | Source users | contexto | fragment | CTX-SYSTEM_CONTEXT-003 | Bodeguero |
| SCC-UDI-01 | system_context | User data input interfaces | decision_de_plan | plan_context | PLAN-SYSTEM_CONTEXT-004 | UI WEB (SPA) responsiva |
| SCC-UDO-01 | system_context | User data output interfaces | decision_de_plan | plan_context | PLAN-SYSTEM_CONTEXT-005 | UI WEB (SPA) responsiva |
| SCC-TU-01 | system_context | Target users | contexto | fragment | CTX-SYSTEM_CONTEXT-006 | QF DT |
| SCC-TU-02 | system_context | Target users | contexto | fragment | CTX-SYSTEM_CONTEXT-007 | QF Complementario |
| SCC-TU-03 | system_context | Target users | contexto | fragment | CTX-SYSTEM_CONTEXT-008 | Bodeguero |
| SCC-SS-01 | system_context | Source systems | contexto | fragment | CTX-SYSTEM_CONTEXT-009 | POS |
| SCC-SDI-01 | system_context | System data input interfaces | decision_de_plan | plan_context | PLAN-SYSTEM_CONTEXT-010 | API Transacciones POS |
| SCC-SDO-01 | system_context | System data output interfaces | decision_de_plan | plan_context | PLAN-SYSTEM_CONTEXT-011 | API Consulta Stock POS |
| SCC-TS-01 | system_context | Target systems | contexto | fragment | CTX-SYSTEM_CONTEXT-012 | POS |
| SCC-RDO-01 | system_context | Repository data output interfaces | decision_de_plan | plan_context | PLAN-SYSTEM_CONTEXT-013 | Generación de Libro de Controlados |
| SCC-TR-01 | system_context | Target repositories | contexto | fragment | CTX-SYSTEM_CONTEXT-014 | Libro físico de productos controlados (ISP) |
| SCC-SD-01 | system_context | Source devices | decision_de_plan | plan_context | PLAN-SYSTEM_CONTEXT-015 | Lector de código de barras |
| SCC-DDI-01 | system_context | Device data input interfaces | decision_de_plan | plan_context | PLAN-SYSTEM_CONTEXT-016 | Lectura de código de barra |
| SCC-DDO-01 | system_context | Device data output interfaces | decision_de_plan | plan_context | PLAN-SYSTEM_CONTEXT-017 | impresión mensual sobre hojas foliadas/timbradas |
| SCC-DDO-02 | system_context | Device data output interfaces | decision_de_plan | plan_context | PLAN-SYSTEM_CONTEXT-018 | Generación de OC PDF / Excel |

- Trazas: 193
- Destinos únicos declarados: 193
- Trazas huérfanas: 0
- Cobertura de trazas: 1,00
