# Taller 4 · Casos de uso

Se trabaja en clase, por equipo.

- **Entrega:** en el **repositorio del equipo en GitHub**, diligenciando el enunciado con los puntos 1 a 5 y subiendo el diagrama al repositorio _(imagen exportada o fuente PlantUML/draw.io)_.
- Herramienta: draw.io, PlantUML, StarUML o Visual Paradigm.

---

## 1. Actores y casos

**Actores**

| Actor             | Tipo _(humano / sistema externo / tiempo)_ | Principal o secundario | Objetivo en el sistema                                                                                                                       |
| ----------------- | ------------------------------------------ | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| _(usuario)_       | _(Humano)_                                 | _(Principal)_          | _(Gestionar sus ingresos, gastos y presupuesto personal)_                                                                                    |
| _(Administrador)_ | _(Humano)_                                 | _(Principal)_          | _(Desarrollar nuevas funcionalidades y correcion de errores)_                                                                                |
| _(Sistema IA)_    | _(Sistema externo)_                        | _(Secundario)_         | _(Procesar la información enviada por el sistema para generar análisis y recomendaciones generales sobre los hábitos de gasto del usuario.)_ |

- Roles, no personas. La base de datos y el servidor **no** son actores.
- Si el proyecto tiene componente de IA, el **proveedor del modelo** es un actor secundario.

**Casos de uso**

| ID    | Nombre _(verbo en infinitivo + objeto)_ | Actor principal | RF que cubre |
| ----- | --------------------------------------- | --------------- | ------------ |
| CU-01 | _(Registrar gastos)_                    | _(Usuario)_     | _(RF-01)_    |
| CU-02 | _(Registrar ingresos)_                  | _(Usario)_      | _(RF-02)_    |
| CU-03 | _(Modificar movimiento financiero)_     | _(Usuario)_     | _(RF-03)_    |
| CU-04 | _(Eliminar movimiento financiero)_      | _(Usuario)_     | _(RF-04)_    |
| CU-05 | _(Clasificar gasto)_                    | _(Usuario)_     | _(RF-05)_    |
| CU-06 | _(Consultar historial de movimientos)_  | _(Usuario)_     | _(RF-06)_    |
| CU-07 | _(Consultar total gastado)_             | _(Usuario)_     | _(RF-07)_    |
| CU-08 | _(Calcular saldo disponible)_           | _(Usuario)_     | _(RF-08)_    |
| CU-09 | _(Crear presupuesto mensual)_           | _(Usuario)_     | _(RF-09)_    |
| CU-10 | _(Consultar alerta de presupuesto)_     | _(Usuario)_     | _(RF-10)_    |
| CU-11 | _(Crear cuenta de usuario)_             | _(Usuario)_     | _(RF-11)_    |
| CU-12 | _(Iniciar sesión)_                      | _(Usuario)_     | _(RF-12)_    |
| CU-13 | _(Visualizar estadísticas de gastos)_   | _(Usuario)_     | _(RF-13)_    |
| CU-14 | _(Generar análisis financiero con IA)_  | _(Usuario)_     | _(RF-14)_    |
| CU-15 | _(Cambiar contraseña)_                  | _(Usuario)_     | _(RF-15)_    |
| …     |                                         |                 |              |

- **Mínimo 6 casos**, todos con al menos un RF.

---

## 2. Diagrama de casos de uso

Un solo diagrama con:

- **Límite del sistema** con su nombre; los casos dentro, los actores fuera.
- Todos los casos del punto 1 y sus asociaciones con los actores.
- Al menos una relación **`«include»`, `«extend»` o generalización**, justificada en una línea. Si el dominio no pide ninguna, se escribe por qué.

**Imagen o enlace al diagrama:** <<link>>

**Justificación de las relaciones:**

- _(completar)_

---

## 3. Casos críticos

Los tres casos que el prototipo implementa **de punta a punta** _(de la interfaz a la persistencia)_.

| Caso      | Por qué es crítico _(valor / frecuencia / riesgo técnico)_ |
| --------- | ---------------------------------------------------------- |
| _(CU-0#)_ | _(completar)_                                              |
| _(CU-0#)_ | _(completar)_                                              |
| _(CU-0#)_ | _(completar)_                                              |

- **Máximo uno** puede ser el caso de IA; los otros dos son funcionalidad con persistencia propia.
- No valen iniciar sesión.

---

## 4. Descripción detallada de los casos críticos

Una tabla por caso crítico.

| Campo                    | Contenido                                                    |
| ------------------------ | ------------------------------------------------------------ |
| **ID y nombre**          | _(completar)_                                                |
| **Actor principal**      | _(completar)_                                                |
| **Actores secundarios**  | _(completar o —)_                                            |
| **Requisitos que cubre** | _(RF-0#, RNF-0#)_                                            |
| **Precondiciones**       | _(completar)_                                                |
| **Disparador**           | _(completar)_                                                |
| **Frecuencia**           | _(completar, con la fuente del Taller 3 o de la entrevista)_ |

**Flujo principal**

1. _(El actor…)_
2. _(El sistema…)_
3. …

**Flujos alternos** _(se logra el objetivo por otro camino)_

- **#a.** _(condición → qué hace el sistema → a qué paso vuelve)_

**Excepciones** _(no se logra el objetivo)_

- **#a.** _(condición → qué hace el sistema → cómo termina)_

**Postcondiciones**

- **Éxito:** _(completar)_
- **Garantía mínima:** _(completar)_

- **Mínimo por caso:** 5 pasos en el flujo principal, **un flujo alterno y una excepción**.
- Pasos con un sujeto _(el actor o el sistema)_ y sin detalles de interfaz: _"elige la franja"_, no _"hace clic en el botón"_.
- Si uno de los críticos es el de IA, sus excepciones incluyen **timeout, cuota agotada y respuesta malformada**.

---

## 5. Trazabilidad

**Columna de caso de uso de la matriz** _(la que se abrió en la Clase 3)_:

| Requisito | Fuente             | Caso de uso |
| --------- | ------------------ | ----------- |
| RF-01     | _(P# o documento)_ | _(CU-0#)_   |
| …         |                    |             |

**Huecos detectados:**

| Hueco              | Cuál                      | Qué se hace                                    |
| ------------------ | ------------------------- | ---------------------------------------------- |
| RF sin caso de uso | _(completar o "ninguno")_ | _(se crea el caso / el RF sale del catálogo)_  |
| Caso de uso sin RF | _(completar o "ninguno")_ | _(se agrega el RF / el caso sale del alcance)_ |

- Todo lo que cambie el catálogo va al **registro de control de cambios** de la bitácora.

---

## Ejemplo diligenciado

Referencia de nivel de detalle. Mismo dominio de los talleres anteriores: **no se puede usar.**

**1. Actores** _(barbería; extracto)_

| Actor           | Tipo                         | Principal o secundario | Objetivo                                         |
| --------------- | ---------------------------- | ---------------------- | ------------------------------------------------ |
| Cliente         | Humano                       | Principal              | Conseguir un turno sin llamar                    |
| Barbero         | Humano                       | Principal              | Saber a quién atiende y registrar quién no llegó |
| Dueño           | Humano _(hereda de Barbero)_ | Principal              | Cerrar caja y mantener la clientela              |
| Proveedor de IA | Sistema externo              | Secundario             | Redactar el texto del recordatorio               |

**1. Casos** _(extracto)_

| ID    | Nombre                       | Actor principal | RF    |
| ----- | ---------------------------- | --------------- | ----- |
| CU-01 | Reservar turno               | Cliente         | RF-01 |
| CU-02 | Consultar franjas libres     | Cliente         | RF-01 |
| CU-03 | Cancelar turno               | Cliente         | RF-04 |
| CU-05 | Marcar turno no asistido     | Barbero         | RF-02 |
| CU-06 | Cerrar caja del día          | Dueño           | RF-05 |
| CU-07 | Redactar recordatorio con IA | Dueño           | RF-08 |

**2. Relaciones:** CU-01 `«include»` CU-02, porque toda reserva pasa por consultar las franjas y el cliente también las consulta sin reservar. Dueño hereda de Barbero, porque el dueño también atiende una silla.

**3. Críticos**

| Caso                               | Por qué                                                                                                                |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| CU-01 Reservar turno               | Es el problema que se tiene es: el teléfono no para los sábados; ~40 al día; riesgo de dos reservas en la misma franja |
| CU-06 Cerrar caja del día          | Todos los días; cálculo sobre los turnos atendidos                                                                     |
| CU-07 Redactar recordatorio con IA | El caso de IA; reduce los no asistidos _(P6)_                                                                          |

**4. Descripción** _(CU-07; CU-01 está completo en la Sesión 5)_

| Campo                   | Contenido                                            |
| ----------------------- | ---------------------------------------------------- |
| **Actor principal**     | Dueño                                                |
| **Actores secundarios** | Proveedor de IA                                      |
| **Requisitos**          | RF-08, RNF-04 _(respuesta en menos de 10 s)_         |
| **Precondiciones**      | Hay turnos _Reservados_ para el día siguiente        |
| **Disparador**          | El dueño prepara los recordatorios al cierre del día |
| **Frecuencia**          | Una vez al día                                       |

1. El dueño pide los recordatorios del día siguiente.
2. El sistema lista los turnos _Reservados_ de mañana.
3. El sistema envía al proveedor de IA la franja, el barbero y el nombre de pila de cada cliente, **sin teléfono**.
4. El proveedor devuelve un borrador de mensaje por turno.
5. El sistema valida que cada borrador traiga fecha y franja, y los muestra marcados como _texto generado_.
6. El dueño revisa, edita si quiere y aprueba.
7. El sistema guarda los mensajes aprobados listos para enviar.

- **5a.** Un borrador no trae fecha o franja: se descarta y se usa la plantilla fija para ese turno. Vuelve al paso 6.
- **6a.** El dueño descarta un borrador: el sistema usa la plantilla fija para ese turno. Vuelve al paso 6.
- **4a.** _(excepción)_ El proveedor no responde en 10 s o devuelve HTTP 429: el sistema informa que la IA no está disponible, registra el evento y ofrece la plantilla fija para todos. El caso termina sin texto generado.

**Postcondiciones.** Éxito: cada turno de mañana tiene un mensaje aprobado. Garantía mínima: ningún dato de contacto sale hacia el proveedor.

**5. Huecos:** RF-06 _(reporte mensual de ingresos)_ sin caso → se crea CU-09 Consultar reporte mensual. CU-04 Avisar a la lista de espera sin RF → se agrega RF-11 y se registra en el control de cambios.
