#Seguidamente se hará un programa que ejemplifica el uso del operador in
print("Asignatauras Optativas Año 2020")
print("Asignatauras Optativas: Informatica Grafica - Pruebas de Software - Usabilidad y Accesibilidad")
opcion = input("Escribe la asignatura escogida: ")
asignatura = opcion.lower()

if asignatura in ("informatica grafica","pruebas de software", "usabilidad y accesibilidad"):
	print("Asignatura escogida: "+asignatura)
else:
	print("La asignatura no está contemplada.")