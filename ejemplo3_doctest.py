import math as mate

def raizCuadrada(listaNumeros):

	"""
	La funcion devuelve una lista con la 
	raiz cuadrada de los elementosa numericos
	pasados por parametros en otra lista
	
	>>> lista=[]
	>>> for i in [4 , 9, 16]:
	...		lista.append(i)
	>>> raizCuadrada(lista)
	[2.0, 3.0, 4.0]

	>>> lista=[]
	>>> for i in [4,9,16,50,-6,85]:
	... 	lista.append(i)
	>>> raizCuadrada(lista)
	Traceback (most recent call last):
 		...
	ValueError: math domain error


	"""

	return [mate.sqrt(n) for n in listaNumeros]

#print(raizCuadrada([9, -16, 25, 64]))

import doctest
doctest.testmod()


#--------Apuntes de los tests en este programa----------
	
	#Los ... hará que el programa sepa que es una expresion anidada que pertenece a la linea anterior.
	#En esa prueba de la excepcion(la segunda prueba) cuando hacemos eso ahi lo que hacemos es que copiamos toda la excepcion
	#que deberia marcar pero solo dejamos la primer y ultima linea y entre esas dos colocamos los 3 puntos (...)

#---------ULTIMO VIDEO "GENERAR EJECUTABLES"---
'''
Para hacerlo vamos a una carpeta donde este la aplicacion.py y quizas un icono
debemos ir a la ruta en CMD

AGREGAMOS LO SIGUIENTE:
	
	pyinstaller NOMBRE_DEL_ARCHIVO_CON_EXTENSION_.PY

EJEMPLO:

	C:\Projects\Ejecutable BD>pyinstaller --windowed --onefile --icon=./icono.ico practica_base_de_datos.py

En ese ejemplo el windowed hace que aparezca solo la aplicacion, sin el cmd, el one file hace que todos los archivos que necesite la aplicacion sea solo uno y el icon= es obviamente para agregarle el icono a la aplicación

'''