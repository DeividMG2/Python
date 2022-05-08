from tkinter import *

raiz = Tk()
raiz.resizable(0,0)


raiz.title("Fast Languages")
raiz.iconbitmap("icono1.ico")

img = PhotoImage(file="descarga.pgm")
img = img.subsample(8, 8)



#-------VARIABLES CON VALORES DE ENTRADA----------
nombreVar = StringVar()
correoVar = StringVar()
contraseñaVar = StringVar()
contraseña2Var = StringVar()
opcionGeneroVar = IntVar()
registrado = StringVar()
registrado.set("Aún no estas registrado")
inicioSesion=StringVar()
inicioSesion.set("Aún no has iniciado sesión")
verifyNombre = StringVar()
verifyPassword = StringVar()


opcionElegida = []
espanol = IntVar()
ingles = IntVar()
aleman = IntVar()
frances = IntVar()
portugues = IntVar()

def salir():
	raiz.destroy()

def guardarInfo():
	labelsEnBlanco()
	global opcionElegida
	nuevoUsuario = True

	if len(nombreVar.get())<=0:

		labelNombre = Label(frame1, text="Nombre",fg="red").grid(row=5, column=1,sticky = "e")
		nuevoUsuario = False

#------------VERIFICAR E IMPRIMIR IDIOMAS--------
	if len(opcionElegida)>0:
		print("\nIdiomas Elegidos: ")
		for i in opcionElegida:
			print(i)
	else:
		labelIdiomas = Label(frame1, text="Idioma(s) para aprender",fg="red").grid(row=7, column=1,sticky = "e")
		nuevoUsuario = False

#------------VERIFICAR E IMPRIMIR GENEROS--------
	if opcionGeneroVar.get() != 1 and opcionGeneroVar.get() != 2:
		labelGenero = Label(frame1, text="Genero",fg="red").grid(row=6, column=1,sticky = "e")
		nuevoUsuario = False

#------------VERIFICAR E IMPRIMIR ESTADO DE CONTRASEÑAS--------
	if (contraseñaVar.get()==contraseña2Var.get())and(len(contraseñaVar.get())>=8):
		nuevoUsuario = True
	else:
		nuevoUsuario = False
		labelContraseña = Label(frame1, text="Contraseña",fg="red").grid(row=9, column=1,sticky = "e")
		labelContraseña2 = Label(frame1, text="Confirmar contraseña",fg="red").grid(row=10, column=1,sticky = "e")

#---------VERIFICAR HE IMPRIMIR ESTADO DE CORREO----------
	
	correoCorrecto = True
	error = 0

	for i in correoVar.get():

		if (i == " " or i == "!" or i == '"' or i == "#" or i == "$" or i == "%" or i == "," or i == ":" or i == "(" or i == ")" or i == "<" or i == "@" or i == "[" or i == ";" or i == "" or i == ">" or i == "]" or i == "|"):
			error+=1     

	if len(correoVar.get())<6 or len(correoVar.get())>30:
		error+=1  

	if error!=0:
		nuevoUsuario = False
		labelCorreo = Label(frame1, text="Correo",fg="red").grid(row=8, column=1,sticky = "e")



#----------REGISTRAR USUARIO--------
	if nuevoUsuario:
		registrado.set("Usuario Registrado Correctamente")
		lblInfoRegistro = Label(frame1, textvariable=registrado, font=("Times New Roman",12), fg="green").grid(row=1, column=3,columnspan=6,sticky="w",pady=10)

	else:
		registrado.set("Error Al Registrar Usuario")
		lblInfoRegistro = Label(frame1, textvariable=registrado, font=("Times New Roman",12), fg="red").grid(row=1, column=3,columnspan=6,sticky="w",pady=10)

def showPassword():

		entradaPassword = Entry(frame1, textvariable=contraseñaVar).grid(row=9, column=2, sticky="e")
		entradaPassword2 = Entry(frame1, textvariable=contraseña2Var).grid(row=10, column=2, sticky="e")	
		Button(frame1, image = img,command= lambda: hide_password()).grid(row = 9,column = 4)


def iniciarSesion():
	
	if registrado.get() == "Usuario Registrado Correctamente":

		if ((verifyNombre.get() == nombreVar.get()) and (verifyPassword.get()==contraseñaVar.get())):

			inicioSesion.set("Has iniciado sesión")
			lblInfoInicioSesion = Label(frame1, textvariable=inicioSesion, font=("Times New Roman",12), fg="green").grid(row=13, column=3,columnspan=6,sticky="w",pady=10)

		else:
			inicioSesion.set("Ha ocurrido un error con el usuario o la contraseña.")
			lblInfoInicioSesion = Label(frame1, textvariable=inicioSesion, font=("Times New Roman",12), fg="red").grid(row=13, column=3,columnspan=7,sticky="e",pady=10)


	else:
		inicioSesion.set("El usuario no ha sido registrado")
		lblInfoInicioSesion = Label(frame1, textvariable=inicioSesion, font=("Times New Roman",12), fg="red").grid(row=13, column=3,columnspan=6,sticky="w",pady=10)



def idiomasElegidos(valor):
	global opcionElegida
	v = valor in opcionElegida
	diccionarioIdiomas = {espanol.get():"Español ", ingles.get():"Inglés ", aleman.get():"Alemán ", frances.get():"Francés ", portugues.get():"Portugués "}
	
	for i in diccionarioIdiomas:
			
			if(i==1)and(v==False):
				opcionElegida.append(valor)	
			elif(v == True):
				if(valor in opcionElegida):
					opcionElegida.remove(valor)
		
	#print("Lista: ",opcionElegida, " valor: ",valor, " V: ",v)
			


frame1 = Frame(raiz, width="800", height="500", padx=20,pady=20)
frame1.pack()
frame1.grid_propagate(False)


Label(frame1, text="EL MEJOR LUGAR PARA APRENDER",font=("Times New Roman",14)).grid(row=0, column=1,columnspan=6,pady=5)

Label(frame1, text="REGISTRO",font=("Times New Roman",14)).grid(row=1, column=1,columnspan=3,pady=10,sticky="w")


def labelsEnBlanco():
	lblInfoRegistro = Label(frame1, textvariable=registrado, font=("Times New Roman",12), fg="red").grid(row=1, column=3,columnspan=6,sticky="w",pady=10)

	labelNombre = Label(frame1, text="Nombre").grid(row=5, column=1,sticky = "e")

	labelGenero = Label(frame1, text="Genero").grid(row=6, column=1,sticky = "e")

	labelIdiomas = Label(frame1, text="Idioma(s) para aprender").grid(row=7, column=1,sticky = "e")

	labelCorreo = Label(frame1, text="Correo").grid(row=8, column=1,sticky = "e")

	labelContraseña = Label(frame1, text="Contraseña").grid(row=9, column=1,sticky = "e")

	labelContraseña2 = Label(frame1, text="Confirmar contraseña").grid(row=10, column=1,sticky = "e")



labelsEnBlanco()

def hide_password():
	entradaPassword = Entry(frame1, textvariable=contraseñaVar)
	entradaPassword.grid(row=9, column=2, sticky="e")
	entradaPassword.config(show="*")
	entradaPassword2 = Entry(frame1, textvariable=contraseña2Var)
	entradaPassword2.grid(row=10, column=2, sticky="e")
	entradaPassword2.config(show="*")
	Button(frame1, image = img,command= lambda: showPassword()).grid(row = 9,column = 4)

hide_password()

entradaNombre = Entry(frame1, textvariable=nombreVar).grid(row=5,column=2)

Radiobutton(frame1, text="Masculino", variable=opcionGeneroVar, value=1).grid(row=6, column=2)
Radiobutton(frame1, text="Femenino", variable=opcionGeneroVar, value=2).grid(row=6, column=3)

Checkbutton(frame1, text="Español", variable = espanol, onvalue=1, offvalue=0,command = lambda: idiomasElegidos("Español ")).grid(row=7, column=2)
Checkbutton(frame1, text="Inglés", variable = ingles, onvalue=1, offvalue=0,command = lambda: idiomasElegidos("Inglés ")).grid(row=7, column=3)
Checkbutton(frame1, text="Alemán", variable = aleman, onvalue=1, offvalue=0,command = lambda: idiomasElegidos("Alemán ")).grid(row=7, column=4)
Checkbutton(frame1, text="Francés", variable = frances, onvalue=1, offvalue=0,command = lambda: idiomasElegidos("Francés ")).grid(row=7, column=5)
Checkbutton(frame1, text="Portugués", variable = portugues, onvalue=1, offvalue=0,command = lambda: idiomasElegidos("Portugués ")).grid(row=7, column=6)

entradaCorreo = Entry(frame1, textvariable=correoVar).grid(row=8, column=2, sticky="e")
labelFinalCorreo = Label(frame1, text="@gmail.com").grid(row=8, column=3,sticky = "w")
Label(frame1, text="(6-30) caracteres").grid(row=8, column=4,columnspan=6,sticky = "w")

 

Label(frame1, text="(+8) caracteres").grid(row=9, column=3,columnspan=6,sticky = "w")

Label(frame1, text="(+8) caracteres").grid(row=10, column=3,columnspan=6,sticky = "w")


Button(frame1, text="Aceptar", width=15, command= lambda: guardarInfo()).grid(row = 11, column=2)
Button(frame1, text="Salir",command=salir,width=15).grid(row=12, column=2,pady=10)


Label(frame1, text="INICIO DE SESIÓN",font=("Times New Roman",14)).grid(row = 13, column=1, columnspan=6,sticky="w",pady=10)
lblInfoInicioSesion = Label(frame1, textvariable=inicioSesion, font=("Times New Roman",12), fg="red").grid(row=13, column=3,columnspan=6,sticky="w",pady=10)


Label(frame1, text="Nombre: ",pady=10).grid(row=14,column=1, sticky="e")
Label(frame1, text="Contraseña: ",pady=10).grid(row=15,column=1, sticky="e")


entradaVerifyNombre = Entry(frame1, textvariable=verifyNombre).grid(row=14,column=2)
entradaVerifyPassword = Entry(frame1,textvariable=verifyPassword)
entradaVerifyPassword.grid(row=15,column=2)
entradaVerifyPassword.config(show="*")

Button(frame1, text="ENTRAR", command = lambda: iniciarSesion()).grid(row=16,column=2)


raiz.mainloop()