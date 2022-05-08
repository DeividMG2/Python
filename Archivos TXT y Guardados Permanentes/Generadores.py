#Generadores: Son extructuras que extraen valores de una funcion, que se van a almacenar en objetos iterables, o sea esos valores se podrá recorrer.
#La diferencia de las funciones que returnan por ejemplo una lista con numeros y un generador que devuelva con el codigo yield en ves de return es que nos devuelve de uno en uno.
#Ejemplo:
def generarNumPares(Limite):
	numero = 1


	while numero<Limite:
		yield numero*2
		numero += 1

devuelvePares = generarNumPares(10)

print(next(devuelvePares))#Aqui conseguimos que nos devuelva el primer valor que tiene almacenado

print(next(devuelvePares))#Aqui el segundo y asi sucesivamente.

#Ahora veremos la instrucción yield from
#Utilidad: Simplificar el codigo de los generadores en el caso de utilizar bucles anidados."
def devuelve_ciudades (*ciudades):#Cuando agregamos ese asterisco antes del parametro siginifica que no sabemos cuantos elementos van a ingresarse y se van a guardar en forma de tupla.
	for elemento in ciudades:
		#for subElemento in elemento:
			yield from elemento #Aqui es hacer como un yield pero del primer elemento

ciudades_devueltas = devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")

for x in range (2):
	print(next(ciudades_devueltas))

