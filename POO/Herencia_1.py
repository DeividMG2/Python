'''
La clase que esta en lo principal o en la cúspide por decirlo asi se le deniminca la clase padre o superclase
La clase que hereda de esa se llamara subclase y si esta tambien va a heredar a otra tambien se llamara superclase

La herencia sirve para reutilizar codigo en caso de crear objetos similares

Se construye una clase con todas las propiedades y metodos en comun de los objetivos y despues las caracteristicas de cada objeto los construiremos en su propia clase.

'''

class Vehiculos():

	def __init__(self,marca,modelo):

		self.marca = marca	
		self.modelo = modelo
		self.enMarcha = False
		self.acelera = False
		self.frena = False

	def arrancar(self):

		self.enMarcha = True

	def acelerar(self):

		self.acelerar = True

	def frena(self):

		self.frena = True

	def ImprimirEstado(self):

		print("Marca: ",self.marca, "\nModelo: ",self.modelo, "\nEn Marcha: ",
			self.enMarcha, "\nAcelerando :",self.acelera, "\nFrenando: ",self.frena)

class Moto(Vehiculos): #Asi se hereda de la clase vehiculos, simplemente se agrega en el parametro el nombre de la clase padre

	pass

miMoto = Moto("Honda", "CBR") #Se crea la instancia miMoto de la clase Moto que tiene toda la herencia de la clase Vehiiculos por lo cual tiene los atributos y metodos de la clase Vehiculos
miMoto.ImprimirEstado()

