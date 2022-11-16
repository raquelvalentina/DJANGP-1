"""
Ejercicio: Convertidor de Temperatura
Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.
"""
def clc (C):
    prp = (C*9/5)+32
    return prp

def frh (F):
    prp = (F-32)*5/9
    return prp

def loop(again):
    while again == 1:
        slccn = int(input('''
            1- celcius a farenheint
            2- farenheit a celcius
              (seleccione 1 o 2)
              :'''))
        if slccn == 1:
            C = float(input('grados celcius: '))
            rtd = clc(C)
            print(f'{C}°C son {rtd}°F')

        elif slccn == 2:
            F = float(input('grados farenheit: '))
            rtd = frh(F)
            print(f'{F}°F son {rtd}°C')
        else:
            print('no esta en el menu')

        again = int(input('''quiere continuar?
        SI = 1  ,  NO = 0
        __ '''))
    if again == 0:
        print('FINAL DEL PROGRAMA')
    else:
        print('FINAL')
loop(1)

