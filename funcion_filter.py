'''
Verifica que los elementos de una secuencia cumplan con una condicion
y esta devuelve los iteradores de los elementos que cumplen dicha condición. 
'''
'''
#Conseguir los numeros pares

def numero_par(num):

	if num%2==0:

		return True

numeros=[17,27,54,34,55,18,20,11]

print(list(filter(lambda numero_par:numero_par%2==0, numeros)))#Así se usa el filter y asi tambien me imprime los numeros gracias al filter y los almacena en un list e imprime.Y con el lambda se resume
'''

#---Otro ejemplo:-----------
class Empleado:

	def __init__(self, nombre, cargo, salario):

		self.nombre = nombre
		self.cargo = cargo
		self.salario = salario

	def __str__(self):

		return "{} que trabaja como {} tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)

listaEmpleados = [
	
Empleado("Juan","Director",75000),
Empleado("Pedro","Administrador",50000),
Empleado("Miguel","Presidente",90000),
Empleado("Sara","Secretaria",45000)

]

salarios_altos = filter(lambda empleado: empleado.salario>50000, listaEmpleados)

for i in salarios_altos:
	print(i)