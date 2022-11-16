#tuplas en python
frutas = ['naranja', 'platano', 'guayaba']

print(frutas)
print(len(frutas))
for fruta in frutas:
    print(fruta, end = ' ')

frutaslista = list(frutas)

frutaslista[0] = 'pera'
frutas= tuple(frutaslista)

print('/n', frutas, end=' ')
del frutas
print(frutas)