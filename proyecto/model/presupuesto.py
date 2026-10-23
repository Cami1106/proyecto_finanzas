class Presupuesto:

    def __init__(self, id_presupuesto, valor_limite, mes, anio):
        self.id_presupuesto = id_presupuesto
        self.valor_limite = valor_limite
        self.mes = mes
        self.anio = anio

    def actualizar_limite(self, nuevo_limite):
        self.valor_limite = nuevo_limite

    def calcular_porcentaje_consumido(self, total_gastos):
        return (total_gastos / self.valor_limite) * 100

    def esta_cerca_del_limite(self, total_gastos):
        porcentaje = self.calcular_porcentaje_consumido(total_gastos)
        return porcentaje >= 80

    def supera_limite(self, total_gastos):
        return total_gastos > self.valor_limite