# poliformismo en python
# multiples formas en tiempo de ejecucion
# multiples metodos en tiempos de ejecucion

class emplL:
    def __init__(self,name, sld):
        self.name = name
        self.sld = sld

    def __str__(self):
        return f'Nombre del empleado: [{self.name}], salario del empleado: [{self.sld}] '

class grnt(emplL):
    def __init__(self, name, sld, empl):
        super().__init__(name, sld)
        self.empl = empl
    def __str__(self):
        return f'CAMPO: [{self.empl}], {super().__str__()}'

def prnt (obj):
    print(obj.__str__())

    '''si el obj pertenece a la clase GeReNTe imprimira los atributos indicados del objeto'''
    if isinstance(obj, grnt):
        print(obj.empl)
        print(obj.name)
        print(obj.sld)

ll = emplL('RAQUEL', 450)
prnt(ll)


lk = grnt('FABIO', 0, 'sis')
prnt(lk)
