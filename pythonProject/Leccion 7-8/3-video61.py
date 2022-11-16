nombres = ['juan', 'karla', 'ricardo', 'maria']
print("")
print(nombres)
print("")

# for nombre in nombres:
#     print(nombre)
# else:
#     print("no existe")
#
# print(len(nombres))

#para agregar nuevos elementos
print('remover --- append')
nombres.append("lorenzo")
print(nombres)
#incertar en un indice determinado
# variable.funcion(posicion, elemento)
print('remover --- insert')
nombres.insert(1, "octavio")
print(nombres)

#remover elemento
print('remover --- remove')
nombres.remove("octavio")
print(nombres)

#remover el ultimo elemento de la lista
print('remover --- pop')
nombres.pop()
print(nombres)

#remueve segun el indice dado
print('remover --- del')
del nombres[0]
print(nombres)

#removueve todos los elementos
print('remover --- claer')
nombres.clear()
print(nombres)

#borrar la lista de la memoria
del nombres
print(nombres)