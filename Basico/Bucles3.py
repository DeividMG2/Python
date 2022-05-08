print("Bucles: Continue, pass y else")
#Continue lo que hace es saltar a la siguiente interacción de bucle.
#Pass lo que hace es devolver null en cuanto se lee en interior del bucle, es 
#como si no se leyera el bucle.
#Else lo que hace es lo mismo que en un condicional.
for letra in "Python":
	
	if letra == "h":
		continue#Aqui ignorará el resto del punto y pasara al resto de interacción del bucle.
		#O bien ignora lo que hay abajo del bucle y lo salta al principio del bucle.

	print("Viendo la letra: "+letra)

#Ejemplo de su uso de continue:
nombre = "Pildoras Informaticas"
contador = 0

for i in nombre:
	if(i == " "):
		continue
	contador+=1

print(contador)

#Ejemplo de uso de pass

#while True:
	#pass #Mantiene el programa ocupado hasta que el usuario presione Contrl+c

#Otro ejemplo
#class mi_clase
	#pass #Para implementar mas tarde.

#Ejemplo uso del Else
email = input("Introduce email: ")
for i in email:
	if i == "@":
		arroba = True
		break
else: #Aqui se ejecuta cuando termine de recorrer el for, o sea si no hubiese estado
# ese break, se ejecutaría el else.

	arroba = False
print(arroba)
