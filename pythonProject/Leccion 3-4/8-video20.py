#Ejercicio clasificacion de tu dia del 1 al 10

cc = int(input("Como ha sido tu dia? clasificalo del 1 al 10: "))

if cc <= 3:
    print ("que mal que tu dia haya sido un ", cc)
elif cc == 4:
    print (("por lo menos tu dia fue un "), cc ,(" hay peores"))
else:
    print ("Enhorabuena que tu dia haya sido un ", cc)