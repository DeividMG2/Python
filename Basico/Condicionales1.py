#Ejemplo de su uso:

nota_alumno = int(input("Ingrese su nota:  "))
def evaluacion(nota):
	valoracion = "APROBADO"
	if(nota<70):
		valoracion = "REPROBADO"

	return valoracion

print(evaluacion(nota_alumno))	