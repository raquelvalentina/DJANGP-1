'''clase, 2 atributos area y base metodo calsular '''
print('''   AREA DE UN TRIANGULO''')
class tr:
    def __init__(self,bc, h):
        self.bc = bc
        self.h = h
    def mtd(self):
        print(f'area de un rectangulo: {self.bc * self.h}')

def loop(again):
    while again == 1:
        bc = float(input('proporcione la base: '))
        h = float(input('Proporcione la altura: '))
        rct = tr(bc, h)
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

