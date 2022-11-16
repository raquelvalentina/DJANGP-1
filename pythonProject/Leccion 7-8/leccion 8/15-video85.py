"""
Ejercicio: Calculadora de Impuestos
Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
# Formula:
"""

def imp ():
    pago_sin_impuesto = float(input('Cantidad a pagar: '))
    impuesto = float(input('monto del impuesto:'))
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    print(pago_total)

imp()
