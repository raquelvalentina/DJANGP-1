from objct import *
class pc:
    cntr = 0
    def __init__(self, name, mn, tcl, ms):
        pc.cntr += 1
        self.idpc = pc.cntr
        self.name = name
        self._mn = mn
        self._tcl = tcl
        self._ms = ms
    def __str__(self) -> object:
        return f''' COOMPUTADORA [{self.name}] ID: [{self.idpc}]
                    monitor; {self._mn}
                    tcl : {self._tcl}
                    ms : {self._ms}'''

class ordn:
    id = 0
    def __init__(self, pc):
        ordn.id += 1
        self._idordn = ordn.id
        self._pc = pc
    def agr(self,pcs):
        self._pc.append(pcs)
    def __str__(self):
        pc_str = ''
        for pcs in self._pc:
            pc_str += pcs.__str__()
        return f'''
                    group: {self._idordn}
                    PC: {pc_str}'''

if __name__ == '__main__':
    teclado1 = tcl('HP', 'USB')
    raton1 = ms('HP', 'USB')
    monitor1 = mn('HP', 15)
    computadora1 = pc('HP', monitor1, teclado1, raton1)
    print(computadora1)
    teclado2 = tcl('Acer', 'Bluetooth')
    raton2 = ms('Acer', 'Bluetooth')
    monitor2 = mn('Acer', 27)
    computadora2 = pc('Acer', monitor2, teclado2, raton2)
    print(computadora2)
    h = [computadora1, computadora2]
    r = ordn(computadora1)

    print(r)
