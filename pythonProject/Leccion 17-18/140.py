# poliformismo en python
# multiples formas en tiempo de ejecucion
# multiples metodos en tiempos de ejecucion

class emplL:
    def __init__(self,name, sld):
        self.name = name
        self.sld = sld

    def __str__(self):
        return f'{self.name}, {self.sld} '

class grnt(emplL):
    def __init__(self,name, sld, empl):
        super().__init__(name,sld)
        self.empl = empl
    def __str__(self):
        return f'{self.empl}, {super().__str__()}'

def prnt (obj):
    print(obj.__str__())
    if isinstance(obj, grnt):
        print(obj.empl)

ll = emplL('rauqle', 450)
prnt(ll)
print(ll)

lk = grnt('rauqle', 450, 'sis')
prnt(lk)
print(lk)