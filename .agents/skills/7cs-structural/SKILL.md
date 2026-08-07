---
name: 7cs-structural
description: Procesador del Structural Canvas bajo la metodología 7Cs. Convierte el COM JSON en especificaciones y planes de arquitectura para Spec Kit.
---

# Skill: 7cs-structural

## Visión General
Este skill toma como entrada el **Canvas Object Model (COM)** extraído del **Structural Canvas** (página 4) y aplica las transformaciones necesarias para alimentar la arquitectura del sistema en Spec Kit.

---

## Reglas de Mapeo y Transformación

### 1. Regla Guardrail de Negocio vs. Tecnología (Regla G2)
- **`/speckit.specify` (Requisitos Observables):** No debe contener nombres de tecnologías específicas, librerías, bases de datos o servicios cloud (ej. Node.js, PostgreSQL, GCP, Docker). Solo se describen capacidades funcionales o estructurales observables.
- **`/speckit.plan` (Planes de Implementación):** Toda mención tecnológica explícita proveniente de los post-its o notas se asigna directamente a las decisiones de diseño e infraestructura dentro del plan.

### 2. Mapeo de Secciones a Spec Kit

| Sección COM Original | Destino Spec Kit | Identificador | Regla de Transformación |
| :--- | :--- | :--- | :--- |
| **Frontend bundles** | `/speckit.plan` | `COMP-FE-n` | Define módulos/paquetes de interfaz. |
| **Backend bundles** | `/speckit.plan` | `COMP-BE-n` | Define módulos/paquetes de lógica de negocio. |
| **Repository bundles** | `/speckit.plan` | `COMP-REPO-n` | Define persistencia y modelos de datos. |
| **Platform & Infra bundles** | `/speckit.plan` | `INFRA-n` | Define la plataforma y servicios base. |
| **Device bundles** | `/speckit.plan` | `DEV-n` | Define integración con hardware o dispositivos. |
| **Interfaces (Inputs/Outputs)** | `/speckit.specify` | `INT-STR-n` | Define los contratos e interfaces requeridos entre módulos. |
| **Constraints** | `/speckit.specify` | `R-STR-n` / `NFR-STR-n` | Si describe un comportamiento observable, se promueve a Requisito (R) o Requisito No Funcional (NFR). |

---

## Flujo de Ejecución (Fase 2)

Al procesar un archivo `E1-structural-p4.json`:

1. **Lectura e Ingesta:** Cargar las secciones y stickies del COM.
2. **Filtrado y Clasificación:**
   - Separar conceptos tecnológicos de requerimientos de interfaz y restricciones.
   - Evaluar los post-its de `Constraints` para etiquetarlos como `R-STR-n` (Funcional) o `NFR-STR-n` (Rendimiento, Seguridad, Inmutabilidad, etc.).
3. **Generación de Trazabilidad:** Crear una tabla 1:1 que mapee cada `id` del sticky original (ej. `STR-FB-01`) hacia su destino en Spec Kit.
4. **Resumen de Balance Structural:** Describir la cohesión entre Frontend, Backend, Repositorios e Interfaces.

---

## Formato de Salida Esperado

```markdown
# 7Cs Structural Mapping Report - [Delivery ID]

## 1. Mapeo a /speckit.specify
### Interfaces y Contratos
- **INT-STR-01:** [Descripción sin mencionar tecnologías]

### Requisitos Estructurales y Restricciones
- **R-STR-01:** [Requisito observable derivado de Constraints]
- **NFR-STR-01:** [Restricción no funcional observable]

---

## 2. Mapeo a /speckit.plan
### Componentes de Arquitectura
- **COMP-FE-01:** [Módulo Frontend + Tech Stack asignado]
- **COMP-BE-01:** [Módulo Backend + Tech Stack asignado]
- **COMP-REPO-01:** [Persistencia / DB + Tech Stack asignado]
- **INFRA-01:** [Infraestructura cloud / despliegue]

---

## 3. Tabla de Trazabilidad 1:1

| ID Sticky COM | Texto Original | Elemento Spec Kit | Tipo |
| :--- | :--- | :--- | :--- |
| STR-FB-01 | ... | COMP-FE-01 | Plan |
| STR-C-01 | ... | NFR-STR-01 | Specify |