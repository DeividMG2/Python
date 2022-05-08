#Se va a usar el ejemplo del menu(archuvo menus.py)

from tkinter import *
from tkinter import messagebox

raiz = Tk()

def infoAdicional():
	messagebox.showinfo("Procesador ","Procesador de textos version 2019")#Asi es un messagebox de informacion

def avisoLicencia():
	messagebox.showwarning("Licencia","Producto bajo licencia GNU")#Asi es un messagebox de aviso

def salirAplicacion():
	valor = messagebox.askquestion("Salir","¿Estas seguro que deseas salir de la aplicación?")#Asi es un messagebox de PREGUNTAR se obtiene un yes o un no
	#valor = messagebox.askokcancel("Salir","¿Estas seguro que deseas salir de la aplicación?")#Este a diferencia del de arriba es con Aceptar y Cancelar y el valor que almacena es TRUE or False 
	if valor == "yes":
		raiz.destroy()

def cerrarDocumento():
	valor = messagebox.askretrycancel("Reintentar","No es posible cerrar. Documento Bloqueado")#Asi es un messagebox para reintentar o cancelar. Los valores que almacena son TRUE or False
	if valor == True:
		raiz.destroy()

barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)#Asi se crea el menú

archivoMenu = Menu(barraMenu, tearoff=0)#Asi se quita la barra que trae por defecto.
archivoMenu.add_command(label="Nuevo Archivo")
archivoMenu.add_command(label="Abrir Archivo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator() #Asi se agrega como una linea divisora entre los elementos.
archivoMenu.add_command(label="Cerrar", command = cerrarDocumento)
archivoMenu.add_command(label="Salir", command = salirAplicacion)#Asi se agregan las opciones que tiene el elemento de archivo en el menu

editarMenu = Menu(barraMenu, tearoff=0)
editarMenu.add_command(label="Copiar")
editarMenu.add_command(label="Cortar")
editarMenu.add_command(label="Pegar")

herramientasMenu = Menu(barraMenu, tearoff=0)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command = avisoLicencia)
ayudaMenu.add_command(label="Acerca de", command=infoAdicional)


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)#Asi hacemos que aparezca el menu.

barraMenu.add_cascade(label="Edición", menu=editarMenu)

barraMenu.add_cascade(label="Herramientas", menu=herramientasMenu)

barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


raiz.mainloop()
