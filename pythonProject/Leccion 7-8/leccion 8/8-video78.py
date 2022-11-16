"""
Crear una función para multiplicar los valores recibidos de tipo numérico,
utilizando argumentos variables *args como parámetro de la función
y regresar como resultado la multiplicación de todos los valores pasados como argumentos.
"""
def sma(*args):
    rtd = 1
    for arg in args:
            rtd *= arg
    return rtd
print(sma(7, 7, 5, 8))
