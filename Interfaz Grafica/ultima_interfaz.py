from tkinter import *
from tkinter import filedialog

raiz = Tk()

def abreFichero():

	#fichero = filedialog.askopenfilename(title="Abrir") #Esto sirve para navegar en las carpetas o sistema de directorios Y NOS ALMACENA LA RUTA.
	fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Ficheros de Excel", "*.xlsx"), ("Ficheros de Texto", "*.txt"),("Todos los ficheros","*.*")))#Este es lo mismo que arriba pero el de arriba abre las carpetas pero de documento por defecto y con este, con el initialdir podemos modificar eso Y con el filetypes filtra o muestra solo los archivos en este caso los de texto, los de excel o la opcion de todos los ficheros. 
	print("Direccion del fichero: "+fichero)

Button(raiz, text="Abrir Fichero", command = abreFichero).pack()


raiz.mainloop()