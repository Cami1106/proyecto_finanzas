from model.movimiento import Movimiento


class Gasto(Movimiento):

    def __init__(self, id_movimiento, valor, fecha, categoria):
        super().__init__(id_movimiento, valor, fecha)
        self.categoria = categoria

    def asignar_categoria(self, categoria):
        self.categoria = categoria

    def calcular_impacto_saldo(self, saldo_actual):
        return saldo_actual - self.valor