#Un numero mayor que otro 2 variables
a1 = int(input("Primer valor :  "))
a2 = int(input("Segundo valor :  "))

if a1 > a2 or a1 < a2:
    if a1 > a2:
        print(f"El primer valor {a1} es mayor que el segundo valor {a2}")
    else:
        print (f"El segundo valor {a2} es mayor que el primer valor {a2}")
else:
    print (f"Son iguales los valores {a1} y {a2}")


