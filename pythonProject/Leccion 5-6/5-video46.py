#mes del anio estacion que corresponde

mes = int(input("month of the year "))
estacion = (None)
name = (None)
if mes == 2 or mes == 1 or mes == 12:
    estacion = 'invierno'
    if mes == 2:
        name = "febrero"
    elif mes == 1:
        name = "enero"
    else:
        name = "diciembre"

elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
    if mes == 3:
        name = "marzo"
    elif mes == 4:
        name = "abril"
    else:
        name = "mayo"

elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
    if mes == 6:
        name = "junio"
    elif mes == 7:
        name = "julio"
    else:
        name = "agosto"

elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'otonio'
    if mes == 9:
        name = "septiembre"
    elif mes == 10:
        name = "octubre"
    else:
        name = "noviembre"

else:
    print ("acaso no te sabes los meses del anioo pndjo")

print ('''resultado''')
print (f"En {name}-{mes}, ocurre la {estacion}")
