class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
    # los metods estaticos no agregan nada nuevo a la varible tiene que ser llamadas aparte
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)
# llamda al metyodo estatico
MiClase.metodo_estatico()
