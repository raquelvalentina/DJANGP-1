dict = {
    'IDE':'integrated development environment',
    'dbms':'ddatabase management system',
    'oop':'object oriented programming'
}

for termino, valor in dict.items():
    print('key and value')
    print(termino,valor)
    print('')
for valor in dict.values():
    print('value')
    print(valor)
    print('')
for termino in dict.keys():
    print('key')
    print(termino)
    print('')
print('')
print('IDE' in dict)
print('')
print('add PK to dict')
dict['PK'] = 'primary key'
print(dict)
print ('remove: pop, clear ')
dict.pop('dbms')
dict.clear()