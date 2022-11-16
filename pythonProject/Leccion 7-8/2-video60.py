nombres = ['juan', 'karla', 'ricardo', 'maria']
print (nombres[0:2])
print(nombres[:3])
print(nombres[1:])

#[0:2] etc llegara hasta el elemento indicado
# especificar un valor cmbiando el ultimo

nombres[3] = 'ivone'
print(nombres)
for nombre in nombres:
    print(nombre)
else:
    print("no existe")

print(len(nombres))
#para agregar nuevos elementos

nombres.append("lorenzo")
print(nombres)