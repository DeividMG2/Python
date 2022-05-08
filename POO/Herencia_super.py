class Persona():

	def __init__(self, nombre, edad, lugar_residencia):

		self.nombre = nombre
		self.edad = edad
		self.lugar_residencia = lugar_residencia

	def descripcion(self):

		print("Nombre: ", self.nombre, "Edad: ",self.edad, "Residencia: ",self.lugar_residencia)


class Empleado(Persona):

	def __init__(self, salario, antiguedad, nombreEmpleado, edadEmpleado, residencia_Emplado):

		super().__init__(nombreEmpleado,edadEmpleado,residencia_Emplado)

		self.salario = salario
		self.antiguedad = antiguedad

	def descripcion(self):

		super().descripcion()
		print("Salario: ",self.salario, "Antiguedad: ",self.antiguedad)

Antonio = Empleado(1500, 15, "Antonio",55,"España")
Antonio.descripcion()
print(isinstance(Antonio, Persona))#Esto sirve para ver si Antonio e suna instancia de la clase persona, o sea se envian 2 parametros, la instancia y la clase.






