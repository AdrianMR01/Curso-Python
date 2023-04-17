import sqlite3

# Creando la Base de datos #
Data_Base = sqlite3.connect("Data_Base.db") # Crea o conecta a una base de datso que ya existe
cursor = Data_Base.cursor() # Permite ejecutar sentencias dentro de las bases de datos
#-------------------------#

# Creando una tabla #
cursor.execute("DROP TABLE PEOPLE") # Elimina la tabla people
cursor.execute('CREATE TABLE PEOPLE(nombre TEXT, apellido_pat TEXT, apellido_mat TEXT, edad INTEGER, estudia TEXT)')
'''Solo se permite crear la tabla una vez
en caso de que esta ya exista marcara un error''' 
#-------------------#

# Insertando datos #
cursor.execute("INSERT INTO PEOPLE VALUES ('Adrian','Martinez','Rios',21,'si')")
#------------------#

# Insertando varios datos #
'''Es necesario crear una lista de todas las filas que se van a insertar en la tabla'''
people_list = [
('Francisco Javier','Martinez','Reyes',61,'no'),
('Margarita','Rios','Martinez',52,'no'),
('Frida Elizabeth','Lopez','Camargo',23,'si'),
('Montserrat','Martinez','Rios',27,'si')
]
cursor.executemany("INSERT INTO PEOPLE VALUES (?,?,?,?,?)",people_list)
''' .executemany permite colocar varios datos a la vez, los signos ? indican los
campos que tiene la tabla en el que vamos a agregar las filas'''
#-------------------------#

# Parametros finales #
Data_Base.commit() # Confirma los cambios hechos
Data_Base.close() # Siempre tiene que ir al ultimo
#--------------------#