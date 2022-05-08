import sqlite3

miConexion = sqlite3.connect("PrimeraBaseDeDatos") #Asi se abre o crea y abre al mismo tiempo una base de datos.

miCursor=miConexion.cursor()#Asi creamos el puntero o cursor

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO_ARTICULO INTEGER, SECCION VARCHAR(20))")#Asi se crea digamos una tabla con sus datos.

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 5000,'DEPORTES')")#Asi se inserta valores en una tabla.
'''

listaProductos = [
	
	("CAMISETA",4000,"DEPORTES"),	
	("JARRÓN",2000,"CERÁMICA"),	
	("CAMIÓN",2500,"JUGUETERÍA")	

]#Esto se pudo haber hecho con INSERT INTO pero
#al hacer esto nos ahorramos tiempo si vamos a ingresar
#varios elementos y es mas cómodo.

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", listaProductos)#Asi se usa para insertar una lista por ejemplo. Los signos de pregunta representan cuantos elementos tiene la tupla en este caso.
'''

miCursor.execute("SELECT * FROM PRODUCTOS")

listaProductos=miCursor.fetchall() #Asi nos devuelve una lista de todos los registros que nos devuelve la instruccion SQL anterior.

for producto in listaProductos:

	print("Nombre Artículo: ",producto[0]," Sección: ",producto[2])

miConexion.commit()#Es como confirmar los cambios que vamos a realizar.


miConexion.close()