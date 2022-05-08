from tkinter import *

raiz = Tk()
 
miFrame = Frame(raiz)

miFrame.pack()
#-------Variables Globales--------------
numeros = []
operando = False
contadorEspacios = 0
num1 = 0
num2 = 0
simboloOperacion = ""
operacionActiva = False
contadorNum1 = 0
modificacion = False
newNumber = 0

#-------Creacion de la pantalla-----------

numeroPantalla = StringVar()
def inicio():

	numeroPantalla.set("0")

pantalla = Entry(miFrame, textvariable=numeroPantalla, command = inicio())
pantalla.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan=4) #Ese columnspan=4 hace que esta pantalla ocupe 4 columnas del grid.
pantalla.config(background="black", fg = "#03f943", justify = "right")

#-------Acciones o metodos--------




def numeroPulsado(digito):

	global numeros
	global operando
	global contadorEspacios
	global num1
	global num2
	global simboloOperacion 
	global modificacion
	global newNumber

	if(numeroPantalla.get() == "0"):
		numeroPantalla.set("")

	if digito != "0" :



		if digito == ".":


			punto = False

			for i in numeroPantalla.get():
				if i == ".":
					punto = True
					break
			
			if punto == False and len(numeroPantalla.get()) > 0:
				numeroPantalla.set(numeroPantalla.get()+digito)
				numeros.append(digito)


		elif digito == "<-":
			tam = len(numeroPantalla.get())
			n = numeroPantalla.get()
			numeroPantalla.set(n[0:tam-1])
			
			if len(numeros)>0:
				newNumber = float(numeroPantalla.get())
				numeros.pop()
			modificacion=True
		    

		elif digito == "<--":

			numeroPantalla.set("")
			numeros=[]
			


		elif digito == "+" or digito == "-" or digito == "X" or digito == "/":
			simboloOperacion = digito
			num1 = float(numeroPantalla.get())
			for i in digito:
				if digito == "+":
					botonSuma.config(fg="red")
					botonRes.config(fg="black")
					botonMult.config(fg="black")
					botonDiv.config(fg="black")
					operando = True
				elif digito == "-":
					botonSuma.config(fg="black")
					botonRes.config(fg="red")
					botonMult.config(fg="black")
					botonDiv.config(fg="black")
					operando = True
				elif digito == "X":
					botonSuma.config(fg="black")
					botonRes.config(fg="black")
					botonMult.config(fg="red")
					botonDiv.config(fg="black")
					operando = True
				elif digito == "/":
					botonSuma.config(fg="black")
					botonRes.config(fg="black")
					botonMult.config(fg="black")
					botonDiv.config(fg="red")
					operando = True



		else:

			if operando == False:
				numeroPantalla.set(numeroPantalla.get()+digito)
				numeros.append(digito)
				
			else:
				operacionActiva = True
				
				if contadorEspacios==0:
					numeroPantalla.set(""+digito)
					contadorEspacios+=1
				else:
					numeroPantalla.set(numeroPantalla.get()+digito)
					numeros.append(digito)
				operando = False
				contadorEspacios = 0
			botonSuma.config(fg="black")
			botonRes.config(fg="black")
			botonDiv.config(fg="black")
			botonMult.config(fg="black")
		


	else:

		if len(numeros)!=0:
			numeroPantalla.set(numeroPantalla.get()+digito)
			numeros.append(digito)

		


def operaciones():

	global num1
	global num2 
	global modificacion
	global newNumber

	num2 = float(numeroPantalla.get())

	if(modificacion):
		num1 = newNumber

	if(simboloOperacion == "+"):
		numeroPantalla.set(num1+num2)
		num1 = float(numeroPantalla.get())

	elif(simboloOperacion == "-"):
		numeroPantalla.set(num1-num2)
		num1 = float(numeroPantalla.get())

	elif(simboloOperacion == "X"):
		numeroPantalla.set("{:.2f}".format(num1*num2))
		num1 = float(numeroPantalla.get())
		

	elif(simboloOperacion == "/"):
		numeroPantalla.set("{:.2f}".format(num1/num2))
		num1 = float(numeroPantalla.get())
		
		
	





	



#---------fila 1--------------------

boton7 = Button(miFrame, text="7",width=3, command = lambda: numeroPulsado("7"))
boton7.grid(row = 2, column=1)
boton8 = Button(miFrame, text="8",width=3, command = lambda: numeroPulsado("8"))
boton8.grid(row = 2, column=2)
boton9 = Button(miFrame, text="9",width=3, command = lambda: numeroPulsado("9"))
boton9.grid(row = 2, column=3)
botonDiv = Button(miFrame, text="/",width=3, command = lambda: numeroPulsado("/"))
botonDiv.grid(row = 2, column=4)


#---------fila 2--------------------

boton4 = Button(miFrame, text="4",width=3, command = lambda: numeroPulsado("4"))
boton4.grid(row = 3, column=1)
boton5 = Button(miFrame, text="5",width=3, command = lambda: numeroPulsado("5"))
boton5.grid(row = 3, column=2)
boton6 = Button(miFrame, text="6",width=3, command = lambda: numeroPulsado("6"))
boton6.grid(row = 3, column=3)
botonMult = Button(miFrame, text="X",width=3, command = lambda: numeroPulsado("X"))
botonMult.grid(row = 3, column=4)

#----------fila 3--------------------

boton1 = Button(miFrame, text="1",width=3, command = lambda: numeroPulsado("1"))
boton1.grid(row = 4, column=1)
boton2 = Button(miFrame, text="2",width=3, command = lambda: numeroPulsado("2"))
boton2.grid(row = 4, column=2)
boton3 = Button(miFrame, text="3",width=3, command = lambda: numeroPulsado("3"))
boton3.grid(row = 4, column=3)
botonRes = Button(miFrame, text="-",width=3, command = lambda: numeroPulsado("-"))
botonRes.grid(row = 4, column=4)

#-----------fila 4--------------------

boton0 = Button(miFrame, text="0",width=3, command = lambda: numeroPulsado("0"))
boton0.grid(row = 5, column=1)
botonComa = Button(miFrame, text=",",width=3, command = lambda: numeroPulsado("."))
botonComa.grid(row = 5, column=2)
botonIgual = Button(miFrame, text="=",width=3, command = lambda: operaciones())
botonIgual.grid(row = 5, column=3)
botonSuma = Button(miFrame, text="+",width=3, command = lambda: numeroPulsado("+"))
botonSuma.grid(row = 5, column=4)

#------------fila 5-------------

botonEliminar = Button(miFrame, text="<-", width=3, command = lambda: numeroPulsado("<-"))
botonEliminar.grid(row = 6, column = 1)

botonLimpieza = Button(miFrame, text="<--", width=3, command = lambda: numeroPulsado("<--"))
botonLimpieza.grid(row = 6, column = 2)




raiz.mainloop()