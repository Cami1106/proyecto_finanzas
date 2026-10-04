# Taller 3 · Elicitación cruzada de requerimientos

Enunciado del **Taller 3**. Se trabaja en clase, por parejas de equipos, y se entrega al final de la sesión.

- **Dinámica:** cada equipo entrevista a otro, que hace de **cliente** de su dominio, y luego se invierten los papeles.
- **Entrega:** en el **repositorio del equipo en GitHub**, diligenciando el enunciado con los puntos 1, 4, 5 y 6; las notas de la entrevista del punto 2 o 3 van como anexo en el mismo archivo.

---

## 1. Preparación

**Emparejamiento:** formar parejas de equipos con dominios distintos.

**Cómo funciona:** cada equipo pregunta **sobre su propio proyecto**. El otro equipo no responde sobre el suyo: se pone en el lugar del usuario del proyecto de quien pregunta. Si A hace inventario de materiales para técnicos, en la Ronda 1 B hace de almacenista de esa empresa y responde a las preguntas de A; en la Ronda 2, A hace de usuario del dominio de B.

- Que el cliente no conozca el dominio **es parte del ejercicio**: obliga a preguntar sin dar por sentado nada, y lo que el cliente improvisa se valida después con el cliente del proyecto.
- Lo que se evalúa hoy es la **técnica**: el guion, el sondeo, las notas y la conversión en requisitos con fuente. La verdad del dominio sale de la entrevista con el cliente del proyecto.
- **Este emparejamiento queda fijo:** el equipo que hace de cliente hoy es el **equipo cliente** para los proyectos que no tienen usuario real ni sustituto.

**Tarjeta de personaje:** el equipo entrevistador se la entrega al cliente al inicio, para que pueda responder con verosimilitud. Da el contexto, **no las respuestas**.

| Campo                      | Ejemplo _(barbería)_                                       |
| -------------------------- | ---------------------------------------------------------- |
| Quién es                   | Dueño de la barbería, 15 años con el local                 |
| Qué hace en el día a día   | Atiende una silla, contesta el teléfono y cierra caja      |
| Cómo se hace hoy           | Cuaderno de turnos y llamadas                              |
| Relación con la tecnología | Usa WhatsApp; nunca ha usado un computador para el negocio |

**Como cliente** _(del dominio del otro equipo)_:

- Leer la ficha de dominio y la tarjeta de personaje del equipo que va a entrevistar.
- Sostener el personaje toda la ronda _(e.g. "soy la dueña de la papelería, 12 años con el negocio, no uso computador")_.
- Responder con **problemas y situaciones del día a día**, no con soluciones técnicas. Si no sabe algo, puede inventarlo, siempre que sea verosímil con la tarjeta.

**Como entrevistador** _(del dominio propio)_:

- Ordenar las 10 preguntas. El banco de abajo sirve para completar tipos que falten.
- Asignar los roles de la entrevista.

**Banco de preguntas por tipo:** plantillas que sirven para cualquier dominio. Se reemplaza lo que va entre guillemets _(«proceso», «elemento»)_ por el vocabulario del proyecto propio. **Copiarlas sin adaptar no cuenta**: una pregunta que podría hacerse en cualquier proyecto no saca requisitos de este.

| Tipo                | Para qué                                     | Plantillas                                                                                                                                               |
| ------------------- | -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Contexto**        | Entender el rol y el proceso completo        | ¿Cuál es su papel en «el negocio / el área»? · ¿Cómo se hace hoy «el proceso», desde que empieza hasta que termina? · ¿Quién más participa?              |
| **Abierta**         | Encontrar el dolor                           | ¿Qué es lo que más le complica de «el proceso»? · ¿Qué le quita más tiempo en la semana? · Si pudiera cambiar una sola cosa, ¿cuál sería?                |
| **Sondeo**          | Profundizar en una respuesta                 | ¿Por qué? · ¿Me cuenta la última vez que pasó? · ¿Qué hizo en ese momento? · ¿Qué quiere decir con «término que usó el cliente»?                         |
| **Excepción**       | Sacar flujos alternos                        | ¿Qué pasa cuando «el elemento» falta, llega tarde o viene mal? · ¿Y si la persona responsable no está? · ¿Qué hace cuando se equivoca al registrar algo? |
| **Cuantitativa**    | Sacar RNF medibles                           | ¿Cuántos «registros» maneja al día o al mes? · ¿Cuántas personas lo hacen al mismo tiempo? · ¿Cuánto tiempo toma hoy? · ¿Cuánto es aceptable esperar?    |
| **Datos y control** | Sacar permisos, auditoría y datos personales | ¿Quién puede ver o cambiar «la información»? · ¿Necesita saber quién hizo cada cambio y cuándo? · ¿Qué datos de personas se guardan?                     |
| **Cierre**          | No dejar nada por fuera                      | ¿Hay algo que no le pregunté y debería saber? · ¿Con quién más debería hablar? · ¿Qué documentos o formatos usa hoy y me los puede mostrar?              |

- **Evitar:** preguntas sobre la solución _("¿quiere una app móvil?")_, inductoras _("¿no le parece que sería mejor…?")_ y las que se responden con sí o no sin dar información.

**Guion de entrevista**

| #   | Pregunta                                                                                                                                                                | Tipo _(contexto / abierta / sondeo / excepción / cuantitativa / datos y control / cierre)_ |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| P1  | _(¿Cómo lleva actualmente el control de sus ingresos y gastos desde que recibe dinero hasta que revisa cuánto le queda disponible?)_                                    | _(Contexto)_                                                                               |
| P2  | _(¿Qué es lo que más se le dificulta actualmente al llevar el control de sus finanzas personales?)_                                                                     | _(abierta)_                                                                                |
| P3  | _(Cuando registra un ingreso o un gasto, ¿qué información considera necesaria guardar? )_                                                                               | _(Datos y control)_                                                                        |
| P4  | _(Cuando quiere revisar en qué ha gastado su dinero durante el mes, ¿cómo lo hace actualmente y qué información necesita consultar? )_                                  | _(abierta)_                                                                                |
| P5  | _(¿Qué hace cuando registra un ingreso o gasto con un valor, fecha o categoría incorrecta?)_                                                                            | _(Excepcion)_                                                                              |
| P6  | _(¿Qué debería ocurrir cuando intenta registrar un movimiento y falta información necesaria?)_                                                                          | _(Excepcion)_                                                                              |
| P7  | _(Aproximadamente, ¿cuántos ingresos y gastos registra durante un día, una semana o un mes?)_                                                                           | _(Cuantitativa)_                                                                           |
| P8  | _(Cuando registra o consulta información financiera, ¿cuánto tiempo considera aceptable esperar para obtener una respuesta?)_                                           | _(Cuantitativa)_                                                                           |
| P9  | _(¿Quién debería poder consultar, modificar o eliminar la información financiera registrada en su cuenta?)_                                                             | _(Datos y control)_                                                                        |
| P10 | _(¿Cómo maneja actualmente un presupuesto mensual y cómo identifica que está cerca de gastar más de lo planeado?)_                                                      | _(Sondeo)_                                                                                 |
| P11 | _(¿Qué información o aviso le sería útil recibir cuando se acerque o supere el presupuesto que estableció?)_                                                            | _(Sondeo)_                                                                                 |
| P12 | _(¿Hay alguna situación relacionada con el control de sus ingresos, gastos o presupuesto que no le hayamos preguntado y considere importante?)_                         | _(Cierre)_                                                                                 |
| P13 | _(¿Cómo considera que debería identificarse un usuario antes de poder consultar su información financiera y qué información debería solicitarse para crear su cuenta?)_ | _(Datos y control)_                                                                        |
| P14 | _(¿Qué consecuencias tendría para usted que un ingreso o gasto registrado se pierda, cambie de valor o no pueda consultarse?)_                                          | _(Excepcion)_                                                                              |
| P15 | _(Cuando revisa sus gastos, ¿qué tipo de información o recomendación le ayudaría a entender mejor cómo está utilizando su dinero?)_                                     | _(Abierta)_                                                                                |

- **Mínimo:** dos preguntas de **excepción** y dos **cuantitativas**. De ellas salen los flujos alternos y los RNF.

**Roles**

| Rol           | Integrante                         |
| ------------- | ---------------------------------- |
| Entrevistador | _(Camila Gomez and Steven Cortes)_ |
| Anotador      | _(Camila Gomez and Steven Cortes)_ |
| Observador    | _(Camila Gomez and Steven Cortes)_ |

> **Equipo de 2:** el anotador asume también la observación. **Equipo de 4:** el cuarto integrante lleva el tiempo y anota las preguntas de sondeo que surjan.

---

## 2. Ronda 1

El **equipo A** entrevista al **equipo B**, que hace de cliente del dominio de A.

- 12 minutos exactos: el docente marca el tiempo.
- El anotador registra las respuestas **textuales**, numeradas con la pregunta que las originó _(P1, P2…)_. Si una respuesta abre un tema nuevo, la pregunta de sondeo se anota como _P4a, P4b_.
- El observador anota contradicciones, jerga del dominio y lo que el cliente evita responder.

---

## 3. Ronda 2

Se invierten los papeles: el **equipo B** entrevista al **equipo A**. Mismas reglas.

---

## 4. Análisis

Convertir las notas propias en requisitos candidatos. Todavía no es el catálogo final: es lo que se va a confirmar con el cliente del proyecto.

**Requisitos funcionales candidatos** _(mínimo 8)_:

| ID    | Descripción                                                                                                                                                                                                                                        | Prioridad _(MoSCoW)_ | Fuente       |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------------ |
| RF-01 | _(El sistema debe permitir al usuario registrar gastos, almacenando la información definida para cada movimiento.)_                                                                                                                                | _(Must)_             | _(P3)_       |
| RF-02 | _(El sistema debe permitir al usuario registrar ingresos, almacenando la información definida para cada movimiento.)_                                                                                                                              | _(Must)_             | _(P3)_       |
| RF-03 | _(El sistema debe permitir al usuario modificar ingresos y gastos previamente registrados.)_                                                                                                                                                       | _(Should)_           | _(P5)_       |
| RF-04 | _(El sistema debe permitir al usuario eliminar ingresos y gastos previamente registrados.)_                                                                                                                                                        | _(Should)_           | _(P5, P9)_   |
| RF-05 | _(El sistema debe permitir clasificar los gastos por categorías.)_                                                                                                                                                                                 | _(Must)_             | _(P3, P4)_   |
| RF-06 | _(El sistema debe permitir al usuario consultar el historial de ingresos y gastos registrados.)_                                                                                                                                                   | _(Must)_             | _(P4)_       |
| RF-07 | _(El sistema debe permitir al usuario consultar el total de gastos realizados durante un periodo determinado.)_                                                                                                                                    | _(Should)_           | _(P4)_       |
| RF-08 | _(El sistema debe calcular y mostrar el saldo disponible a partir de los ingresos y gastos registrados.)_                                                                                                                                          | _(Must)_             | _(P1, P4)_   |
| RF-09 | _(El sistema debe permitir al usuario crear y definir un presupuesto mensual.)_                                                                                                                                                                    | _(Should)_           | _(P10)_      |
| RF-10 | _(El sistema debe generar alertas cuando el usuario se acerque o supere el límite de su presupuesto.)_                                                                                                                                             | _(Should)_           | _(P10, P11)_ |
| RF-11 | _(El sistema debe permitir la creación de una cuenta de usuario utilizando la información de registro definida.)_                                                                                                                                  | _(Must)_             | _(P13)_      |
| RF-12 | _(El sistema debe permitir al usuario autenticarse para acceder a su información financiera.)_                                                                                                                                                     | _(Must)_             | _(P9, P13)_  |
| RF-13 | _(El sistema debe permitir al usuario visualizar estadísticas de sus gastos, organizadas por categorías y periodos.)_                                                                                                                              | _(Should)_           | _(P4)_       |
| RF-14 | _(El sistema debe permitir al usuario generar mediante inteligencia artificial un análisis de sus movimientos financieros, identificando patrones de gasto y proporcionando recomendaciones generales para mejorar el control de su presupuesto.)_ | _(Must)_             | _(P15)_      |
| RF-15 | _(El sistema debe permitir al usuario cambiar la contraseña de su cuenta)_                                                                                                                                                                         | _(Must)_             | _(P13)_      |
| …     |                                                                                                                                                                                                                                                    |                      |              |

**Requisitos no funcionales candidatos** _(mínimo 3, con métrica)_:

| ID     | Característica _(ISO/IEC 25010)_ | Descripción medible                                                                                                                                                                             | Fuente  |
| ------ | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| RNF-01 | _(Eficiencia de desempeño)_      | _(Las operaciones principales de registro, consulta y actualización de información deberán responder en un máximo de 2 segundos bajo condiciones normales de uso.)_                             | _(P8)_  |
| RNF-02 | _(Usabilidad)_                   | _(Un usuario nuevo deberá poder registrar un ingreso o gasto en un tiempo máximo de 1 minuto, sin asistencia externa.)_                                                                         | _(P6)_  |
| RNF-03 | _(Seguridad)_                    | _(El sistema deberá solicitar autenticación antes de permitir al usuario consultar o modificar su información financiera.)_                                                                     | _(P9)_  |
| RNF-04 | _(Confidencialidad)_             | _(Un usuario autenticado únicamente podrá consultar, modificar o eliminar la información financiera asociada a su propia cuenta.)_                                                              | _(P9)_  |
| RNF-05 | _(Fiabilidad)_                   | _(El 100 % de los movimientos almacenados correctamente deberá conservar su valor, fecha, categoría y demás información registrada al volver a consultarlos.)_                                  | _(P14)_ |
| RNF-06 | _(Fiabilidad de la IA)_          | _(Si el servicio de inteligencia artificial no responde o devuelve una respuesta inválida, el sistema deberá informar al usuario y mantener intactos los movimientos financieros almacenados.)_ | _(P15)_ |
| …      |                                  |                                                                                                                                                                                                 |         |

**Ambigüedades y conflictos detectados** _(lo que hay que aclarar con el cliente del proyecto)_:

- _(¿Qué información será obligatoria al registrar un ingreso o gasto: valor, fecha, categoría, descripción u otros datos?)_
- _(¿Las categorías de gastos serán únicamente las definidas por el sistema o el usuario podrá crear nuevas categorías?)_
- _(¿Al eliminar un ingreso o gasto este se borrará definitivamente o deberá conservarse algún registro de la operación?)_
- _(¿El presupuesto mensual será un único valor general o se podrán establecer presupuestos diferentes por categoría?)_
- _(¿En qué momento debe generarse una alerta de presupuesto: al acercarse al límite, al alcanzarlo o al superarlo?)_
- _(¿Qué tipos de estadísticas debe mostrar el sistema: gastos por categoría, evolución mensual, comparación entre ingresos y gastos u otras?)_
- _(¿Qué información financiera podrá utilizar el componente de inteligencia artificial para realizar el análisis?)_
- _(¿Qué tipo de recomendaciones podrá generar la inteligencia artificial sin considerarse asesoría financiera profesional?)_
- _(¿Con qué datos se creará la cuenta del usuario y cuáles serán obligatorios?)_

> Todo requisito lleva **fuente**. Un requisito sin pregunta que lo respalde es un requisito inventado por el equipo.

---

## 5. Validación cruzada

El equipo cliente lee la lista del punto 4 y marca cada requisito:

| Marca | Significado                                     |
| ----- | ----------------------------------------------- |
| ✅    | Lo dije y está bien entendido                   |
| ✏️    | Lo dije, pero no así _(se anota la corrección)_ |
| ❌    | No lo dije: el equipo lo supuso                 |

**Resultado de la validación:**

| Requisito                                   | Marca   | Corrección del cliente                                                                                                                       |
| ------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| _(RF-01 Registrar gastos)_                  | _(✅)_  |
| _(RF-02 Registrar ingresos)_                | _(✏️ )_ | _(El registro debe almacenar la información necesaria de cada movimiento, como valor, fecha y demás datos definidos.)_                       |
| _(RF-03 Modificar ingresos y gastos)_       | _(❌)_  | _(El cliente no mencionó inicialmente la posibilidad de modificar registros. Pasa a validación posterior.)_                                  |
| _(RF-04 Eliminar ingresos y gastos)_        | _(❌)_  | _(El cliente no mencionó inicialmente la eliminación de movimientos. Pasa a validación posterior.)_                                          |
| _(RF-05 Clasificar gastos por categorías)_  | _(✅)_  |
| _(RF-06 Consultar historial)_               | _(✏️ )_ | _(El cliente indicó la necesidad de consultar los registros de forma organizada.)_                                                           |
| _(RF-07 Consultar total gastado)_           | _(✏️)_  | _(El total debe calcularse a partir de los gastos registrados por el usuario.)_                                                              |
| _(RF-08 Consultar saldo disponible)_        | _(❌)_  | _(No fue mencionado explícitamente durante la entrevista inicial. Pasa a validación posterior.)_                                             |
| _(RF-09 Crear presupuesto mensual)_         | _(❌)_  | _(El cliente no mencionó inicialmente la creación de un presupuesto mensual.)_                                                               |
| _(RF-10 Generar alertas de presupuesto)_    | _(❌)_  | _(La generación de alertas no fue mencionada explícitamente por el cliente.)_                                                                |
| _(RF-11 Crear cuenta de usuario)_           | _(❌)_  | _(No fue mencionado durante la entrevista original. Se incorpora como pregunta posterior de validación.)_                                    |
| _(RF-12 Autenticarse en el sistema)_        | _(✏️)_  | _(El cliente indicó que se manejará información personal, pero no definió inicialmente el mecanismo de autenticación.)_                      |
| _(RF-13 Visualizar estadísticas de gastos)_ | _(❌)_  | _(La funcionalidad se encontraba dentro del alcance del proyecto, pero no fue mencionada directamente durante la entrevista del ejercicio.)_ |
| _(RF-14 Generar análisis mediante IA)_      | _(❌)_  | _(El componente de inteligencia artificial no fue definido durante la entrevista original y debe ser validado con el cliente.)_              |
| _(RF-15 Permitir al usuario cambiar la contraseña de su cuenta)_      | _(❌)_  | _(No fue mencionado en la entrevista original; se incorpora como requisito candidato pendiente de validación.)_              |

| Requisito                                     | Marca  | Corrección del cliente                                                                                                                                      |
| --------------------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| _(RNF-01 Eficiencia de desempeño)_            | _(✏️)_ | _(El cliente espera que la aplicación responda rápidamente, pero el tiempo máximo debe quedar definido y validado como criterio medible.)_                  |
| _(RNF-02 Usabilidad)_                         | _(✏️)_ | _(Se busca que el registro de movimientos sea sencillo y rápido, pero el tiempo máximo debe definirse como criterio del proyecto.)_                         |
| _(RNF-03 Seguridad — autenticación)_          | _(✏️)_ | _(El cliente indicó que el sistema manejará información personal, por lo que debe restringirse el acceso, aunque inicialmente no especificó el mecanismo.)_ |
| _(RNF-04 Confidencialidad de la información)_ | _(✏️)_ | _(Se determinó que cada usuario debe tener acceso únicamente a su propia información financiera.)_                                                          |
| _(RNF-05 Fiabilidad e integridad)_            | _(✏️)_ | _(El cliente indicó que una falla puede afectar al usuario; se precisa que los datos almacenados deben conservarse correctamente)_                          |
| _(RNF-06 Fiabilidad del componente de IA)_    | _(❌)_ | _(Este comportamiento no fue tratado en la entrevista original y surge al incorporar posteriormente el componente obligatorio de IA.)_                      |

- Los ❌ no se borran: pasan a **preguntas para el cliente del proyecto**. Pueden ser requisitos válidos que el cliente no mencionó, o suposiciones del equipo.

---

## 6. Plan con el cliente del proyecto

La entrevista de hoy es un ensayo. La elicitación que cuenta para la Nota 1 es con el **cliente del proyecto**, siempre **externo al equipo**. Se usa el primer nivel posible:

1. **Usuario real** del dominio. Si un integrante trabaja en el lugar, su papel es conseguir la cita con quien vive el proceso _(jefe, almacenista, cliente)_, no ser el entrevistado.
2. **Usuario sustituto**: alguien que hace esa actividad en otro lugar, aunque no vaya a usar el sistema.
3. **Equipo cliente**: el equipo que hizo de cliente hoy. En este caso la técnica complementaria es obligatoria: **análisis de documentos o de sistemas similares** _(formatos, planillas, aplicaciones parecidas)_, para que los requisitos no dependan solo de lo que el otro equipo imagine.

| Campo                                                    | Respuesta                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Cliente del proyecto _(nivel 1, 2 o 3 y rol, no nombre)_ | _(Nivel 3, equipo cliente)_                                                                                                                                                                                                                                                                                                          |
| Técnica principal y técnica complementaria               | _(entrevista + análisis de documentos)_                                                                                                                                                                                                                                                                                              |
| Fecha y lugar                                            | _(21/09/2026)_                                                                                                                                                                                                                                                                                                                       |
| Responsables                                             | _(Steven Cortes (entrevistador) Camila Gomez (anotadora))_                                                                                                                                                                                                                                                                           |
| Evidencia que se va a recoger                            | _(grabación con consentimiento)_                                                                                                                                                                                                                                                                                                     |
| Preguntas que se añaden al guion tras el taller          | _(. 1¿Se deben poder editar y eliminar los gastos e ingresos registrados? 2. ¿La aplicación debe permitir crear un presupuesto mensual? 3. ¿Se debe mostrar el saldo disponible? 4. ¿La aplicación debe generar alertas cuando se acerque al límite del presupuesto? 5. ¿Qué datos debe contener cada registro de ingreso o gasto?)_ |

- Añadir la tarjeta de la entrevista real al tablero, dentro del **Sprint 1**, con responsable y fecha.

---

## Ejemplo diligenciado

Referencia de nivel de detalle. Mismo dominio de los Talleres 1 y 2: **no se puede usar.**

**1. Guion** _(barbería de barrio; extracto)_

| #   | Pregunta                                                                                  | Tipo         |
| --- | ----------------------------------------------------------------------------------------- | ------------ |
| P1  | ¿Cómo se agenda hoy un turno, desde que el cliente llama hasta que se sienta en la silla? | Contexto     |
| P3  | ¿Qué es lo que más le complica del día a día con los turnos?                              | Abierta      |
| P4  | ¿Por qué? ¿Me cuenta la última vez que pasó?                                              | Sondeo       |
| P6  | ¿Qué pasa cuando un cliente no llega?                                                     | Excepción    |
| P7  | ¿Y cuando un barbero falta sin avisar?                                                    | Excepción    |
| P9  | ¿Cuántos turnos atienden en un sábado? ¿Cuántos clientes llaman al tiempo?                | Cuantitativa |
| P10 | ¿Cuánto tiempo está dispuesto a dedicarle al sistema al día?                              | Cuantitativa |
| P12 | ¿Hay algo que no le pregunté y debería saber?                                             | Cierre       |

**2. Notas** _(extracto)_

- **P3:** "Los sábados el teléfono no para y mientras contesto no corto."
- **P6:** "Unos dos o tres por semana no llegan y ese turno se pierde."
- **P9:** "Unos 40 turnos el sábado, entre los tres."
- **Observador:** el "cliente" dice _"agenda"_ para el cuaderno y _"turno"_ para cada cita; usar esos términos en el catálogo.

**4. Requisitos candidatos** _(extracto)_

| ID     | Descripción                                                                                                                   | Prioridad | Fuente  |
| ------ | ----------------------------------------------------------------------------------------------------------------------------- | --------- | ------- |
| RF-01  | El sistema debe permitir al cliente reservar un turno eligiendo barbero, fecha y franja libre                                 | Must      | P1, P3  |
| RF-02  | El sistema debe permitir al barbero marcar un turno como no asistido                                                          | Should    | P6      |
| RF-03  | El sistema debe reasignar los turnos de un barbero ausente o notificar a sus clientes                                         | Should    | P7      |
| RNF-01 | _(Eficiencia de desempeño)_ El sistema soporta 40 reservas en un día y 10 consultas simultáneas, respondiendo en menos de 2 s | Must      | P9      |
| RNF-02 | _(Usabilidad)_ El dueño registra un turno telefónico en menos de 30 s                                                         | Should    | P3, P10 |

**Ambigüedad:** ¿el cliente reserva con un barbero concreto o con el primero libre? Se pregunta al dueño real.

**5. Validación:** RF-01 ✅, RF-02 ✅, RF-03 ✏️ _("no reasigno, los llamo yo")_ → pasa a "notificar a los clientes"; RNF-02 ❌ _("no dije tiempo")_ → pregunta para el cliente del proyecto.

**6. Plan:** entrevista al dueño el lunes a las 8:00 en la barbería, antes de abrir, + fotos de dos páginas del cuaderno de turnos _(análisis de documentos)_. Responsables: entrevistador y anotador del taller. Tarjeta creada en el tablero.
