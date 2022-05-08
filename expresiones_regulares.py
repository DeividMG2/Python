'''
Son una secuencia de caracteres que forman un patron que sirve para realizar busquedas la mayor parte de busquedas de texto,
Ej:
	Buscar un texto que se ajusta a un formato determinado(correo electronico, o sea ver si este existe)
	Buscar si existe o no una cadena de caracteres dentro de un texto.
	Contar el numero de coincidencias dentro de un texto. Etc..


'''
import re

cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

#print(re.search("aprender",cadena)) #Si me devuelve un objeto, si esta en el texto si nos devuelve "none" pues no.

textoBuscar = "Python"
'''
if re.search(textoBuscar,cadena) is not None:

	print("He encontrado el texto")

else:

	print("No he encontrado el texto")
'''
textoEncontrado = re.search(textoBuscar,cadena)

print(textoEncontrado.start()) #Aqui nos da el valor del primer caracter donde comienza el texto.

print(textoEncontrado.end()) #Y aqui el caracter donde finaliza 

print(textoEncontrado.span()) #Nos devuelve en una tupla el caracter donde inicia y donde termina.

print(re.findall(textoBuscar, cadena)) #Asi nos devuelve el valor que busquemos en una tupla o lista las veces que este en la cadena, con un len antes de todo eso vemos cuantas veces salió.

