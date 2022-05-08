import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID = 5")
#Asi se elimina un valor de la base de datos.

miConexion.commit()
miConexion.close()

'''
miCursor.execute('''
#	CREATE TABLE PRODUCTOS(
#	ID INTEGER PRIMARY KEY AUTOINCREMENT,
#	NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#	PRECIO INTEGER,
#	SECCION VARCHAR(20))
''')#Asi el campo clave se autoincrementa asi que no tenemos que preocuparnos por el.
#con UNIQUE se impide que se repita la informacion o en este caso el mismo nombre.
productos=[
	
	("PELOTA", 4000, "JUGUETERÍA"),
	("PANTALÓN", 6000, "CONFECCIÓN"),
	("DESTORNILLADOR", 1000, "FERRETERÍA"),
	("JARRÓN", 1000, "CERÁMICA"),
	("PANTALONES", 2000, "CONFECCIÓN")

]



miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)
#se debe agregar ese NULL para que funcione el id autoincrementable.

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='CONFECCIÓN'")
#ASI USO EL WHERE

miCursor.execute("UPDATE PRODUCTOS SET PRECIO=3500 WHERE NOMBRE_ARTICULO='PELOTA'")
#Asi se actualiza un valor.


listaProductos=miCursor.fetchall()

print(listaProductos)


'''