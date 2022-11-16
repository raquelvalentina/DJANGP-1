class psn:
    def __init__(self,nombre,apellido,edad, *listas, **dicconario):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.listas = listas
        self.diccionario = dicconario
        print(nombre, apellido, edad, listas,dicconario)

'''modificar los objetos'''

per1 = psn('juan', 'perez', 43, 'cats', 'dogs', hm = 'homosexual')
per1.nombre = 'juanes'
per2 = psn('mae', 'lin', 23)


'''codigo del profe'''


class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')

persona1 = Persona('Juan', 'Perez', 28, '44553322', 2, 3, 5, m='manzana', p='pera')
persona1.mostrar_detalle()

persona2 = Persona('Karla', 'Gomez', 30)
persona2.mostrar_detalle()
