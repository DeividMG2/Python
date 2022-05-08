miLista = ["María", "Juan","Luis","Pedro"]#Asi se crean las listas, puede tener cualquier tipo de dato.
print(miLista[-1])#Imprime el primer numero de atras a adelante y no se toma en cuenta el 0.
print(miLista[0:2])#Aqui se imprimen del 0 al 1, excluye el ultimo numero.
print(miLista[:3])#Otra forma donde se imprimen del 0 al 2, excluye el ultimo numero.
print(miLista[1:2])#Aqui imprimiria solo el 1
print(miLista[2:])#Acá es alreves, accede desde el indice 2 hasta el final
miLista.append("Rodrigo")#Asi se agrega un elemento a la lista.
miLista.insert(2, "Sandra")#Aqui nos agrega un elemento pero en el indice que queramos.
miLista.extend(["Andrea", "Jimena"])#Aqui agrega varios elementos a la lista.
print(miLista.index("Andrea"))#Aquí me dan el indice donde se encuentre Andrea, solo nos da el primer indice si hay 2 Andreas, en este caso imprimimos el indice.
print("María" in miLista)#Aqui nos devuelve True o False si el elemento que enviamos está en la lista
miLista.remove("María")#Aquí se elimina el elemento que agreguemos en los parentesis
miLista.pop()#Esta funcion elimina el ultimo elemento de la lista, le podemos agregar un indice y borra el elemento de ese indice
milista2=["Sandra", "Luis"]
milista3 = miLista+milista2#Aqui se hace una lista que concatena ambas listas.
print(milista3[:])
milista4 = ["Manuel",5,True,89.98]*3#Aqui repite los elementos de la lista 3 veces.
print(milista4[:])
print("Fin del Programa de Listas")
<<<<<<< HEAD
print("Aqui estoy en la rama master")
=======
print("Aqui estoy en la rama de prueba con el uso de Git")
>>>>>>> NombreRama
