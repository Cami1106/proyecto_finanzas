class Movimiento:

    def __init__(self, id_movimiento, valor, fecha):
        self.id_movimiento = id_movimiento
        self.valor = valor
        self.fecha = fecha

    def modificar(self, valor, fecha):
        self.valor = valor
        self.fecha = fecha

    def validar_datos(self):
        return self.valor > 0 and self.fecha != ""