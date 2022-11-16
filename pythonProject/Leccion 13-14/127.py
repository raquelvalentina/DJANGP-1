class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

miClase = ('valor de la varible de intancia')
print(MiClase.variable_clase)

# las varibles de clase se pueden agrar desde fuera de la clase y puede ser llamadas desde los objetos
MiClase.variable_clase2 = 'Valor variable clase 2'                 '''<----'''


print(MiClase.variable_clase2)
print(miClase.variable_clase2)
