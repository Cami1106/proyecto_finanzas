# Ficha de equipo y dominio — Sesión 1

Plantilla de la **actividad de cierre de la Clase 1**. Se diligencia en clase, en equipo, y se entrega al final de la sesión.

- **Equipos:** de 2 a 3 integrantes, fijos durante todo el curso.
- **Entrega:** una ficha por equipo.
- **Cada equipo elige un dominio distinto.**

---

## 1. Identificación del equipo

| Campo | Respuesta |
|---|---|
| Nombre del equipo | _(finanzas)_ |
| Fecha | _(14/09/2026)_ |

| # | Integrante | Correo | Rol / responsabilidad |
| --- | --- | --- | --- |
| 1 | _(Andres Steven Cortes Perez)_ | _(ancortes2021@gmail.com)_ | Coordinación _(obligatorio)_ |
| 2 | _(Maria Camila Gomez Toro)_ | _(mariacamila20061104@gmail.com)_ | _(desarrolladora)_ |

> El rol no es definitivo: se ajusta en la bitácora de gestión. Lo que sí queda fijo hoy es **quién coordina**.

---

## 2. Dominio propuesto

**Dominio:** _(una línea — el sector o la actividad; e.g. "gestión de inventario para una tienda de barrio")_

**Problema que se quiere resolver** _(máximo tres líneas: qué pasa hoy, a quién le duele y por qué el proceso actual no alcanza)_:

_(La economia actual de las personas y sus finanzas, debido a que actualmente. Muchas personas tienen dificultades para controlar sus ingresos y gastos, porque no llevan un registro organizado de en que utilizan su dinero. Esto conlleva a generar gastos innecesarios, falta de ahorro y problemas financieros.)_

**Cómo se hace hoy sin software** _(o con qué herramienta improvisada: papel, WhatsApp, un Excel)_:

_(En libretas, Notas de calculo o Excel)_

---

## 3. Usuarios del sistema

| Tipo de usuario | Qué necesita hacer en el sistema | ¿Tenemos acceso para entrevistarlo? |
| --- | --- | --- |
| _(administrador)_ | _(actualizaciones y correcion de errores)_ | Sí — _(steven y camila)_ |
| _(publico)_ | _(ingresar y consultar los datos de sus finanzas)_ | Sí  — _(andres murillo)_ |

> Al menos **un usuario real y accesible** es obligatorio: en la Clase 3 hay que hacerle una sesión de elicitación de verdad.

---

## 4. Capacidad del equipo

**¿Por qué este equipo puede levantar requisitos de este dominio?** _(acceso a usuarios reales, alguien trabaja o trabajó ahí, experiencia previa con el proceso, etc.)_

_(Dado que hemos vivido la experiencia de no controlar nuestros gastos financieros, adicional de que conocemos en la actualidad como a las personas se les dificulta manejar sus cuentas en metodos no fiables o metodos muy convencionales.)_

---

## 5. Alcance tentativo

**Tres cosas que el sistema sí debe hacer**:

1. _(Registrar ingresos y gastos)
2. _(Visualizar las estadisticas de los gastos)
3. _(Clasificar los gastos por categorias segun las prioridades)

**Tres cosas que el sistema no va a hacer**:

1. _(No filtrar los datos de las demas personas al publico)
2. _(No brindar asesorias financieras profesionales)
3. _(No tendra acceso directo a las cuentas bancarias de los usuarios)

---

## 6. Autoverificación

- [x] Hay **usuarios reales accesibles** para entrevistar en la Clase 3.
- [x] El dominio da para **10 requisitos funcionales y 5 no funcionales** sin inventarlos.
- [ ] Los **tres casos críticos** se ven implementables end-to-end en seis semanas.
- [x] El proyecto **no fue desarrollado** en otra asignatura ni se está reciclando.
- [x] No es demasiado grande _(una red social completa)_ ni demasiado pequeño _(una calculadora)_.
- [x] El sistema **maneja datos personales**: Sí / No. Si es Sí, aplica la Ley 1581 de 2012 en el numeral 10 de la Nota 1.

---

## Ejemplo diligenciado

Referencia de nivel de detalle esperado. **No se puede usar este dominio.**

- **Dominio:** control de turnos en una barbería de barrio con tres sillas.
- **Problema:** los turnos se anotan en un cuaderno; los clientes llegan sin saber la espera y se van, y el dueño no sabe cuánto factura cada barbero al mes.
- **Hoy:** cuaderno físico y llamadas telefónicas.
- **Usuarios:** cliente _(reserva y consulta su turno)_, barbero _(ve su agenda del día)_, administrador _(cierra caja y ve el reporte mensual)_. Acceso real: el tío de un integrante es dueño del local.
- **Sí hace:** reservar turno, ver agenda del día por barbero, cerrar caja con reporte de ingresos.
- **No hace:** pagos en línea, domicilios, inventario de productos.

---

## Flujo del Proyecto

```bash
UI → Controlador → ServicioIA «interfaz» → AdaptadorProveedor → API del modelo → AdaptadorSimulado → respuesta fija (pruebas)
```