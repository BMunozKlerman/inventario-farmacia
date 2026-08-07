# Plan E1

> Contexto técnico, tecnológico, topológico y operativo separado de la especificación funcional.

## Fuente: mapping/E1-architectural_context-plan_context.md

# Contexto de plan E1 — architectural_context

> Tecnología y topología se mantienen fuera de la especificación funcional.

## PLAN-ARCHITECTURAL_CONTEXT-014

- Sección: IT strategy
- Cita literal: «Plataforma web responsivo»

## PLAN-ARCHITECTURAL_CONTEXT-015

- Sección: IT strategy
- Cita literal: «Integración con el POS»

## PLAN-ARCHITECTURAL_CONTEXT-016

- Sección: Technology goals & drivers
- Cita literal: «Reducir errores derivados del registro manual/paralelo»

## PLAN-ARCHITECTURAL_CONTEXT-017

- Sección: Technology goals & drivers
- Cita literal: «Eliminar la doble digitación entre POS e inventario»

## PLAN-ARCHITECTURAL_CONTEXT-018

- Sección: Technology standards & policies
- Cita literal: «APIs para que el POS registre transacciones (venta, notas de crédito, entre otras) y consulta stock disponible»

## PLAN-ARCHITECTURAL_CONTEXT-019

- Sección: Technical principles
- Cita literal: «Sistema intuitivo»

## PLAN-ARCHITECTURAL_CONTEXT-020

- Sección: Technical principles
- Cita literal: «Integridad de los registros»

## PLAN-ARCHITECTURAL_CONTEXT-021

- Sección: Technical principles
- Cita literal: «no alteración de registros de transacciones una vez emitidos.»



## Fuente: mapping/E1-business_context-plan_context.md

# Contexto de plan E1 — business_context

> Tecnología y topología se mantienen fuera de la especificación funcional.

_Sin decisiones de plan adicionales._


## Fuente: mapping/E1-deployment-plan_context.md

# Contexto de plan E1 — deployment

> Tecnología y topología se mantienen fuera de la especificación funcional.

## PLAN-DEPLOYMENT-001

- Sección: Environments
- Cita literal: «Desarrollo»

## PLAN-DEPLOYMENT-002

- Sección: Environments
- Cita literal: «Producción»

## PLAN-DEPLOYMENT-003

- Sección: Bundles
- Cita literal: «Frontend: SPA (aplicación web con diseño responsivo)»

## PLAN-DEPLOYMENT-004

- Sección: Bundles
- Cita literal: «Backend: monolito (Node.js)»

## PLAN-DEPLOYMENT-005

- Sección: Middleware
- Cita literal: «Cloud SQL for PostgreSQL»

## PLAN-DEPLOYMENT-006

- Sección: Runtime
- Cita literal: «Node.js»

## PLAN-DEPLOYMENT-007

- Sección: Orchestration & scheduling
- Cita literal: «Cloud Run (backend)»

## PLAN-DEPLOYMENT-008

- Sección: Orchestration & scheduling
- Cita literal: «Cloud Scheduler (Jobs)»

## PLAN-DEPLOYMENT-009

- Sección: Container runtimes
- Cita literal: «Docker»

## PLAN-DEPLOYMENT-010

- Sección: Container runtimes
- Cita literal: «GCP: Cloud Run, Cloud SQL, Cloud Scheduler, Cloud Storage»

## PLAN-DEPLOYMENT-011

- Sección: Networks
- Cita literal: «Acceso vía HTTPS»

## PLAN-DEPLOYMENT-012

- Sección: Installation
- Cita literal: «Despliegue en GCP a cargo del equipo de desarrollo/implementación»

## PLAN-DEPLOYMENT-013

- Sección: Operation
- Cita literal: «Soporte y operación en producción a cargo de personal de soporte del cliente»



## Fuente: mapping/E1-functional-back-plan_context.md

# Contexto de plan E1 — functional-back

> Tecnología y topología se mantienen fuera de la especificación funcional.

## PLAN-FUNCTIONAL-BACK-001

- Sección: Bundles & components
- Cita literal: «Compras»

## PLAN-FUNCTIONAL-BACK-002

- Sección: Bundles & components
- Cita literal: «Recepción de Mercadería»

## PLAN-FUNCTIONAL-BACK-003

- Sección: Bundles & components
- Cita literal: «Reposición»

## PLAN-FUNCTIONAL-BACK-004

- Sección: Bundles & components
- Cita literal: «Inventario (stock, lotes, ubicaciones)»

## PLAN-FUNCTIONAL-BACK-005

- Sección: Bundles & components
- Cita literal: «Control Regulatorio (libro de productos controlados)»

## PLAN-FUNCTIONAL-BACK-006

- Sección: Bundles & components
- Cita literal: «Módulo de Alertas y Notificaciones»

## PLAN-FUNCTIONAL-BACK-007

- Sección: Bundles & components
- Cita literal: «Integración POS Venta»

## PLAN-FUNCTIONAL-BACK-008

- Sección: Bundles & components
- Cita literal: «Vencimientos (canje/destrucción)»

## PLAN-FUNCTIONAL-BACK-009

- Sección: Technology stack
- Cita literal: «Backend: monolito Node.js / DB: PostgreSQL / Infra: GCP»



## Fuente: mapping/E1-functional-front-plan_context.md

# Contexto de plan E1 — functional-front

> Tecnología y topología se mantienen fuera de la especificación funcional.

## PLAN-FUNCTIONAL-FRONT-001

- Sección: Bundles & components
- Cita literal: «Compras»

## PLAN-FUNCTIONAL-FRONT-002

- Sección: Bundles & components
- Cita literal: «Recepción de Mercadería»

## PLAN-FUNCTIONAL-FRONT-003

- Sección: Bundles & components
- Cita literal: «Reposición»

## PLAN-FUNCTIONAL-FRONT-004

- Sección: Bundles & components
- Cita literal: «Inventario (stock, lotes, ubicaciones)»

## PLAN-FUNCTIONAL-FRONT-005

- Sección: Bundles & components
- Cita literal: «Control Regulatorio (libro de productos controlados)»

## PLAN-FUNCTIONAL-FRONT-006

- Sección: Bundles & components
- Cita literal: «Reportes»

## PLAN-FUNCTIONAL-FRONT-007

- Sección: Bundles & components
- Cita literal: «Vencimientos (canje/destrucción)»

## PLAN-FUNCTIONAL-FRONT-008

- Sección: Technology stack
- Cita literal: «Frontend: SPA responsiva»



## Fuente: mapping/E1-structural-plan_context.md

# Contexto de plan E1 — structural

> Tecnología y topología se mantienen fuera de la especificación funcional.

## PLAN-STRUCTURAL-001

- Sección: Data input interfaces to frontend bundles
- Cita literal: «Interfaz web»

## PLAN-STRUCTURAL-002

- Sección: Frontend bundles
- Cita literal: «Single Page Application (SPA) web con diseño responsivo»

## PLAN-STRUCTURAL-003

- Sección: Data output interfaces from frontend bundles
- Cita literal: «UI WEB (SPA) responsiva»

## PLAN-STRUCTURAL-004

- Sección: Data input interfaces to backend bundles
- Cita literal: «API REST»

## PLAN-STRUCTURAL-005

- Sección: Backend bundles
- Cita literal: «Aplicación monolítica server-side (Node.js), con posible evolución futura a microservicios»

## PLAN-STRUCTURAL-006

- Sección: Data output interfaces from backend bundles
- Cita literal: «API REST»

## PLAN-STRUCTURAL-007

- Sección: Repository bundles
- Cita literal: «PostgreSQL (Cloud SQL)»

## PLAN-STRUCTURAL-008

- Sección: Platform & Infrastructure bundles
- Cita literal: «Google Cloud Platform (GCP)»

## PLAN-STRUCTURAL-009

- Sección: Data input interfaces to device bundles
- Cita literal: «Lectura de código de barras»

## PLAN-STRUCTURAL-010

- Sección: Device bundles
- Cita literal: «Lector de código de barras»

## PLAN-STRUCTURAL-011

- Sección: Device bundles
- Cita literal: «Impresora»

## PLAN-STRUCTURAL-012

- Sección: Data output interfaces from device bundles
- Cita literal: «Libro de control mensual»

## PLAN-STRUCTURAL-013

- Sección: Data output interfaces from device bundles
- Cita literal: «PDF/Excel OC»



## Fuente: mapping/E1-system_context-plan_context.md

# Contexto de plan E1 — system_context

> Tecnología y topología se mantienen fuera de la especificación funcional.

## PLAN-SYSTEM_CONTEXT-004

- Sección: User data input interfaces
- Cita literal: «UI WEB (SPA) responsiva»

## PLAN-SYSTEM_CONTEXT-005

- Sección: User data output interfaces
- Cita literal: «UI WEB (SPA) responsiva»

## PLAN-SYSTEM_CONTEXT-010

- Sección: System data input interfaces
- Cita literal: «API Transacciones POS»

## PLAN-SYSTEM_CONTEXT-011

- Sección: System data output interfaces
- Cita literal: «API Consulta Stock POS»

## PLAN-SYSTEM_CONTEXT-013

- Sección: Repository data output interfaces
- Cita literal: «Generación de Libro de Controlados»

## PLAN-SYSTEM_CONTEXT-015

- Sección: Source devices
- Cita literal: «Lector de código de barras»

## PLAN-SYSTEM_CONTEXT-016

- Sección: Device data input interfaces
- Cita literal: «Lectura de código de barra»

## PLAN-SYSTEM_CONTEXT-017

- Sección: Device data output interfaces
- Cita literal: «impresión mensual sobre hojas foliadas/timbradas»

## PLAN-SYSTEM_CONTEXT-018

- Sección: Device data output interfaces
- Cita literal: «Generación de OC PDF / Excel»


