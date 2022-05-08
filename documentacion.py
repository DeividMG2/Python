'''Documentacion: Incluir comentarios en clases, metodos, modulos, etc...
Para ayudar en el trabajo en equipo. Especialmente util en aplicaciones complejas.'''
from Modulos import funciones_matematicas
class Areas:
	"""Esta clase calcula areas"""

	def areaCuadrado(lado):

		"""Calcula el area de un cuadrado
		elevando al cuadrado el lado pasado por parametro"""

		return("El area del cuadrado es: "+str(lado*lado))

	def areaTriangulo(base, altura):
		return "El area del triangulo es: "+str((base*altura)/2)

#print(areaCuadrado(3))

#print(areaCuadrado.__doc__) #Podemos hacer esto para imprimir la documentacion o el comentario de en este caso el metodo de areaCuadrado.
#help(areaCuadrado) #Esta es otra manera que nos imprime esta documentacion pero un poco mas elaborada.

help(Areas.areaCuadrado) #Asi se hace lo anterior pero con metodos dentro de una clase.

help(Areas) #Asi muestro en este caso todas las documentaciones de la clase Areas

help(funciones_matematicas) #Asi muestro la documentacion de un modulo