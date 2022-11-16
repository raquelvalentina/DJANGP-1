# sobrecarga de operadores en python para agregarlos a las clases

'''magic method'''

# no se que es eso
# operador +
a = 2
b = 3
print(a + b)

a = 'Hola '
b = 'Mundo'
print(a + b)

a = [1,2,3]
b = [6,7,8]
print(a + b)
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, otro):
        return f'{self.nombre} {otro.nombre}'

    def __sub__(self, otro):
        return self.edad - otro.edad


persona1 = Persona('Juan', 28)
persona2 = Persona('Carlos', 20)
print(persona1 + persona2)
print(persona1 - persona2)

