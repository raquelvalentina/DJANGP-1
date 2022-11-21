file = open('prueba.txt', 'r', encoding='utf8')
# print(file.read())
print(file.read(5))

'''readline idenifica la ruta del archivo'''
print(file.readlines()[2])
'''forma de acceder a las lineas del archivo'''
# modos para un archivo

# for linea in file:
#     print(linea)