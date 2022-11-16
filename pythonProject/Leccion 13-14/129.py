# las metodos de lcase son similares a los metodos de clase

class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

MiClase.metodo_clase()


'''----------------------------------------------------------------------------'''

# variable de clases

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        print(firstname, lastname)

    @classmethod
    def from_fullname(cls, fullname):
        cls.firstname, cls.lastname = fullname.split(' ', 1)
        print(cls.firstname, cls.lastname)


prn = Person('Raquel', 'herrera')


prn.from_fullname('Raquel herrera')