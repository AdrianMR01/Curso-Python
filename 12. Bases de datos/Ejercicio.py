'''
Crear una base de datos 'basededatos.db'
Crear una tabla "productos" con 3

id : Identificador del producto de tipo
nombre : del producto de tipo texto
precio: Precio del producto de tipo numérico

Insertar 3 productos en la tabla -productos
1, "Impresora" , 300
2, "Raton- , 20
3, "Ordenador" , 600

Consultar los productos de la tabla -productos
Cerrar la base de datos basededatos. db
'''
import sqlite3

Data_Base = sqlite3.connect("Productos.db")
cursor = Data_Base.cursor()

cursor.execute("DROP TABLE Productos")
cursor.execute("CREATE TABLE Productos(id INTEGER, nombre TEXT, precio INTEGER)")

product_list = [
(1,'Impresora',300),
(2,'Raton',20),
(3,'Ordenador',600)
]

cursor.executemany("INSERT INTO Productos VALUES(?,?,?)",product_list)
cursor.execute("SELECT * FROM Productos")

productos = cursor.fetchall()

for producto in productos:
	print(producto)

Data_Base.commit()
Data_Base.close()