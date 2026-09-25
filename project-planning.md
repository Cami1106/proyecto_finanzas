# Taller  2· Metodología y tablero

Enunciado del **Taller 2**. Se trabaja en clase, en equipo, y se entrega al final de la sesión.

- **Entrega:** un documento por equipo con los puntos 1, 2, 3 y 5, más el **enlace al tablero** del punto 4 con el docente invitado.
- **Nota:** cuenta dentro de los Talleres 1 a 6 *(60% del Seguimiento)*. **No es recuperable**: se califica con la asistencia y el trabajo hecho en la sesión.
- **Requisito previo:** ficha de dominio aprobada en el primer taller. Si quedó con ajustes, se resuelven en los primeros 5 minutos.
- Lo que se produce aquí se reutiliza: la justificación pasa al **numeral 5** de la Nota 1 y el tablero con su acta abren la **bitácora de gestión**.

---

## 1. Caracterización del dominio

Ubicar el proyecto en cada factor **con un dato concreto del dominio**, no con una opinión. Una celda que dice "medio" sin evidencia no cuenta.

| Factor | Valoración *(ágil ← → plan)* | Evidencia del dominio |
| --- | --- | --- |
| Tamaño | *(agil)* | *(la primera version tendra funciones limitadas como registrar ingresos, gastos, categorias y presupuesto)* |
| Criticidad | *(agil)* | *(Un error en un registro puede afectar el control financiero del usuario)* |
| Dinamismo de los requisitos | *(agil)* | *(los usuarios pueden solicitar cambios en categorias y presupuestos despues de probar la aplicacion)* |
| Personal *(experiencia del equipo)* | *(plan)* | *(El equipo de trabajo esta compuesto por personas con poca experiencia en el desarrollo de software)* |
| Cultura *(del cliente u organización)* | *(agil)* | *(El usuario acepta revisar avances parciales y dar su opinion sobre las funciones de registro y control de gastos)* |
| Acceso al cliente | *(agil)* | *(El cliente puede probar la funcionalidad y comunicar cambios que necesite)* |
| Regulación | *(plan)* | *(La aplicacion debe considerar valores financieros como la TRM y la tasa efectiva anual, los cuales deben manejarse con formulas y valores definidos.)* |

---

## 2. Selección y justificación

**Metodología elegida:** *(Scrum)*

**Justificación** *(un párrafo que cite al menos tres factores del punto 1)*:

*(Se selecciona Scrum porque el proyecto es pequeño (Tamaño: bajo), los requisitos pueden cambiar durante el desarrollo (Dinamismo: medio) y el usuario puede revisar avances parciales (Cultura: ágil). Además, el equipo está conformado por 2 estudiantes (Personal: plan).)*

**Alternativas descartadas** *(mínimo dos)*:

| Alternativa | Por qué no encaja en este dominio |
| --- | --- |
| *(cascada)* | *(Los requisitos de la aplicacion pueden cambiar despues de que el usuario pruebe los avances, por lo que definir todas las funcionalidades al inicio dificultaria integrar cambios en categorias o presupuestos)* |
| *(kanban)* | *(El proyecto necesita trabajar por etapas y realizar revisiones de los avances, por lo que Scrum permite organizar mejor las tareas.)* |

> "Porque es la más usada" o "porque es flexible" no son justificaciones: no dicen nada del dominio.

---

## 3. Adaptación

Explicar cómo se organiza el equipo **dentro** de ellas.

| Campo | Respuesta |
| --- | --- |
| Duración de la iteración *(o "flujo continuo")* | *(Cada 2 semanas)* |
| Eventos o reuniones y cuándo se hacen | *(Cada 3 dias)* |
| Cómo se llega a la primera entrega | *(Se desarrollan primero las funciones principales como el registro de ingresos, gastos, categoria y consultas de gastos.)* |

**Roles asignados** *(ajustar los nombres a la metodología elegida)*:

| Integrante | Rol | Qué hace en la práctica |
| --- | --- | --- |
| *(Maria Camila Gomez Toro)* | *(e.g. Product Owner)* | *(definir las tareas)* |
| *(Andres Steven Cortes Perez)* | *(e.g. Scrum Master)* | *(organizar el trabajo y revisar los avances.)* |
| *(Andres Steven Cortes Perez y Maria Camila Gomez Toro)* | *(Desarrollador)* | *(desarrollar las funcionalidades)* |

**Definición de Hecho** *(mínimo tres condiciones verificables para que una tarjeta pase a Hecho)*:

1. *(La funcionalidad esta programada y funciona correctamente)*
2. *(La funcionalidad fue probada sin errores)*
3. *(El codigo esta en el repositorio de github)*

---

## 4. Tablero y backlog inicial

Crear el tablero en **GitHub Projects**, Trello o Jira e **invitar al docente**.

**Mínimos del tablero:**

- Columnas: *Backlog · Por hacer · En progreso · En revisión · Hecho* *(o equivalentes, justificadas)*.
- **Límite de WIP** declarado en *En progreso*.
- **Mínimo 10 tarjetas** con el trabajo hasta la Nota 1 *(Clase 4)*. Los requisitos del producto todavía no existen: el backlog de hoy es de **tareas del proyecto** *(preparar la entrevista, redactar el problema, catalogar RF y RNF, armar la sustentación…)*.
- Cada tarjeta con **responsable, estimación** *(horas o puntos)* y **fecha límite**.
- **Todos los integrantes** con al menos una tarjeta asignada.

**Enlace al tablero:** *(completar)*

**Método de estimación usado:** *(horas / tres puntos / puntos de historia con planning poker)*

---

## 5. Primera acta

Primera entrada de la bitácora de gestión.

| Campo | Respuesta |
| --- | --- |
| Fecha | *(14/09/26)* |
| Asistentes | *(Andres Steven Cortes Perez y Maria Camila Gomez Toro)* |
| Decisiones tomadas | *(Definir el problema del proyecto, establecer el alcance inicial de la aplicación y trabajar con la metodología Scrum.)* |
| Compromisos *(quién, qué)* | *(Andres Steven: definir requisitos y organizar el tablero de GitHub. Maria Camila: apoyar la definición del alcance y la planificación del proyecto.)* |
| Bloqueos o riesgos | *( Falta de requisitos detallados del cliente y posibilidad de que algunos requisitos cambien durante el desarrollo.)* |

## Ejemplo diligenciado

Referencia de nivel de detalle. Mismo dominio del ejemplo de la ficha: **no se puede usar.**

**1. Caracterización** *(barbería de barrio con tres sillas)*

| Factor | Valoración | Evidencia |
| --- | --- | --- |
| Tamaño | Ágil | Equipo de 3; un solo interesado con poder de decisión *(el dueño)* |
| Criticidad | Ágil | Si el sistema falla se vuelve al cuaderno; no hay riesgo físico ni pérdida grave |
| Dinamismo | Ágil | El dueño no sabe si quiere reservas por WhatsApp o por web hasta ver una pantalla |
| Personal | Intermedio | Nadie ha trabajado con Scrum; dos integrantes han hecho proyectos web |
| Cultura | Ágil | El dueño acepta ver avances parciales y opinar |
| Acceso al cliente | Ágil | El tío de un integrante; disponible los lunes |
| Regulación | Plan *(leve)* | Maneja nombres y teléfonos: Ley 1581 de 2012, sin norma sectorial |

**2. Selección:** Scrum. Los requisitos van a cambiar cuando el dueño vea las primeras pantallas *(dinamismo)*, un fallo es recuperable *(criticidad)* y hay acceso semanal al dueño para las Review *(acceso al cliente)*. Descartamos **cascada** porque obliga a cerrar requisitos que el dueño aún no conoce, y **Kanban** porque el trabajo sí se puede planificar en bloques y necesitamos un compromiso semanal ligado a las fechas de entrega.

**3. Adaptación:** Sprint de dos semanas. Planning el lunes por videollamada, Review con el dueño el lunes siguiente, Retro al final de la segunda clase de la semana. Daily por chat del equipo, tres preguntas por escrito. DoD: revisado por otro integrante, subido al repositorio, enlazado en la tarjeta.

**4. Tablero:** GitHub Projects, WIP de 3 en *En progreso*. 12 tarjetas estimadas en horas, entre ellas *Preparar guion de entrevista (2 h)*, *Entrevistar al dueño (1 h)*, *Redactar problema y alcance (3 h)*, *Catalogar RF (4 h)*, *Ensayar sustentación (2 h)*.

**5. Acta:** se decide Scrum con Sprint semanal; compromiso de agendar la entrevista con el dueño antes de la primera entrega.