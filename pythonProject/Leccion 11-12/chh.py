class vh:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return f'Color del vehiculo: {self.color}, ruedad c/u: {self.ruedas}'
class ch(vh):
    def __init__(self, color, ruedas, velocidad):
        self.velocidad = velocidad
        super().__init__(color, ruedas)
    def __str__(self):
        return f'color de la coche: {self.color}, ruedas c/u: {self.ruedas}, velocidad del coche: {self.velocidad}'

class bc(vh):
    def __init__(self, color, ruedas, tipo):
        self.tipo = tipo
        super().__init__(color, ruedas)
    def __str__(self):
        return f'color de la bicicleta: {self.color}, ruedas c/u: {self.ruedas}, tipo de bici: {self.tipo}'
