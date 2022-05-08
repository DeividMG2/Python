'''
Es similar a la funcion filter pero esta realiza cosas mas complejos, lo que hace es
aplicar una funcion a cada elemento de una lista iterable.
'''

class Empleado:

	def __init__(self, nombre, cargo, salario):

		self.nombre = nombre
		self.cargo = cargo
		self.salario = salario

	def __str__(self):

		return "{} que trabaja como {} tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)

listaEmpleados = [
	
Empleado("Juan","Director",28000),
Empleado("Pedro","Administrador",15000),
Empleado("Miguel","Presidente",40000),
Empleado("Sara","Secretaria",20000)

]

def calculo_comision(empleado):

	if empleado.salario >=25000:
		empleado.salario=empleado.salario*1.03

	return empleado

listaEmpleadosComision=map(calculo_comision, listaEmpleados)
#Asi es como se usa el map, el primer parametro es una funcion, y el segundo de la lista de los elementos que quiero.
for empleado in listaEmpleadosComision:

	print(empleado)