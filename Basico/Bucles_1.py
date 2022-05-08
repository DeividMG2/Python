#Para no hacer saltos de lineas y escribir todo en una linea en for sería:
#print("Hola",end = " ")
 
contadorArroba = 0
contadorPuntos = 0
miEmail = input("Introduce el correo: ")

for i in miEmail:
	if(i == "@"):
		contadorArroba+=1
	if(i == "."):
		contadorPuntos += 1

if (contadorArroba==1 and contadorPuntos>=1):
	print("El email es correcto.")
else:
	print("El email es incorrecto.")

