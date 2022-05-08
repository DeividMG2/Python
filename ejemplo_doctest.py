def areaTriangulo(base,altura):
	"""
	Calcula el area de un triangulo dado
	
	>>> areaTriangulo(3,6)
	'El area del triangulo es: 9.0'

	>>> areaTriangulo(4,5)
	'El area del triangulo es: 10.0'

	>>> areaTriangulo(9,3)
	'El area del triangulo es: 13.5'

	"""

	return "El area del triangulo es: "+str((base*altura)/2)
 
import doctest
doctest.testmod()
'''
El doctest lo que hace basicamente es entre esas comillas primero por ejemplo
se pone un comentario luego se usan esos 3 signos(>>>) y seguido de ellos+
se escribe la funcion en este caso con paramentros y debajo de esa linea debemos
poner el resultado que nos debe dar, si el resultado que agregamos es el correcto
no nos dará ningun mensaje ni nada pero si no es nos sará un error.
'''
