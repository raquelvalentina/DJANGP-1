# UML modelar programas

# 1 class prodct
# +ontador de productos
# id del prodcto
# namw
# precio

# 2 class ordn
# countr
# id
# productos en lista

class prdc:
    countr = 0
    def __init__(self , name, prc):
        prdc.countr += 1
        self._id = prdc.countr
        self._name = name
        self._prc = prc

    @property
    def prcio(self):
        return self._prc
    def __str__(self):
        return f' PRODUCTO: --{self._name} ... {self._prc} $ [ID.{self._id}]'





class orden:
    countr2 = 0
    def __init__(self, listt):
        orden.countr2 +=1
        self.id = orden.countr2
        self._list = list(listt)

    def hh(self, obj):
        self._list.append(obj)
    def cl(self):
        ll = 0
        for obj in self._list:
            ll += obj.prcio
        return ll
    def __str__(self):
        list_str = ''
        for obj in self._list:
            list_str += obj.__str__() + '|'
            return f'{self.id}, precio {list_str}, {orden.cl}'


rr = prdc('pasta', 14)
rr1 = prdc('pasta', 14)
rr2 = prdc('pasta', 14)
d = [rr, rr1, rr2]
h = orden(d)
print(h)

producto1 = prdc('Camisa', 100.00)
producto2 = prdc('Pantalón', 150.00)
productos1 = [producto1, producto2]
orden1 = orden(productos1)
print(orden1)
orden2 = orden(productos1)
print(orden2)

