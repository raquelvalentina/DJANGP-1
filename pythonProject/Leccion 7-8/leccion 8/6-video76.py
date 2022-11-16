"""
Crear una función para sumar los valores recibidos de tipo numérico,
utilizando argumentos variables *args como parámetro de la función
y regresar como resultado la suma de todos los valores pasados como argumentos.
"""

# def sma (*values):
#     for value in values:
#         a = int(value)
#         print(a)
#         print(type(a))
# b = sma()
# print(f'Resultado sumar: {b}')
# sma('7', '8', '5', '7')

'''SOLUCIIIIIIIIIION'''

def sma(*args):
    rtd = 0
    for arg in args:
        if arg == str(arg):
            a = int(arg)
            rtd += a
        else:
            rtd += arg
    return rtd
print(sma(7, 7, 5, 8))
print(sma('7', '8', '5', '7'))
