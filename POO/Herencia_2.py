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

	def __init__(self):
autonomia = 100

		self.
	def cargarEnergia(self):

		self.cargando = True


miMoto = Moto("Honda", "CBR") #Se crea la instancia miMoto de la clase Moto que tiene toda la herencia de la clase Vehiiculos por lo cual tiene los atributos y metodos de la clase Vehiculos

miMoto.caballito()

miMoto.ImprimirEstado() #Aqui se llama al ver estado de la clase metodo porque es el que se sobreescribe

miFurgoneta = Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.ImprimirEstado()

print(miFurgoneta.carga(True))

class BicicletaElectrica(Velectricos, Vehiculos): #Aqui se hace la herencia de 2 clases, se llama al constructor de la primera clase que heredo en los parametros.

	pass

miBici = BicicletaElectrica()

