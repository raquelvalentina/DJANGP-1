# HERENCIA MULTIPLE EN PYTHON
# va heredar caracterizticas de multiples clases
# FG : alto, ancho
# color: color
# cuadarado: area


# clase padre
class fg:
    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho
    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho



# clase padre

class color1:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color
'''----------------------------------------------- HIJAS ------------------------------------------------------------'''

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
