# Contecto estatico y cotexto dinamico



class MiClase:

    variable_clase = 'Valor variable clase'
# '''contexto dinamico '''
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
# '''contexto estatico '''
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

 # '''contexto estatico '''
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase, cls.variable_instancia)

MiClase(1)