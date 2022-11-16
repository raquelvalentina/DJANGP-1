#libro: nombre(str),id(num),precio(float),enviogratuito(true,false)
print ("Informacion de un Libro")
print ("")
tt = input ("Cual es el titulo del libro:  ")
id = int(input("Cual es el id del libro:  "))
pr = float(input("Cual es el precio del libro:  "))
sf = input("Es el envio gratis:  ")

if sf == "True" or sf == "true" or sf == "si":
    sf = "True"
elif sf == "False" or sf == "false" or sf == "no":
    sf = "False"
else:
    print ("Intente denuevo solo es valido True o false")
    exit ()

print (f'''
    Titulo:  {tt} 
    ID :  {id} 
    Precio:  {pr}$  
    Envio gratis?:  {sf}''')