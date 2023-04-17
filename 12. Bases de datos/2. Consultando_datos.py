import sqlite3

Data_Base = sqlite3.connect('Data_Base.db')

cursor = Data_Base.cursor()

# Consultando datos con for #
cursor.execute("SELECT * FROM PEOPLE")

people = cursor.fetchall() # Permite seleccionar todos los datos

for person in people:
	print(person)
#---------------------------#

# Consultando datos con WHERE #
cursor.execute("SELECT * FROM PEOPLE WHERE edad > 19 and edad < 50")

select_people = cursor.fetchall() # Permite seleccionar todos los datos
print('\n')
for person in select_people:
	print(person)
#-----------------------------#

# Ordenando datos #
cursor.execute("SELECT * FROM PEOPLE ORDER BY edad")

order_list = cursor.fetchall()
print('\n')
for people in order_list:
	print(people)

#-----------------#
Data_Base.close()