#Los diccionarios pueden almacenar valores de diferentes de tipo, se crea una asociacion
# de tipo clave : valor
#Los elementos almacenados no están ordenados.
#Sintaxis:
#nombre_Diccionario = {nombre_clave : nombre_valor, nombre:clave2 : nombre_valor2}
miDiccionario = {"Alemania" : "Berlin", "Francia":"París", "Reino Unido": "Londres", "España":"Madrid"}#Asi se crea un diccionatrio
miDiccionario["Italia"] = "Lisboa" #Asi se agrega un nuevo elemento al diccionario

print(miDiccionario)

miDiccionario["Italia"]="Roma"#Asi se modifica un elemento del diccionario
print(miDiccionario)

del miDiccionario["Reino Unido"]#Asi se elimina un elemento del diccionario
print(miDiccionario)

diccionario2 = {"Alemania":"Berlin",23:"Jordan","Mosqueteros":3}#Diccionario con valores de diferente tipo
print(diccionario2)

miTupla = ("España","Francia","Reino Unido","Alemania")
miDiccionario2 = {miTupla[0]:"Madrid",miTupla[1]:"París",miTupla[2]:"Londres",miTupla[3]:"Berlin"}#Asi se le asigna los valores de una lista a las claves de un diccionario
print(miDiccionario2["Francia"])#Puedo acceder asi a un elemento o con sub[miTupla[1]]

miDiccionario3 = {23:"Jordan","Nombre": "Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}#Aqui se mete un  diccionario dentro de con varios valores para una clave, pero no pueden existir varias claves con un solo valor
print(miDiccionario3["anillos"])
print(miDiccionario3["anillos"]["temporadas"][2])#Aqui accedo e imprimo a un elemento dentro de la lista que esta dentro de un diccionario dentro de otro diccionario.

print(miDiccionario3.keys())#Asi imprimo las claves del diccionario
print(miDiccionario3.values())#Así imprimo los valores del diccionario
print(len(miDiccionario3))#Asi imprimo la longitud del diccionario
