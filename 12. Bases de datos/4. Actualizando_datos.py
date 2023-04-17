import sqlite3

Data_Base = sqlite3.connect("Data_Base.db")

cursor = Data_Base.cursor()

cursor.execute("UPDATE PEOPLE SET estudia = 'Licenciatura' WHERE edad < 50")

Data_Base.commit()
Data_Base.close()