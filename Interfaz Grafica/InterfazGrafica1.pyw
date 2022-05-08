#Para trabajar con las GUI vamos a usar la librería Tkinter
'''
Estructura de ventana con Tkinter: 
-Raiz o la ventana
-Frame
-Widgets(botones, menus, casillas, cuadros de texto...)
En python un frame se considera un widget

'''

from tkinter import *

raiz=Tk() #Es como el inicio para crear la ventana

raiz.title("Ventana de Pruebas") #Agregacion del titulo de la ventana

#raiz.resizable(0,0) #El primer parametro es del ancho(width) y el segundo al alto(height) y son booleanos, o sea si coloco un 0 no puedo redimencionar o ajustar la ventana el largo y el ancho, para poder redimencionarlo simplemente coloco unos(1,1) o lo dejo por defecto.Tambien se puede usar TRUE OR FALSE en ves de 1 y 0

raiz.iconbitmap("icono1.ico") #Asi se cambia el icono de la barra del titulo, el parametro es para escribir la ruta.

#raiz.geometry("650x400") #Asi se ajusta el tamaño de la ventana.

raiz.config(bg="green") #Asi le cambio el color del fondo, ese bg significa el background

miFrame = Frame()#Asi se crea el frame

#miFrame.pack(side = "left", anchor = "n") #Así se coloca el frame en el interior de la raiz (empaquetado) esos parametro me permiten "fijar" el frame en la parte izquierda y en el norte o arriba a la izquierda.

#miFrame.pack(fill ="x") #El frame se redimenciona horizontalmente arriba

#miFrame.pack(fill = "y",expand=True) #Asi se redimenciona verticalmente en el centro, se debe usar el expand

#miFrame.pack(fill = "both", expand = True) #Aqui hacemos que se redimencione el frame siempre con la ventana al mismo tamaño.

miFrame.pack()

miFrame.config(bd = 35) #Es como el tamaño del borde

miFrame.config(relief = "sunken") #Aqui podemos utilizar diferentes tipos de bordes.

miFrame.config(cursor = "hand2") #Asi transformo la forma del cursor cuando esté sobre el frame.

miFrame.config(bg = "red") 

miFrame.config(width = "650",height = "350") #Asi se cambia el tamaño del frame, debo quitar el geometry para poder hacerlo y ademas el tamaño de la raiz se adaptará al del frame.

raiz.mainloop() #Esto permite que la ventana este siempre activa es como un bucle infinito. DEBE ESTAR SIEMPRE DE ULTIMO!


   