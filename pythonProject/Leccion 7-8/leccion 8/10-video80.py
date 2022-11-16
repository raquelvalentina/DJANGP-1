'''iterar los elementos de un diccionario'''

def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}')

listarTerminos(IDE='Integrated Developement Environment', PK='Primary Key')
listarTerminos(DBMS='Database Management System')