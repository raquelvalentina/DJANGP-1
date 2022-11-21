'''CLass: Computadora y dispositivos de entrada'''

class pc:
    cntr = 0
    def __init__(self, name, mn, tcl, ms):
        pc.cntr += 1
        self.idpc = pc.cntr
        self.name = str(name)
        self._mn = mn
        self._tcl = tcl
        self._ms = ms

    @property
    def monitor(self):
        return self._mn
    @monitor.setter
    def mn(self, mn):
        self._mn = mn


    @property
    def teclado(self):
        return self._tcl
    @teclado.setter
    def tcl(self, tcl):
        self._tcl = tcl

    @property
    def mouse(self):
        return self.ms
    @mouse.setter
    def ms(self, ms):
        self._ms = ms

    def __str__(self) -> object:
        return f''' COOMPUTADORA [{self.name}] ID: [{self.idpc}]'''
class dadclas:
    def __init__(self, typ, mrk):
        self._entrada = typ
        self._mrk = mrk

    @property
    def entrada(self):
        return self._entrada
    @entrada.setter
    def entrada(self, typ):
        self._entrada = mn

    @property
    def mrkk(self):
        return self._mrk
    @mrkk.setter
    def mrkk(self, mrk):
        self._mrk = mrk
    def __str__(self):
        return f'MARCA[{self._mrk}], Tipo de entrada:[{self._entrada}]'