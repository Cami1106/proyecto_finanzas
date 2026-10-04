# Taller 5 · Diagrama de clases

- **Entrega:** en el **repositorio del equipo en GitHub**, diligenciando el enunciado con los puntos 2, 3 y 4 y subiendo el diagrama al repositorio *(imagen exportada o fuente PlantUML/draw.io)*.
- **Requisito previo:** diagrama de casos de uso del Taller 4.
- Herramienta: draw.io, PlantUML, StarUML o Visual Paradigm.

---

## 1. Guía mínima

**Diagrama de clases:** vista estructural del sistema. Muestra qué cosas existen en el dominio, qué datos guardan, qué saben hacer y cómo se relacionan. No muestra orden ni tiempo: eso es de los diagramas de secuencia.

### Clase

```bash
┌──────────────────────┐
│       Turno          │  ← nombre: sustantivo singular, del vocabulario del dominio
├──────────────────────┤
│ - fecha: Fecha       │  ← atributos: visibilidad nombre: tipo
│ - estado: EstadoTurno│
├──────────────────────┤
│ + cancelar(): void   │  ← métodos: visibilidad nombre(parámetros): retorno
└──────────────────────┘
```

- **Visibilidad:** `+` pública, `-` privada, `#` protegida, `~` de paquete. Los atributos van privados por defecto.
- En el **modelo de dominio** se pueden omitir los métodos: importan los conceptos, sus datos y sus relaciones.
- Una clase **no es una pantalla, una tabla ni un botón**. `PantallaLogin` o `BotonGuardar` no son conceptos del dominio.

### Relaciones

| Relación        | Notación                                  | Se lee                           | Ejemplo                  |
| --------------- | ----------------------------------------- | -------------------------------- | ------------------------ |
| **Asociación**  | línea simple                              | "A se relaciona con B"           | Cliente — Turno          |
| **Agregación**  | rombo vacío en el todo                    | "A tiene B, pero B existe sin A" | Barbería ◇— Barbero      |
| **Composición** | rombo lleno en el todo                    | "B es parte de A y muere con A"  | Factura ◆— LíneaFactura  |
| **Herencia**    | flecha con triángulo vacío hacia el padre | "B es un tipo de A"              | Usuario ◁— Administrador |
| **Dependencia** | flecha punteada                           | "A usa a B de paso"              | Reporte ⇢ Turno          |

- Ante la duda entre agregación y composición: si al borrar el todo **las partes no tienen sentido solas**, es composición.
- Herencia solo si el hijo **es un** padre y comparte su comportamiento. Si solo comparten un campo, no es herencia.

### Multiplicidad

Se escribe en cada extremo de la relación: cuántos objetos de ese lado se relacionan con **uno** del otro.

| Notación | Significa |
| --- | --- |
| `1` | exactamente uno |
| `0..1` | cero o uno |
| `*` o `0..*` | cero o muchos |
| `1..*` | uno o muchos |

- `Cliente 1 —— 0..* Turno`: un cliente tiene cero o muchos turnos; cada turno es de exactamente un cliente.
- Una relación sin multiplicidad está incompleta.

### Navegabilidad

- Flecha abierta en un extremo: desde A se llega a B, pero no al revés.
- En el modelo de dominio se puede dejar sin flecha *(bidireccional)*; se decide en el diseño.

### Cómo encontrar las clases

1. Subrayar los **sustantivos** del catálogo de requisitos y de las descripciones de los casos de uso.
2. Descartar sinónimos, atributos disfrazados *(el "nombre" no es una clase)*, actores que no guardan datos y cosas fuera del alcance.
3. Lo que queda son **clases candidatas**. Los **verbos** entre ellas sugieren relaciones.

---

## 2. Clases candidatas

| Clase candidata | Fuente *(RF o caso de uso)* | ¿Se queda? | Por qué |
| --- | --- | --- | --- |
| Usuario | RF-11, RF-12, RF-15 / CU-11, CU-12, CU-15 | Sí | Representa a la persona que utiliza el sistema y es propietaria de su información financiera. |
| Movimiento | RF-01, RF-02, RF-03, RF-04, RF-06 / CU-01, CU-02, CU-03 | Sí | Representa un movimiento financiero registrado por el usuario y reúne información común como valor, fecha y descripción. |
| Ingreso | RF-02 / CU-02 | Sí | Representa un tipo de movimiento que aumenta el saldo disponible del usuario. |
| Gasto | RF-01, RF-05 / CU-01, CU-04 | Sí | Representa un tipo de movimiento que disminuye el saldo y puede asociarse a una categoría. |
| Categoria | RF-05 / CU-04 | Sí | Permite organizar y clasificar los gastos registrados por el usuario. |
| Presupuesto | RF-09, RF-10 / CU-06, CU-09 | Sí | Representa el límite de gasto definido por el usuario para un periodo mensual. |
| AlertaPresupuesto | RF-10 / CU-09 | Sí | Representa el aviso generado cuando el usuario se acerca o supera el presupuesto establecido. |
| AnalisisIA | RF-14 / CU-14 | Sí | Guarda el resultado generado por la inteligencia artificial a partir de los movimientos financieros del usuario. |
| Historial | RF-06 / CU-03 | No | No es una entidad independiente; corresponde a una consulta sobre los movimientos registrados. |
| Saldo | RF-08 / CU-08 | No | Es un valor calculado a partir de los ingresos y gastos, por lo que no necesita ser una clase independiente. |
| Estadistica | RF-13 / CU-08 | No | Es información calculada a partir de los movimientos financieros y puede obtenerse cuando el usuario consulta su resumen. |
| Sistema de IA | RF-14 / CU-14 | No | Es un sistema externo que participa en el caso de uso de IA, pero no es una entidad del dominio que deba almacenarse. |
| … | | | |

- **Mínimo 6 clases** que se quedan.
- Toda clase lleva fuente. Una clase que no sale de ningún requisito o caso de uso no está en el alcance.

---

## 3. Diagrama de clases del dominio

Un solo diagrama con:

- **Mínimo 6 clases**, con atributos y tipos.
- **Mínimo 5 relaciones**, cada una con multiplicidad en los dos extremos.
- Al menos **una composición o agregación** y, si el dominio lo justifica, una **herencia**.
- Nombres en el vocabulario del dominio *(el que salió de la elicitación del Taller 3)*.
- Si el proyecto tiene componente de IA, la **entidad que guarda el resultado** del modelo *(e.g. `SugerenciaIA` con fecha, entrada, salida y estado)*. El servicio que llama a la API **no** va en este taller.

**Imagen o enlace al diagrama:** *()*

![Diagrama de clases](./diagramas/diagrama_de_clases.png)

---

## 4. Trazabilidad y dudas

**Columna de clase de la matriz**

| Requisito | Caso de uso | Clase(s)      |
| --------- | ----------- | ------------- |
| RF-01 Registrar gastos | CU-01 Registrar gasto | Usuario, Movimiento, Gasto, Categoria |
| RF-02 Registrar ingresos | CU-02 Registrar ingreso | Usuario, Movimiento, Ingreso |
| RF-03 Modificar ingresos y gastos registrados | CU-03 Gestionar movimientos registrados | Usuario, Movimiento, Ingreso, Gasto |
| RF-04 Eliminar ingresos y gastos registrados | CU-03 Gestionar movimientos registrados | Usuario, Movimiento, Ingreso, Gasto |
| RF-05 Clasificar gastos por categorías | CU-04 Clasificar gasto | Gasto, Categoria |
| RF-06 Consultar historial de ingresos y gastos | CU-03 Gestionar movimientos registrados | Usuario, Movimiento |
| RF-07 Consultar el total gastado | CU-08 Consultar saldo y resumen financiero | Usuario, Gasto |
| RF-08 Calcular y mostrar el saldo disponible | CU-08 Consultar saldo y resumen financiero | Usuario, Movimiento, Ingreso, Gasto |
| RF-09 Crear un presupuesto mensual | CU-06 Crear presupuesto mensual | Usuario, Presupuesto |
| RF-10 Generar alertas de presupuesto | CU-09 Generar alerta de presupuesto | Usuario, Presupuesto, AlertaPresupuesto, Gasto |
| RF-11 Crear una cuenta de usuario | CU-11 Crear cuenta de usuario | Usuario |
| RF-12 Autenticarse en el sistema | CU-12 Iniciar sesión | Usuario |
| RF-13 Visualizar estadísticas de gastos | CU-08 Consultar saldo y resumen financiero | Usuario, Gasto, Categoria |
| RF-14 Generar análisis financiero con IA | CU-14 Generar análisis financiero con IA | Usuario, Movimiento, AnalisisIA |
| RF-15 Cambiar contraseña | CU-15 Cambiar contraseña | Usuario |

- Cada caso crítico debe apoyarse en al menos una clase del diagrama.

-  **CU-01 Registrar gasto:** se apoya en las clases Usuario, Movimiento, Gasto y Categoria.
-  **CU-06 Crear presupuesto mensual:** se apoya en las clases Usuario y Presupuesto.
-  **CU-14 Generar análisis financiero con IA:** se apoya en las clases Usuario, Movimiento y AnalisisIA.


**Dudas para la siguiente clase** *(lo que el equipo no pudo resolver solo)*:

- *(completar)*

---

## Ejemplo diligenciado

**2. Candidatas**

| Clase candidata | Fuente            | ¿Se queda? | Por qué                                                                   |
| --------------- | ----------------- | ---------- | ------------------------------------------------------------------------- |
| Cliente         | RF-01             | Sí         | Reserva y tiene turnos                                                    |
| Turno           | RF-01, CU-01      | Sí         | Concepto central del dominio                                              |
| Barbero         | RF-02             | Sí         | Atiende turnos; tiene agenda                                              |
| Agenda          | P1 *(entrevista)* | No         | Es la lista de turnos de un barbero en un día: una consulta, no una clase |
| CierreCaja      | RF-05             | Sí         | Guarda el total del día                                                   |
| Teléfono        | RF-01             | No         | Es un atributo de Cliente                                                 |

**3. Diagrama** *(extracto en PlantUML)*

![img01](/docs/diagrams/img-01.png)

**4. Trazabilidad:** RF-01 → CU-01 Reservar turno → Cliente, Turno, Barbero. RF-02 → CU-02 Marcar no asistido → Turno *(estado)*.
