
# Como crear una varible de clase
# estas son llamadas de frma aparte y definidas dentro de la clae
class MiClase:

    variable_clase = 'Valor variable clase'                                               '''variable de clase'''
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
# llamada a la varible de clase
print(MiClase.variable_clase)


# variable de instancia se define y luego se lllama y dependera de cada objeto

miClase = MiClase('Valor variable instancia')
print(miClase.variable_instancia)
print(miClase.variable_clase)

