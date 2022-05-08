'''
Si queremos distribuir un objeto que hemos contruido en python por internet es bueno que esté codificado en codigo binario porque es mas fácil distribuirlo y tambien cuando queremos guardar un objeto, coleccion o diccionario en una base de datos.

Debemos utilizar la biblioteca Pickle

Metodos que vamos a utilizar: 

dump() Volcado de datos al fichero binario externo
load() Carga de los datos del fichero binario externo



'''
import pickle
'''
lista_nombres = ["Pedro", "Ana", "Maria", "Isabel"]

fichero_binario = open("lista_nombres","wb")

pickle.dump(lista_nombres, fichero_binario) #Aqui agregamos la lista al fichero y se guarda. Se hace el volcado.

fichero_binario.close()

del(fichero_binario) #Se borra de la memoria, no es necesario pero se puede hacer.
'''

fichero = open("lista_nombres","rb")

lista = pickle.load(fichero) #Aqui accedemos a la lista que hay en el fichero binario

print(lista)