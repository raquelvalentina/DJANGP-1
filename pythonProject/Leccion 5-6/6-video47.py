# edad
#
# 0-10 infancia
# 10- 20 muchos cambios y estudios
# 20-30 amor y tabajo
# else no reconocida


ed = int(input("Cual es tu edad: "))

if 0 < ed < 10:
    print ("Disfuta la infancia")
elif 10 <= ed < 20:
    print ("mucho cambio y estudio")
elif 20<= ed < 30:
    print ("nueva forma de vida amor y trabajo")
else:
    print ('edad no reconocida')