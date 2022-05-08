#Se va a ver decoradores con parametros

def funcion_decoradora(funcion_parametro):

	def funcion_interior(*args, **kwards): #Esto hace que reciba un numero indeterminado de parametros.

		#Acciones adicionales que decoran
		print("Vamos a realizar un cálculo.")

		funcion_parametro(*args, **kwards) #Aqui igual se agrega el args y se debe hacer para que funcione si agrego parametros.

		# Acciones adicionales que decoran

		print("Hemos terminado el cálculo")

	return funcion_interior


@funcion_decoradora  #Asi le digo al programa que cuando se produzca la llamada a la funcion suma esta debe ir decorada.
def suma(n1,n2,n3):

	print(n1+n2+n3)

@funcion_decoradora
def resta(n1,n2):

	print(n1-n2)

@funcion_decoradora
def potencia(base, exponente):

	print(pow(base, exponente))
	
#Ese @funcion_decoradora se debe escribir justo antes de donde se define el metodo o funcion.

suma(7,5,15)
resta(12,10)
potencia(base=5,exponente=3)