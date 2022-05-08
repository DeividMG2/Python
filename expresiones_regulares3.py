import re

cadena1 = "Jara López"

cadena2 = "Antonio Gomez"

cadena3 = "Lara Lopez"

#El match busca solo al inicio de la cadena
'''if re.match(".ara", nombre3, re.IGNORECASE): #Aqui nos verifica si existe Sandra en la lista o el valor que le enviemos. Con ese tercer parametro hacemos que no importe la mayuscula o minusculas. Y ese punto en el primer parametro significa que puede ser cualquier valor ahi.
if re.match("\d",cadena3):
	print("Encontramos EL NUMERO")
else:
	print("NUMERO No Encontrado")
'''

#El search busca en toda la cadena
'''
if re.search("L.pez",cadena1):
	print("Apellido Encontrado")
else:
	print("Apellido No Encontrado")'''

codigo1 = "kjahsdkjhaskjdh71jhadkjhas"
codigo2 = "jkhasdkhas71jhasd kjahsdjkhas"
codigo3 = "jkhasdjkhasd kjlasdkjas"

if re.search("71",codigo3 ):
	print("Encontrado")
else:
	print("No Encontrado")

