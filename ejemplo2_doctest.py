def compruebaMail(mail):

	"""
	La funcion compruebaMail evalúa un mail
	recibido en busca de la @. Si tiene una @ 
	es correcto, si tiene mas de una @ es incorrecto
	si la @ está al final es incorrecto

	>>> compruebaMail('deivillo@guapo.com')
	True

	>>> compruebaMail('deivilloguapo.com@')
	False

	>>> compruebaMail('deivillo@guapo@.com')
	False

	>>> compruebaMail('deivilloguapo.com')
	False
	"""

	arroba = mail.count("@")

	if (arroba!=1 or mail.rfind("@")==(len(mail)-1) or mail.find("@")==0):
		return False
	else:
		return True


import doctest
doctest.testmod()
#En este ejemplo estos tests tienen mas utilidad

#Gracias a estas pruebas podemos ver errores y mejorar el codigo.