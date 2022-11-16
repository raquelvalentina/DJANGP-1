'''1—-
clase y objetos en python clase de tipo persona por la cual se van a poder crear objetos a esto se la llama instancia
POO: programacion orientada a objetos
class para crear una clase
'''
class psn:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        print(nombre, apellido, edad)

per1 = psn('juan', 'perez', 43)
per2 = psn('mae', 'lin', 23)