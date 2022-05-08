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

class Furgoneta(Vehiculos):

	def carga(self, cargar):

		self.cargado = cargar
		if(self.cargado):
			return "La furgoneta esta cargada"
		else:
			return "La furgoneta no esta cargada"




class Moto(Vehiculos): #Asi se hereda de la clase vehiculos, simplemente se agrega en el parametro el nombre de la clase padre

	hcaballito = ""
	def caballito(self):
		self.hcaballito = "Voy haciendo el caballito"	

	def ImprimirEstado(self): #Se sobreescribe el metodo de imprimir el estado

		print("Marca: ",self.marca, "\nModelo: ",self.modelo, "\nEn Marcha: ",
			self.enMarcha, "\nAcelerando :",self.acelera, "\nFrenando: ",self.frena, "\n",self.hcaballito)



class Velectricos():

	def __init__(self, marca, modelo):

		super().__init__(marca, modelo)
		autonomia = 100

	def cargarEnergia(self):

		self.cargando = True

