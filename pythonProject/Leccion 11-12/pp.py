# se va a creer una clase de persona de name a apellido la clase hija va tener el sueldo empleado
class prn:
    def __init__(self, name, edad):
        self.name = name
        self.edad = edad

    def __str__(self):
        return f'persona : {self.name} // edad: {self.edad} years old // '

'''clase hija'''
class empld(prn):
    def __init__(self, name, edad, sueldo):
        self.sueldo = sueldo
        super().__init__(name, edad)
    def __str__(self):
        return f'{super().__str__()} sueldo : {self.sueldo}'
