#solucion
edad = int(input("proporciona"))
msm = None

if 0 <= edad < 10:
    msm = 'la infancia es increible'

elif 10 <= edad < 20:
    msm = 'Muchos cambion, mucho estudio'
elif 20 <= edad < 30:
    msm = 'amor y confianza '
else:
    print("no reconocido")

print(f"La edad de {edad}, {msm} ")