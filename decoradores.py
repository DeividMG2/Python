'''
Decoradores: Son funciones que añaden funcionalidades a otras funciones
que ya existan en tu programa.

'''

def funcion_decoradora(funcion_parametro):

	def funcion_interior():

		#Acciones adicionales que decoran
		print("Vamos a realizar un cálculo.")

		funcion_parametro()

		# Acciones adicionales que decoran

		print("Hemos terminado el cálculo")

	return funcion_interior


@funcion_decoradora  #Asi le digo al programa que cuando se produzca la llamada a la funcion suma esta debe ir decorada.
def suma():

	print(15+20)


@funcion_decoradora
def resta():

	print(20-5)
	
#Ese @funcion_decoradora se debe escribir justo antes de donde se define el metodo o funcion.

suma()
resta()