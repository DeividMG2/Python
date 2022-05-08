#Las excepciones son errores en tiempo de ejecucion, sin error de sintaxis, todo está bien pero es algo inesperado.
#A continuación un ejemplo de excepcion de error de ZeroDivisionError al dividir por 0
'''
def dividir(num1,num2):
	try:
		return(num1/num2)
	except ZeroDivisionError:
		print("No se puede dividir entre 0")
		return "Operación Erronea"

print(dividir(8,0))
print("Fin del programa")
'''
#Ahora un ejemplo de excepcion de error ValueError que al escribir letras donde debe digitar un entero
'''
while True: #Asi se hace un bucle infinito
	try:
		n1 = int(input("Introduce numero 1: "))
		n2 = int(input("Introduce numero 2: "))
		break
	except ValueError:
		print("Los valores introducidos no son correctos. Intentalo de nuevo")

print(n1/n2)
'''
#Ahora un ejemplo con una funcion que divida y en ella se realize todo el procedimiento
'''
def divide():
	try:
		op1=(float(input("Introduce el primer numero: ")))
		op2=(float(input("Introduce el segundo numero: ")))
		print("La division es: "+str(op1/op2))
		
	#except ValueError:
		#print("El valor introducido es incorrecto. ")

	#except ZeroDivisionError:
		#print("No se puede dividir entro 0")
	except:
		print("Ha ocurrido un error") #Es mejor de la manera anterior porque si se hace asi el usuario no sabrá donde este el error.

	finally:
		print("Calculo finalizado") #Esto se ejecutara si o si ocurriendo un error o no gracias al finally

divide()
'''
#Ahora haremos uso de la instrucción Raise y para ello haremos un programa que sea capaz de evaluar nuestra edad
'''
def evaluaEdad(edad):

	if edad < 0:
		raise TypeError("No se permiten edades negativas")#Asi es como creamos nuestras propias excepciones.

	if edad < 20:
		return "Eres muy joven"
	elif edad < 40:
		return "Eres joven"
	elif edad < 65:
		return "Eres maduro"
	elif edad < 100:
		return "Cuídate"

print(evaluaEdad( 45))
'''
#Ahora crearemos una funcion que sea capaz de crear calculos de raices cuadradas:
import math 

def calculaRaiz(num1):
	if(num1<0):
		raise ValueError("Numero no puede ser negativo.")
	else:
		return math.sqrt(num1)

op1 = (int(input("Introduce un número: ")))
try: 
	print(calculaRaiz(op1))
except ValueError as ErrorNumeroNegativo:
	
	print(ErrorNumeroNegativo)

print("Programa finalizado")