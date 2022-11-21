'''objetos'''
from lab import *
from sub import ordn

class mn(pc, dadclas):
    def __init__(self, mrk):
        self.mrk = mrkobjb = mn('love')
        self.idpc = pc.cntr
        self.tnie = pc.monitor
    def __str__(self):
        return f'ID; [{self.idpc}]  |  Marca; [{self.mrk}]  |  Size; [{pc.monitor}]'



class tcl(pc,dadclas):
    def __init__(self, mrk):
        self.idtcl = pc.cntr
        self.mrk = str(mrk)
        self.tpy = dadclas.entrada

    def __str__(self):
        return f'ID; [{self.idtcl}]  |  Marca; [{self.mrk}]  |  Tipo de entrada; [{self.tpy}]'

class ms(pc,dadclas):
    def __init__(self, mrk):
        self.idms = pc.cntr
        self.mrk = str(mrk)
        self.tpy = dadclas.entrada

    def __str__(self):
        return f'ID; [{self.idms}]  |  Marca; [{self.mrk}]  |  Tipo de entrada; [{self.tpy}]'

