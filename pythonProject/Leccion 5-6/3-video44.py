condi = int(input("valor entre 1 y 3: "))

if condi == 1:
    conditxt = 'numero uno'

elif condi == 2:
    conditxt = 'numero dos'

elif condi == 3:
    conditxt = 'numero tres'

else:
    conditxt = 'fuera del rango'

print (f"numero proporcionado: {condi}: {conditxt}")