# objetivo sistemsa de calificaciones
# 0-10
#
# 9-10: A
# 8-9: B
# 7-8: C
# 6-7:D
# 0-6: F
# else; error

print ("Sistema de califaicaciones")
pnt = int (input("Cual es el puntaje en el examen: "))
abc = (None)

if 9 <= pnt <= 10:
    abc = ('A')
    print(f"enhorabuena felicidades por tu {abc}")
elif 9 > pnt >= 8:
    abc = ('B')
    print(f"No esta para nada mal tu {abc}")
elif 8 > pnt >= 7:
    abc = ('C')
    print(f"Nesecitas mas estudio por tu {abc}")
elif 7 > pnt >= 6:
    abc = ('D')
    print(f"Un {abc} Creo que alguien se quedo solo con lo que vio en clase")
elif 6 > pnt >= 0:
    abc = ('F')
    print(f"Nesecitas mas estudio por tu {abc}")

else:
    print ('CALIFICACION NO COENCIDENTE ***')

