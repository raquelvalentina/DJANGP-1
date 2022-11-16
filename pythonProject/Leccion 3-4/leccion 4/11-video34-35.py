#Ejercicio con operador or para dias libre y vacaiones para asistir a un evento

vaca = True
diad = True

if vaca and diad:
    print ("Esta totalmente libre")

elif not (vaca or diad):
    print ("no puede asistir")

else:
    print ("libre")