class Usuario:

    def __init__(self, id_usuario, correo, contrasena):
        self.id_usuario = id_usuario
        self.correo = correo
        self.contrasena = contrasena
        self.movimientos = []
        self.presupuestos = []