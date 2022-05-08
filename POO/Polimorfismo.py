'''
El polimorfismo, un objeto puede cambiar de forma dependiendo del contexto en que se utilice y por cambiar de forma tambien cambia de comportamiento.
'''
class Coche():

	def desplazamiento(self):

		print("Me desplazo utilizando 4 ruedas")

class Moto():

	def desplazamiento(self):

		print("Me desplazo utilizando 2 ruedas")

class Camion():

	def desplazamiento(self):

		print("Me desplazo utilizando 6 ruedas")

def desplazamientoVehiculo(vehiculo): #Aqui es donde sucede el polimorfismo con ese parametro hace que se transforme en un objeto de tipo camion en este ejemplo

	vehiculo.desplazamiento()

miVehiculo = Camion()

desplazamientoVehiculo(miVehiculo)


