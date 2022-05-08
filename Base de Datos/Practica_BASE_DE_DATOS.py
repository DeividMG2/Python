from tkinter import *
from tkinter import messagebox
import sqlite3
import re


ventana = Tk()

ventana.geometry("400x500")
idVar=StringVar()
nombreVar = StringVar()
apellidoVar = StringVar()
direccionVar = StringVar()
passwordVar = StringVar()
usuarioVar = StringVar()
parametroNombre = StringVar()


def crearRegistro():

	if nombreVar.get()!="" and apellidoVar.get()!="" and usuarioVar.get()!="" and passwordVar.get()!="" and direccionVar.get()!="":
		try:
			miConexion = sqlite3.connect("BaseDeDatos")
			miCursor = miConexion.cursor()
			listaUsuario=[nombreVar.get(),passwordVar.get(),direccionVar.get(),apellidoVar.get(),txtComentario.get("1.0",END),usuarioVar.get()]

			miCursor.execute("INSERT INTO USUARIOS VALUES(NULL,?,?,?,?,?,?)",listaUsuario)
			messagebox.showinfo("INFO","Se ha registrado correctamente")

			miConexion.commit()
			miConexion.close()
		except:
			messagebox.showerror("ERROR","Este usuario ya está registrado")
	else:
		messagebox.showerror("ERROR", "Campos incompletos")

def eliminarRegistro():

	if idVar.get()!="":
		try:
			miConexion = sqlite3.connect("BaseDeDatos")
			miCursor = miConexion.cursor()

			miCursor.execute("DELETE FROM USUARIOS WHERE ID=?",(int(idVar.get()), ))

			miConexion.commit()
			miConexion.close()
			messagebox.showinfo("INFO","El registro ha sido eliminado")
		except:
			messagebox.showerror("ERROR", "Ha ocurrido un error")
	else:
		messagebox.showinfo("Error","Primero debes buscar al usuario que deseas eliminar")



def leerRegistro():

	if idVar.get()!="":
		try:
			miConexion=sqlite3.connect("BaseDeDatos")
			miCursor=miConexion.cursor()

			miCursor.execute("SELECT * FROM USUARIOS WHERE ID=?",(int(idVar.get()), ))
			#consulta.execute("SELECT * FROM producto WHERE id = ?", (a, )) #Esta es la manera para comparar info de la base de datos con una variable.
			borrarCampos(1)
			listaInfo=miCursor.fetchall()
			for i in listaInfo:
				nombreVar.set(i[1])
				passwordVar.set(i[2])
				direccionVar.set(i[3])
				apellidoVar.set(i[4])
				txtComentario.insert(1.0,i[5])
				usuarioVar.set(i[6])

			miConexion.commit()
			miConexion.close()
		except:
			messagebox.showwarning("ERROR", "Ha ocurrido un error")

		if usuarioVar.get() == "":
			messagebox.showinfo("INFO", "Usuario inexistente")
	else:
		messagebox.showinfo("Error", "Primero debes buscar al usuario que deseas ver")


def actualizarRegistro():

	if idVar.get()!="":
		miConexion = sqlite3.connect("BaseDeDatos")
		miCursor=miConexion.cursor()

		if nombreVar.get() != "" and apellidoVar.get() != "" and usuarioVar.get() != "" and passwordVar.get() != "" and direccionVar.get() != "":

			lista = (nombreVar.get(), apellidoVar.get(),passwordVar.get(),direccionVar.get(), txtComentario.get("1.0",END), usuarioVar.get(),idVar.get())

			miCursor.execute("UPDATE USUARIOS SET NOMBRE=?,APELLIDO=?,PASSWORD=?,DIRECCION=?,COMENTARIO=?,USUARIO=? WHERE ID = ?",lista)

			messagebox.showinfo("INFO","Registro actualizado correctamente")

			miConexion.commit()
			miConexion.close()
		else:
			messagebox.showerror("ERROR", "Campos incompletos")
	else:
		messagebox.showinfo("Error","Primero debes buscar el usuario que deseas actualizar")

def conectarBase():

	try:
		miConexion=sqlite3.connect("BaseDeDatos")
		miCursor = miConexion.cursor()
		miCursor.execute('''
			CREATE TABLE USUARIOS(

			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE VARCHAR(50),
			PASSWORD VARCHAR(20),
			DIRECCION VARCHAR(50),
			APELLIDO VARCHAR(50),
			COMENTARIO VARCHAR(50),
			USUARIO VARCHAR(20) UNIQUE
			)

			''')
		miConexion.close()
		messagebox.showinfo("AVISO!","Conexion establecida con éxito")
	except:
		messagebox.showwarning("ERROR","La base de datos ya está conectada")

def borrarCampos(valor):

	if valor == 0:
		apellidoVar.set("")
		txtComentario.delete(1.0,END)
		nombreVar.set("")
		passwordVar.set("")
		idVar.set("")
		direccionVar.set("")
		usuarioVar.set("")
	else:
		apellidoVar.set("")
		txtComentario.delete(1.0, END)
		nombreVar.set("")
		passwordVar.set("")
		direccionVar.set("")
		usuarioVar.set("")

def salidaUsuario():

	valor = messagebox.askquestion("SALIR","¿Estas seguro que deseas salir?")#Asi es un messagebox de PREGUNTAR
	
	if valor=="yes":
		ventana.destroy()
		
#-------------Se agrega el menu----------

barraMenu=Menu(ventana)
ventana.config(menu=barraMenu)

baseDeDatosMenu = Menu(barraMenu, tearoff=0)
baseDeDatosMenu.add_command(label="Conectar", command = conectarBase)
baseDeDatosMenu.add_command(label="Salir", command = salidaUsuario)

borrarDatosMenu = Menu(barraMenu, tearoff=0)
borrarDatosMenu.add_command(label="Borrar Todos Los Campos",command= lambda: borrarCampos(0))

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Create",command = crearRegistro)
crudMenu.add_command(label="Read", command = leerRegistro)
crudMenu.add_command(label="Update",command=actualizarRegistro)
crudMenu.add_command(label="Delete",command=eliminarRegistro)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Acerca de")
ayudaMenu.add_command(label="Licencia")

barraMenu.add_cascade(label="BBDD", menu=baseDeDatosMenu)
barraMenu.add_cascade(label="BORRAR", menu=borrarDatosMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="AYUDA",menu = ayudaMenu)

#----------Se agregan los LABEL, ENTRY y BUTTON---------------


lblId = Label(ventana, text="Buscar Id").grid(row = 1, column=3,sticky="e",pady=10,padx=10)
txtId = Entry(ventana, textvariable=idVar, width=10).grid(row=1,column=4,pady=10)

lblNombre = Label(ventana, text="Nombre").grid(row = 1, column=1,sticky="e",pady=10)
txtNombre = Entry(ventana, textvariable=nombreVar).grid(row=1,column=2,pady=10)

lblUsuario = Label(ventana, text="Usuario").grid(row = 2, column=1,sticky="e",pady=10)
txtUsuario = Entry(ventana, textvariable=usuarioVar).grid(row=2,column=2,pady=10)


lblApellido = Label(ventana, text="Apellido").grid(row = 3, column=1,sticky="e",pady=10)
txtApellido = Entry(ventana, textvariable=apellidoVar).grid(row=3,column=2,pady=10)

lblDireccion = Label(ventana, text="Dirección").grid(row = 4, column=1,sticky="e",pady=10)
txtDireccion = Entry(ventana, textvariable=direccionVar).grid(row=4,column=2,pady=10)

lblPassword = Label(ventana, text="Contraseña").grid(row = 5, column=1,sticky="e",pady=10)
txtPassword = Entry(ventana, textvariable=passwordVar)
txtPassword.grid(row=5,column=2,pady=10)
txtPassword.config(show="*")

lblComentario = Label(ventana, text="Comentario").grid(row = 6, column=1,sticky="e",pady=10)
txtComentario = Text(ventana, width = 16, height = 5)
txtComentario.grid(row=6,column=2,pady=10)

barraComentario = Scrollbar(ventana, command = txtComentario.yview)

barraComentario.grid(row = 6, column = 3, sticky="nsew")

txtComentario.config(yscrollcommand=barraComentario.set)

btnCrear = Button(ventana, text="Create",width=10,command = crearRegistro).place(x=10,y=315)
btnLeer = Button(ventana, text="Read",width=10, command = leerRegistro).place(x=110,y=315)
btnActualizar = Button(ventana, text="Update",width=10,command=actualizarRegistro).place(x=210,y=315)
btnBorrar = Button(ventana, text="Delete",width=10,command=eliminarRegistro).place(x=310,y=315)

def buscarNombre():
	

	miConexion = sqlite3.connect("BaseDeDatos")
	miCursor = miConexion.cursor()

	miCursor.execute("SELECT NOMBRE FROM USUARIOS WHERE NOMBRE LIKE '%parametroNombre.get()%' ")
	
	
	miLista = miCursor.fetchall()	
	print(miLista)
	if(len(miLista)>0):
		print("Nombres con ",parametroNombre.get(),": ")
		for i in miLista:
			print(i)
	else:
		print("No hay nombres con: ",parametroNombre.get())
			
	miConexion.commit()
	miConexion.close()


lbl_buscarXNombre = Label(ventana, text="Buscar X Nombre").grid(row = 2, column=3)
txt_buscarXNombre = Entry(ventana, textvariable=parametroNombre, command= buscarNombre()).grid(row=2, column=4)
btnMostrar = Button(ventana, text="Mostrar", command=lambda:buscarNombre()).grid(row=3, column=4)
print("Entrada: ",parametroNombre.get())


ventana.mainloop() 