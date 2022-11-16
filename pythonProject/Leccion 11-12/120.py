from cccc import fg
from cccc import color1

#solucion clases hijas

class cuadrado(fg, color1):
    def __init__(self, lado, color):
        fg.__init__(self, lado, lado)
        color1.__init__(self, color)

    def area(self):
        return self._alto * self._ancho

    def __str__(self):
        return f'area del cuadrado {self.area()} de color ({self._color})'

class rectangulo(fg, color1):
    def __init__(self, bc, h, color):
        fg.__init__(self, bc, h)
        color1.__init__(self, color)

    def area(self):
        return self._alto * self._ancho

    def __str__(self):
        return f'area del rectangulo {self.area()} de color ({self._color})'