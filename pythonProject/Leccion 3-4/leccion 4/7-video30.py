#jercicio proporcionar un nuemero identifica si es par o impar y mostrar en pantalla

intt= input("proporciona un valor numerico: ")

tt = intt.isnumeric()
if tt == False:
    print ("te quivocaste intenta denuevo")

elif tt == True:
    a = int (intt)

    if a % 2 == 0:
        print (f"el valor {intt} es par. ")

    else:
        print (f"el valor {intt} es impar")

