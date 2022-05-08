from tkinter import *

raiz = Tk()

varSeleccion = IntVar()

l = Label(raiz, text="Pelicula Favorita: ").grid(columnspan=2)



r1 = Radiobutton(raiz, text="Accion", variable = varSeleccion, value = 1).grid(row=2, column=1)


r2 = Radiobutton(raiz, text="Terror", variable = varSeleccion, value = 2).grid(row=3, column=1)

r3 = Radiobutton(raiz, text="Romance", variable = varSeleccion, value = 3).grid(row=4, column=1)


r4 = Radiobutton(raiz, text="Suspenso", variable = varSeleccion, value = 4).grid(row=5, column=1)


#Ya hice lo basico pero quiero alinearlo, aun no se pero en los siguientes videos ya lo voy a hacer.


raiz.mainloop()
