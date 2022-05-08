from tkinter import *

raiz = Tk()
raiz.iconify()
raiz.deiconify()
ventanaRegistro=Tk()
ventanaRegistro.iconify()

raiz.title("Fast Languages")
raiz.iconbitmap("icono1.ico")
ventanaRegistro.title("REGISTRO")


def abrirVentanaRegistro():
	raiz.iconify()
	ventanaRegistro.deiconify()

def salir():
	raiz.destroy()

def guardarInfo():
	
	Label(frame2, text="Nombre: "+nombreVar.get()).grid(row=3, column=1, pady=10)

frame1 = Frame(raiz, width="400", height="500", padx=20,pady=20)
frame1.pack()
frame1.grid_propagate(False)


Label(frame1, text="EL MEJOR LUGAR PARA APRENDER").grid(row=1, column=1, pady=10)


Button(frame1, text="Registrarse",command=abrirVentanaRegistro,width=15).grid(row=2, column=1, pady=10)

frame2 = Frame(ventanaRegistro, width="400", height="500", padx=20,pady=20)
frame2.pack()

def saluda():
	Label(frame1,text="Hola: "+entradaU.get()).grid(row=1, column=4, pady=10)
	print(entradaU.get())

raiz.geometry=("500x300+100+100")

lblUsuario=Label(frame1, text="Usuario: ").grid(row=3, column=1, pady=10)


entradaU=StringVar()
txtUsuario=Entry(frame1, textvariable=entradaU).grid(row=3, column=2, pady=10)


btnSaludar=Button(frame1,text="Saludar", command = lambda: saluda()).grid(row=4, column=1, pady=10)

raiz.mainloop()