from tkinter import *

root = Tk()

root.title("Ejemplo")

beach = IntVar()
mountain = IntVar()
RuralTourism = IntVar()

def opcionesViaje():

	opcionEscogida=""
	if beach.get()==1:
		opcionEscogida+=" Playa"
	if mountain.get()==1:
		opcionEscogida+=" Montaña"
	if RuralTourism.get()==1:
		opcionEscogida+=" Turismo Rural"

	textoFinal.config(text=opcionEscogida)

foto = PhotoImage(file="avion.png")

Label(root, image=foto).pack()#Colocamos la imagen en un label donde voy a poder moverla y demas.

frame = Frame(root)
frame.pack()
Label(frame, text = "Elige destinos: ", width=50).pack()


Checkbutton(frame, text="Playa", variable=beach, onvalue=1, offvalue=0, command=opcionesViaje).pack()#Ese onvalue lo que hace es que al estar presionada la opcion de playa va almacenar un uno, el offvalue es lo contrario.
Checkbutton(frame, text="Montaña", variable=mountain, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo Rural", variable=RuralTourism, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal = Label(frame)
textoFinal.pack()

root.mainloop()