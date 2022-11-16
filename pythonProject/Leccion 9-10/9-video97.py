'''nueva claseeeeeeeeeee'''

class artmk:
    """clase aritmetica"""
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def mas(self):
        return self.a + self.b
    def mns(self):
        return self.a - self.b
    def por(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b

artt1 = artmk(7,6)

print(f'suma: {artmk.mas()} resta: {artmk.mns()} multiplicar: {artmk.por()} dividir: {artmk.div()}')