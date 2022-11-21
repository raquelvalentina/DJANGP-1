class dadclas:
    def __init__(self, typ, mrk):
        self.typ = typ
        self.mrk = mrk

class ms(dadclas):
    n=0
    def __init__(self, mrk, typ):
        ms.n += 1
        self.idms = ms.n
        super().__init__(typ, mrk)
    def __str__(self):
        return f'ID; [{self.idms}]  |  Marca; [{self.mrk}]  |  Tipo de entrada; [{self.typ}]'
class tcl(dadclas):
    n = 0
    def __init__(self, typ, mrk):
        tcl.n += 1
        self.idtcl = tcl.n
        super().__init__(typ, mrk)

    def __str__(self):
        return f'ID; [{self.idtcl}]  |  Marca; [{self.mrk}]  |  Tipo de entrada; [{self.typ}]'

class mn(dadclas):
        n = 0
        def __init__(self, mrk, tnie):
            tcl.n += 1
            self.idmn = mn.n
            self._mrk = mrk
            self._tnie = tnie

        def __str__(self):
            return f'ID; [{self.idmn}]  |  Marca; [{self._mrk}]  |  Size; [{self._tnie}]'

