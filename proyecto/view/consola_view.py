class ConsolaView:

    def __init__(self, controller):
        self.controller = controller

    def iniciar(self):

        while True:

            if self.controller.usuario_actual is None:
                continuar = self.menu_acceso()

            else:
                continuar = self.menu_finanzas()

            if not continuar:
                break

    def menu_acceso(self):

        print("==============================")
        print("      ACCESO AL SISTEMA")
        print("==============================")
        print("1. Crear usuario")
        print("2. Iniciar sesion")
        print("3. Salir")
        print("==============================")

        opcion = input("Seleccione una opcion: ")
        print()

        if opcion == "1":
            self.crear_usuario()

        elif opcion == "2":
            self.iniciar_sesion()

        elif opcion == "3":
            print("Programa finalizado")
            return False

        else:
            print("Opcion no valida")

        print()
        return True

    def menu_finanzas(self):

        print("==============================")
        print("     FINANZAS PERSONALES")
        print("==============================")
        print("1. Registrar gasto")
        print("2. Consultar gastos")
        print("3. Crear presupuesto")
        print("4. Consultar presupuestos")
        print("5. Cerrar sesion")
        print("6. Salir")
        print("==============================")

        opcion = input("Seleccione una opcion: ")
        print()

        if opcion == "1":
            self.registrar_gasto()

        elif opcion == "2":
            self.consultar_gastos()

        elif opcion == "3":
            self.crear_presupuesto()

        elif opcion == "4":
            self.consultar_presupuestos()

        elif opcion == "5":
            self.controller.cerrar_sesion()
            print("Sesion cerrada correctamente")

        elif opcion == "6":
            print("Programa finalizado")
            return False

        else:
            print("Opcion no valida")

        print()
        return True

    def crear_usuario(self):

        print("--- CREAR USUARIO ---")

        id_usuario = int(input("ID del usuario: "))
        correo = input("Correo: ")
        contrasena = input("Contraseña: ")

        usuario = self.controller.crear_usuario(
            id_usuario,
            correo,
            contrasena
        )

        print("Usuario creado correctamente:", usuario.correo)

    def iniciar_sesion(self):

        print("--- INICIAR SESION ---")

        correo = input("Correo: ")
        contrasena = input("Contraseña: ")

        resultado = self.controller.iniciar_sesion(
            correo,
            contrasena
        )

        if resultado:
            print("Sesion iniciada correctamente")
        else:
            print("Correo o contraseña incorrectos")

    def registrar_gasto(self):

        print("--- REGISTRAR GASTO ---")

        valor = float(input("Valor del gasto: "))
        fecha = input("Fecha: ")
        categoria = input("Categoria: ")

        gasto = self.controller.registrar_gasto(
            valor,
            fecha,
            categoria
        )

        print("Gasto registrado con ID:", gasto.id_movimiento)

    def consultar_gastos(self):

        print("--- GASTOS REGISTRADOS ---")

        encontrado = False

        for gasto in self.controller.consultar_gastos():

            encontrado = True

            print("----------------------")
            print("ID:", gasto.id_movimiento)
            print("Valor:", gasto.valor)
            print("Fecha:", gasto.fecha)
            print("Categoria:", gasto.categoria)

        if not encontrado:
            print("No hay gastos registrados")

    def crear_presupuesto(self):

        print("--- CREAR PRESUPUESTO ---")

        valor_limite = float(input("Valor limite: "))
        mes = int(input("Mes: "))
        anio = int(input("Año: "))

        presupuesto = self.controller.crear_presupuesto(
            valor_limite,
            mes,
            anio
        )

        print("Presupuesto creado correctamente")
        print("Valor limite:", presupuesto.valor_limite)

    def consultar_presupuestos(self):

        print("--- PRESUPUESTOS REGISTRADOS ---")

        encontrado = False

        for presupuesto in self.controller.consultar_presupuestos():

            encontrado = True

            print("----------------------")
            print("ID:", presupuesto.id_presupuesto)
            print("Valor limite:", presupuesto.valor_limite)
            print("Mes:", presupuesto.mes)
            print("Año:", presupuesto.anio)

        if not encontrado:
            print("No hay presupuestos registrados")