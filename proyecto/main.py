from controller.finanzas_controller import FinanzasController
from view.consola_view import ConsolaView


controller = FinanzasController()
view = ConsolaView(controller)

view.iniciar()
