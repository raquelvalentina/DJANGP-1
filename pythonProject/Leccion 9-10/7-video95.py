'''definir metodos'''

class psn:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mdtlle(self):
        print(f'persona: {self.nombre}, {self.apellido}, {self.edad} ')

per1 = psn('juan', 'perez', 43)
per1.mdtlle()

per2 = psn('mae', 'lin', 23)
per2.mdtlle()