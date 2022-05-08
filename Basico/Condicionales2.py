print("Verificación de Acceso")

edad_usuario = int(input("Introduce tu edad: "))

if(0<edad_usuario<100):#Se pueden hacer con mas condiciones o sea(salario_administrativo<salario_jefe<salario_presidente) y hasta mas.
	if(edad_usuario < 18):
		print("No puedes pasar.")
	elif(edad_usuario>=18):
		print("Puedes pasar")
else:
	print("Edad Incorrecta.")

