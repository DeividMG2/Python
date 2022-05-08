#CAMPOS DE TEXTO
from tkinter import *

raiz = Tk()


miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()



nombreLabel = Label(miFrame, text="Nombre:")#El grid nos sirve para ordenar en casillas como una tabla, lleva 2 parámetros, uno hace refencia a la fila y el otro a la columna.
nombreLabel.grid(row = 0, column = 0,sticky = "e", pady=10, padx=10)

nombreTexto = Entry(miFrame)
nombreTexto.grid(row = 0, column = 1, pady=10, padx=10) 
#cuadroTexto.config(fg="green",bg="black",justify="left") #Asi modifico el campo del texto.


apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row = 1, column = 0, sticky = "e", pady=10, padx=10)

apellidoTexto = Entry(miFrame)
apellidoTexto.grid(row = 1, column = 1, pady=10, padx=10) 

passLabel = Label(miFrame, text="Password:")
passLabel.grid(row = 2, column = 0, sticky = "e", pady=10, padx=10)

passTexto = Entry(miFrame)
passTexto.grid(row = 2, column = 1, pady=10, padx=10) 
passTexto.config(show="*") #Asi convierto la contraseña en asteriscos(muestro los asteríscos)

comentariosLabel = Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row = 3, column = 0, sticky = "e", pady=10, padx=10)

textoComentario = Text(miFrame, width = 16, height = 5)
textoComentario.grid(row = 3, column = 1, padx = 10, pady = 10)

barraDesplazamientoY = Scrollbar(miFrame, command = textoComentario.yview) #Asi constrimos una barra de desplazamiento que pertenece al texto comentario que funciona de manera vertical.
barraDesplazamientoY.grid(row = 3, column = 2, sticky = "nsew") #Colocacion del Scrollbar, ese sicky hace que el Scrollbar se ajuste al tamaño del textbox

textoComentario.config(yscrollcommand=barraDesplazamientoY.set) #La barra de desplazamiento se desplaza en el punto que nos encontremos.

def funcionBoton():
	
	print("Si sirve el botón.")


botonEnviar = Button(raiz, text="Enviar", command=funcionBoton) #Asi se crea el boton y ese command aqui lo que hace es llamar a una accion a un metodo.

botonEnviar.pack()

raiz.mainloop()