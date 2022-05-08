import math
print("Programa de calculos de raíz cuadrada")
numero = int(input("Introduce un numero: "))

intentos = 0

while numero < 0:
	print("No se puede hallar la raíz de un numero negátivo. Intentalo de nuevo: ")
	
	if(intentos == 2):
		print("Has consumido demasiados intentos. El programa ha finalizado.")
		break
	numero = int(input("Introduce un numero: "))

	if(numero<0):
		intentos+=1

if intentos<2:
	solucion = math.sqrt(numero)
	print("La raiz cuadrada de "+str(numero)+" es: "+str(solucion))