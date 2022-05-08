#RadioButton
#Son los de seleccion unica, ejemplo el de seleccionar genero.

from tkinter import *


raiz = Tk()

varOpcion = IntVar()

def imprimir():

	#print(varOpcion.get())
	if varOpcion.get()==1: #Aqui vemos que valor selecciono el usuario y realizamos cualquier accion.
		etiqueta.config(text="Sexo Masculino seleccionado")
	
	elif varOpcion.get() == 2:
		etiqueta.config(text="Sexo Femenino seleccionado")

	else:
		etiqueta.config(text="Has seleccionado otros")

Label(raiz, text="Genero:").pack()

Radiobutton(raiz, text="Masculiuno", variable = varOpcion, value = 1, command = imprimir).pack()

Radiobutton(raiz, text="Femenino", variable = varOpcion, value = 2, command = imprimir).pack() #Asi se crean los Radiobutton con las opciones y que funcione correctamente

Radiobutton(raiz, text="Otros", variable = varOpcion, value = 3, command = imprimir).pack()


etiqueta = Label(raiz)
etiqueta.pack()


raiz.mainloop()