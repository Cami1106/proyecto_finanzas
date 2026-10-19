class Presupuesto:

    def __init__(self, id_presupuesto, valor_limite, mes, anio):
        self.id_presupuesto = id_presupuesto
        self.valor_limite = valor_limite
        self.mes = mes
        self.anio = anio

    def actualizar_limite(self, nuevo_limite):
        self.valor_limite = nuevo_limite