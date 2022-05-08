'''
Metodos de Cadenas
upper() Hace que todo este en mayuscula
lower() Hace que todo este en minuscula
capitalize() Pone la primer letra en mayuscula
title() Todas Las Primeras Letras En Mayúsculas
count() Cuenta cuantas veces aparece una letra o una cadena dentro de una frase o texto
find() Representa el indice donde se encuentra un caracter o grupo de caracteres
isdigit() Nos devuelve un booleano, si hay un digito o valor numero si o no
isalum() Comprueba si son alfas numericos
isalpha() Comprueba si hay solo letras
split() Separa por palabras utilizando espacios
strip() Borra los espacios sobrantes al principio y al final
replace() Cambia una letra o palabra por otra
rfind() Representa el indice donde se encuentra un caracter o grupo de caracteres pero de atras a delante.

'''



edad = input("Introduce la edad: ")

#print(edad.isdigit())#Asi verificamos si digitamos una edad o no, o sea digitos numericos

while(edad.isdigit() == False):#Asi se verifica si la edad esta escrita con numeros o no.
	print("Por favor introduce un valor numerico.")
	edad = input("Introduce la edad: ")

if(int(edad)<18):

	print("No puede pasar.")
else:
	print("Puede pasar.")

