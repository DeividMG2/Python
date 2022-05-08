from tkinter import *

raiz = Tk()

barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)#Asi se crea el menú

archivoMenu = Menu(barraMenu, tearoff=0)#Asi se quita la barra que trae por defecto.
archivoMenu.add_command(label="Nuevo Archivo")
archivoMenu.add_command(label="Abrir Archivo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator() #Asi se agrega como una linea divisora entre los elementos.
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")#Asi se agregan las opciones que tiene el elemento de archivo en el menu

editarMenu = Menu(barraMenu, tearoff=0)
editarMenu.add_command(label="Copiar")
editarMenu.add_command(label="Cortar")
editarMenu.add_command(label="Pegar")

herramientasMenu = Menu(barraMenu, tearoff=0)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de")


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)#Asi hacemos que aparezca el menu.

barraMenu.add_cascade(label="Edición", menu=editarMenu)

barraMenu.add_cascade(label="Herramientas", menu=herramientasMenu)

barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


raiz.mainloop()