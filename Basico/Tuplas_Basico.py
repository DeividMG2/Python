#Datos
#No se permite añadir, eliminar, mover elementos, etc(son listas inmutables).
#Si permiten extraer porciones, pero el resultado de la extraccion es una nueva tupla.
#Si permiten busquedas(index).
#Si permiten comprobar si un elemento se encunetra en una tupla.
#Algunas utilidades o ventajas de la lista es que son 
#Mas rapidas, al ejecutar.
#Menos espacio(menos espacio en memoria que la lista, mejor optimizacion).
#Formatean Strings.
#Pueden utilizarse como claves en un diccionario.(las listas no)
#Sintaxis:
#nombreTupla=(elem1,elem2,elem3), los parentesis se pueden omitir.
miTupla=("Juan",13,1,1995)
print(miTupla[1])#Aqui imprime el elemento que se encuentre en el indice 1
miLista = list(miTupla)#Acá se convierte la tupla en una lista, y para hacerlo al reves es tuple(miLista), o sea asi se convierte lista a tupla.
print("Juan" in miTupla)#Aqui verifica si Juan esta en la tupla.
print(miTupla.count(13))#Aquí nos cuenta cuantos 13 hay en la tupla
print(len(miTupla))#Esta funcion de len es para ver la longitud de la tupla
miTuplaUnitaria = ("Juan",)  #Esto es una tupla unitaria y asi se crea, debe tener esa ","
print(len(miTuplaUnitaria)) 
nombre, dia, mes, agno = miTupla#Aqui se asignan los valores de la tupla a las variables en orden. Esto es conocido como DESEMPAQUETA DE TUPLAS.
print(dia)