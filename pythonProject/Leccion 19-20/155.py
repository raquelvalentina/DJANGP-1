# manejo de archivos
try:
    file = open('prueba.txt', 'w', encoding= 'utf8')
    file.write('agregar información')
    '''manera de agregar texto al archivo'''

except Exception as e:
    print(e)
finally:
    file.close()
    print('CLOSE FILE')


