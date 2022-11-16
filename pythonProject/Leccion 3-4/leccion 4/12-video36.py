#ejercico rango entre 20's y 30's
edad = int(input("Introduce la edad del individuo: "))

if edad >= 20 and edad < 40:
    print ("estas dentro de los 20's y 30's")
    if edad >= 20 and edad < 30:
        print (f"tienes {edad} aun estas en los 20's")
    if edad >= 30 and edad < 40:
        print (f"tiene {edad} aun estas en los 30's")

else:
    print("no range")



