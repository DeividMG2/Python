import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

#miCursor.execute('''
	#CREATE TABLE PRODUCTOS(
	#CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
	#NOMBRE_ARTICULO VARCHAR(50),
	#PRECIO INTEGER,
	#SECCION VARCHAR(20))
	
	#''')
'''
productos=[
	
	("AR01", "PELOTA", 4000, "JUGUETERÍA"),
	("AR02", "PANTALÓN", 6000, "CONFECCIÓN"),
	("AR03", "DESTORNILLADOR", 1000, "FERRETERÍA"),
	("AR04", "JARRÓN", 1000, "CERÁMICA")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?,?)", productos)

'''

miCursor.execute("INSERT INTO PRODUCTOS VALUES('AR03','AVION',1500,'JUGUETERÍA')")




miConexion.commit()

miConexion.close()