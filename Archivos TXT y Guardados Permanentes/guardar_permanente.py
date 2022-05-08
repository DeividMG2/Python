import pickle

class Persona:

	def __init__ (self,nombre,genero,edad):

		self.nombre = nombre
		self.genero = genero
		self.edad = edad

		print("Se ha creado una persona nueva con el nombre "+str(self.nombre))

	def __str__(self): #Convierte la info de un objeto en cadena de texto

		return "{} {} {}".format(self.nombre,self.genero,self.edad)


class ListaPersonas:

	personas = []

	def __init__(self):

		listaDePersonas = open("ficheroExterno","ab+")
		listaDePersonas.seek(0)

		try:
			self.personas=pickle.load(listaDePersonas)
			print("Se cargaron {} personas del fichero".format(len(self.personas)))

		except:

			print("El fichero está vacío")

		finally:
			listaDePersonas.close()
			del(listaDePersonas)

	def agregarPersona(self, persona): #Aqui se agregan las personas a la lista y llama al metodo que los guardara en el fichero externo

		self.personas.append(persona)
		self.guardarPersonasEnFicheroExterno()

	def guardarPersonasEnFicheroExterno(self): #Aqui se guardan las personas en el fichero externo

		listaDePersonas = open("ficheroExterno","wb")
		pickle.dump(self.personas, listaDePersonas)
		listaDePersonas.close()
		del(listaDePersonas)

	def mostrarPersonas(self):

		for i in self.personas:
			print(i)

	def mostrarInfoFicheroExterno(self):

		print("La informacion del fichero externo es la siguiente: ")
		for p in self.personas:
			print(p)


miLista = ListaPersonas()
persona = Persona("Ana","Femenino",31)
miLista.agregarPersona(persona)
miLista.mostrarInfoFicheroExterno()
