# sintaxis de range
#
# rango de 0 a 10 imprimir  valores divicibles entre 3
#
# crae un rango de numeero de 2 a 6 e imprimirlos
#
# rango de 3 a 10 incremento de 2 en 2
print('ejercicio #1')
for i in range(11):
    if i % 3 != 0:
        continue
    print(f"valor:{i}")

print('ejercicio #2')
w = range(2,7)
for n in w:
    print('valor', n)

print('ejercicio #3')
w = range(3,11,2)
for n in w:
    print('valor', n)