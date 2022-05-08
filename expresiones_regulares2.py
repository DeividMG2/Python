import re 
'''
lista_nombres = ['Ana Gómez',
				 'María Martín',
				 'Sandra Lopez',
				 'Sandra Mora',
				 'Santiago Martín',
				 'Ricardo Peña',
				 'niños',
				 'niñas',
				 'camión',
				 'camion']

for elemento in lista_nombres:	
	
	#if re.findall('^Sandra', elemento): #Ese metacaracter(^) lo que hará es agarrar todos los nombres y ver cual tiene Sandra como inicio del elemento.
	#if re.findall('Martín$', elemento):  #Ese metacaracter($) hace lo contrario del anterior, este muestra los elementos que terminen con la palabra que le demos. 
	#if re.findall('[ñd]',elemento):#Aqui busca si hay una ñ o d en toda la lista e imprime el elemento
	#if re.findall('niñ[oa]s',elemento):#Esta forma es como la anterior pero mas elaborada		
	if re.findall('cami[oó]n',elemento):	#Asi lo hacemos para evitar que el usuario se equivoque al no tildarla. 
			print(elemento) 

'''
#Siguiente Video sobre Expresiones Regulares
#Veremos el rango
lista_nombres = ['Ana',
				 'Ma1ría',
				 'Sandra',
				 'Pedro',
				 'Rosa',
				 'Ma2nuel']

for elemento in lista_nombres:
	#if re.findall('[o-t]',elemento):#Nos va a devolver todos los nombres que tienen dentro de su interior cualquier letra de la "o" a la "t"(o,p,q,r,s,t)
	#if re.findall('^[O-T]',elemento):#Asi se puede combinar un poco con lo otro aprendido, es decir imprime solo los que inicien con una letra de la O a la T pero en mayúsculas. Tambien se puede hacer con el $ al final para los que terminen con las que queramos.
		print(elemento)

lista=['Ma1',
		'Se1',
		'Ba1',
		'Ba2',
		'Ma2',
		'Ma3',
		'MaA',
		'MaB',
		'Ma4',
		'Ma.5',
		'Ma:6']

for i in lista:
	#if re.findall('Ma[^0-1]',i): #Asi nos devuelve los que no son del rango de la O a la T, es como una negación.	
	#if re.findall('Ma[0-3A-B]',i): #Asi hacemos como doble condicion o sea los que esten del rango 0 al 3 y del a al b
	if re.findall('Ma[.:]',i):
		print(i)