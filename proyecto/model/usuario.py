class Usuario:

    def __init__(self, id_usuario, correo, contrasena):
        self.id_usuario = id_usuario
        self.correo = correo
        self.contrasena = contrasena

    def autenticar(self, contrasena):
        return self.contrasena == contrasena

    def cambiar_contrasena(self, nueva_contrasena):
        self.contrasena = nueva_contrasena