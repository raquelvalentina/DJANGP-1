#Sintaxis simplificada

edad = int(input("Introduce la edad del individuo: "))

if  20 <= edad < 40:
    print ("estas dentro de los 20's y 30's")
    if 20 <= edad < 30:
        print (f"tienes {edad} aun estas en los 20's")
    if  30 <= edad < 40:
        print (f"tiene {edad} aun estas en los 30's")

else:
    print("no range")