#LABEL
from tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height=400)

miFrame.pack()
'''
miLabel = Label(miFrame, text="LABEL EJEMPLO: ")

miLabel.place(x=100,y=50) #Hacemos esto para permitir ubicar el label en cualquier lugar dentro de la ventana. Si usamos el .pack no respetará el tamaño del frame.
'''
Label(miFrame, text="LABEL EJEMPLO: ", fg="blue", font=("Times New Roman",14)).place(x=20,y=30) #Esto es una abreviacion de lo anterior documentado, una manera mas corta y fácil, sin usar variables.

root.mainloop()
