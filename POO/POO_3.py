class Coche(): #Asi se crea una clase
		
	def __init__(self): #Asi se crea el método constructor 
		self.largoChasis = 250
		self.anchoChasis = 120
		self.__ruedas = 4 #Aqui se maneja el encapsulamiento en las ruedas, se tiene que agregar esos 2 guiones bajos ahí Y esto sirve para todas las variables que quiera y hasta metodos.

		self.enMarcha = False #Aqui se agregan las propiedades comunes o iniciales.

	def arrancar(self, arranque): #La diferencia que hay de funcion y método es que un metodo pertenece a la clase mientras que una funcion no pertenece a ninguna clase. Asi se le hace el comportamiento al objeto, o sea el metodo (def es para funcion y defs es para metodo, lo que he creado e sun método). Y la palabra self hace referencia al objeto perteneciente a la clase.
		
		#self.enMarcha = True #Asi es como le cambio la propiedad enMarcha al objeto que se almacena en self, es como si le estuviera diciendo miCoche.enMarcha = True

		self.enMarcha = arranque

		if(self.enMarcha):
			chequeo = self.__chequeoInterno()

		if(self.enMarcha and chequeo):
			return("El coche está en marcha")
		elif(self.enMarcha and chequeo == False):
			return("Algo ha ido mal en el chequeo, no se puede arrancar.")
		else: 
			return("El coche está parado")


	def estado(self):
		print("El coche tiene ",self.__ruedas, " ruedas. Un ancho de ",self.anchoChasis," y un largo de ",self.largoChasis)


	def __chequeoInterno(self):
		print("Realizando Chequeo Interno")

		self.gasolina = "ok"
		self.aceite = "ok" 
		self.puerta = "cerradas"

		if(self.gasolina == "ok" and self.aceite == "ok" and self.puerta == "cerradas"):
			return True
		else:
			return False


miCoche = Coche() #Aqui se hace una instancia a la clase. 

print(miCoche.arrancar(True)) #Asi accedemos a los metodos o comportamientos de los objetos.

miCoche.estado()

print("---------------A continuacion creamos el segundo objeto---------------")

miCoche2 = Coche()

print(miCoche2.arrancar(False))

miCoche2.__ruedas = 2 #No sirve porque la propiedad de ruedas

miCoche2.estado()

print(miCoche2.__chequeoInterno())#Esto va a dar error porque el metodo solo se puede usar en la clase, es decir está encapsulado.

