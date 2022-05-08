import pickle

class Vehiculo():

	def __init__(self, marca, modelo):

		self.marca = marca
		self.modelo = modelo
		self.enmarcha = False
		self.acelera = False
		self.frena = False

	def arrancar(self):

		self.enmarcha = True

	def acelerar(self):

		self.acelera = True

	def frenar(self):

		self.frena = True

	def estado(self):

		print("Marca: ", self.marca,"\nModelo", self.modelo,"\nAqui va el resto de información...")

coche1 = Vehiculo("Mazda","MX5")	

coche2 = Vehiculo("Seat","Leon")

coche3 = Vehiculo("Renault","Megane")

coches = [coche1,coche2,coche3]

fichero = open("losCoches", "wb") 

pickle.dump(coches, fichero) #Aqui se guarda en fichero la informacion serializada

fichero.close()

del(fichero) #Se elimina porque ya esta en el disco duro, y para eliminarlo de la memoria del programa

ficheroApertura = open("losCoches","rb")

misCoches = pickle.load(ficheroApertura) #Aqui mete la info de apertura a la variable misCoches

ficheroApertura.close()

for i in misCoches:

	print(i.estado())