#Video 36, Paquetes Distribuibles.

'''
Lo que se va a hacer es instalar este paquete dentro de python para que lo pueda leer y acceder a el desde cualquier sitio

Pasos:

1 - Ir a View, luego a Side Bar, y Show Files
2 - Llevar la carpeta que necesito a la parte debajo donde dice Open Files
3 - Crear un archivo que se llame setup.py, lo creamos en la raiz de la carpeta python, este archivo incluye
una descripción del paquete que vamos a distribuir(nombre del paquete, version, descripcion, autor, etc..)
4 - En ese archivo setupo.py debo agregar lo siguiente: 
	 
from setupotools import setup

setup(

	name = "paqueteCalculos", 
	version = "1.0",
	description = "Paquete de Redondeo y Potencia",
	author = "Deivid",
	url = "PaginaWebDeReferencia",
	packages = ["calculos","calculos.redondeo_potencia"]


	)
5 - Ir a la carpeta donde se encuentre desde cmd ej:
C: \Projects\Python\Deivid\Curso Pildoras Informaticas

6 . Escribimos ahi mismo en el cmd lo siguiente que hará que se cree el paquete distibuirlo
C: \Projects\Python\Deivid\Curso Pildoras Informaticas python setup.py sdist

7 - Revisar en nuestra carpeta que se hayan creado 2 carpetas, paquetecalculos.egg-info y la carpeta dist
 
8 - Dentro de la carpeta dist se encuentra el paquete distribuible creado que se puede enviar o distribuir.

PARA INSTALAR UN PAQUETE DISTRIBUIDO SE HACE LO SIGUIENTE:

1 - Con la consola vamos al directorio de la carpeta.

2 - Escribir en el cmd cd dist

3 - Escribir en el cmd pip3 install "Nombre del paquete"(con solo escribir las 2 primeras letras del paquete y darle tab se rellena el nombre)

4 - Pulsamos enter y se instala.



'''
from calculos.redondeo_potencia.redondeo_potencia import *

potencia(9,4)

