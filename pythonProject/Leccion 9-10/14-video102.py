print('''   AREA DE UN CUBO''')


class tr:
    def __init__(self, a, h, p):
        self.a = a
        self.h = h
        self.p = p

    def mtd(self):
        print(f'area de un cubo: {self.a * self.h * self.p}')


def loop(again):
    while again == 1:
        a = float(input('proporcione la ancho: '))
        h = float(input('Proporcione la altura: '))
        p = float(input('proporciona la profundidad: '))
        rct = tr(a, h, p)
        rct.mtd()
        print('''



              ''')
        again = int(input('''quiere continuar?
                SI = 1  ,  NO = 0
                __ '''))

    if again == 0:
        print('FINAL DEL PROGRAMA')
    else:
        print('FINAL')


loop(1)