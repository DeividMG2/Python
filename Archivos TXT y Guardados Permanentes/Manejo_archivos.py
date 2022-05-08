'''
El objetivo de esto es la persistencia de datos o sea que se queden guardados y no se pierda la información.

Se pueden guardar en archivos externos (binarios o textos planos) o en base de datos.

Fases necesarias para guardar info en archivos externos:

	1. Creacion
	2. Apertura
	3. Manipulación
	4. Cierre

Para realizar todos estos tipos de operaciones con archivos externos vamos a utilizar el modulo io de la biblioteca estandar de python.

'''
from io import open
'''
archivo_texto = open("archivo.txt","w") #Aqui se crea y se abre un archivo.txt si no existe 

#El primer parámetro es el nombre del archivo y el segundo es una w si es para escribir una a 
#si es para agregar o sea append y una r si es para leer o sea read

frase = "Estupendo dia para estudiar Python \nel miercoles"

archivo_texto.write(frase) #Aqui le escribimos en el archivo

archivo_texto.close() #Aqui se cierra el archivo.
'''
'''
archivo_texto = open("archivo.txt","r")

texto = archivo_texto.read() #Aqui lee lo que hay en el archivo y lo almacena en la variable

archivo_texto.close()

print(texto)
'''
'''
archivo_texto = open("archivo.txt","r")
lineas_texto = archivo_texto.readlines()
archivo_texto.close()

print(lineas_texto[1])
'''
'''
archivo_texto = open("archivo.txt","a")

archivo_texto.write("\nSiempre es una buena opación para estudiar python.")

archivo_texto.close()
'''
'''
archivo_texto=open("archivo.txt","r+") #Si le agrego ese + puede realizar lectura y escritura.

print(archivo_texto.read())
archivo_texto.seek(0) #El seek nos sirve para cambiar la posicion del puntero puntero o cursor se situa en la posicion que le enviemos por parametro
print(archivo_texto.read(12)) #Aqui se puede enviar un numero y leera hasta la posicion del numero que enviemos y deja el puntero ahí.

archivo_texto.seek(len(archivo_texto.read())/2) #Aqui colocamos el cursor en la mitad del archivo.
print(archivo_texto.read())

'''

archivo_texto=open("archivo.txt","r+")

lista_texto = archivo_texto.readlines() #Hacemos una lista que incluye las lineas del archivo

lista_texto[1]= "Esta linea ha sido incluida desde el exterior\n" #Modificamos el archivo con la lista

archivo_texto.seek(0) 

archivo_texto.writelines(lista_texto)

archivo_texto.close()

