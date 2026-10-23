import os

from model.usuario import Usuario
from model.gasto import Gasto
from model.presupuesto import Presupuesto


class FinanzasController:
    def __init__(self):
        self.usuario_actual = None

        self.ruta_datos = "datos"
        self.archivo_usuarios = "datos/usuarios.txt"
        self.archivo_gastos = "datos/gastos.txt"
        self.archivo_presupuestos = "datos/presupuestos.txt"

        os.makedirs(self.ruta_datos, exist_ok=True)

        open(self.archivo_usuarios, "a", encoding="utf-8").close()
        open(self.archivo_gastos, "a", encoding="utf-8").close()
        open(self.archivo_presupuestos, "a", encoding="utf-8").close()

    def sesion_iniciada(self):
        return self.usuario_actual is not None

    def cerrar_sesion(self):
        self.usuario_actual = None

    def crear_usuario(self, id_usuario, correo, contrasena):

        with open(self.archivo_usuarios, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")

                if datos[0] == str(id_usuario):
                    raise ValueError("Ya existe un usuario con ese ID")

                if datos[1] == correo:
                    raise ValueError("Ya existe un usuario con ese correo")

        usuario = Usuario(id_usuario, correo, contrasena)

        with open(self.archivo_usuarios, "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{usuario.id_usuario};{usuario.correo};{usuario.contrasena}\n"
            )

        return usuario

    def iniciar_sesion(self, correo, contrasena):

        with open(self.archivo_usuarios, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")

                if len(datos) < 3:
                    continue

                id_usuario = datos[0]
                correo_guardado = datos[1]
                contrasena_guardada = datos[2]

                if correo_guardado == correo:
                    usuario = Usuario(
                        int(id_usuario), correo_guardado, contrasena_guardada
                    )

                    if usuario.autenticar(contrasena):
                        self.usuario_actual = usuario
                        return True

        return False

    def registrar_gasto(self, valor, fecha, categoria):

        if self.usuario_actual is None:
            raise ValueError("Debe iniciar sesion primero")

        id_gasto = self.obtener_siguiente_id(self.archivo_gastos)

        gasto = Gasto(id_gasto, valor, fecha, categoria)

        if not gasto.validar_datos():
            raise ValueError("Los datos del gasto no son validos")

        with open(self.archivo_gastos, "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{gasto.id_movimiento};"
                f"{self.usuario_actual.id_usuario};"
                f"{gasto.valor};"
                f"{gasto.fecha};"
                f"{gasto.categoria}\n"
            )

        return gasto

    def consultar_gastos(self):

        if self.usuario_actual is None:
            raise ValueError("Debe iniciar sesion primero")

        with open(self.archivo_gastos, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")

                if len(datos) < 5:
                    continue

                if datos[1] == str(self.usuario_actual.id_usuario):
                    yield Gasto(int(datos[0]), float(datos[2]), datos[3], datos[4])

    def crear_presupuesto(self, valor_limite, mes, anio):

        if self.usuario_actual is None:
            raise ValueError("Debe iniciar sesion primero")

        with open(self.archivo_presupuestos, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")

                if len(datos) < 5:
                    continue

                if (
                    datos[1] == str(self.usuario_actual.id_usuario)
                    and datos[3] == str(mes)
                    and datos[4] == str(anio)
                ):
                    raise ValueError("Ya existe un presupuesto para ese periodo")

        id_presupuesto = self.obtener_siguiente_id(self.archivo_presupuestos)

        presupuesto = Presupuesto(id_presupuesto, valor_limite, mes, anio)

        with open(self.archivo_presupuestos, "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{presupuesto.id_presupuesto};"
                f"{self.usuario_actual.id_usuario};"
                f"{presupuesto.valor_limite};"
                f"{presupuesto.mes};"
                f"{presupuesto.anio}\n"
            )

        return presupuesto

    def consultar_presupuestos(self):

        if self.usuario_actual is None:
            raise ValueError("Debe iniciar sesion primero")

        with open(self.archivo_presupuestos, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")

                if len(datos) < 5:
                    continue

                if datos[1] == str(self.usuario_actual.id_usuario):
                    yield Presupuesto(
                        int(datos[0]), float(datos[2]), int(datos[3]), int(datos[4])
                    )

    def obtener_siguiente_id(self, ruta_archivo):

        ultimo_id = 0

        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")

                if len(datos) > 0 and datos[0].isdigit():
                    ultimo_id = int(datos[0])

        return ultimo_id + 1
