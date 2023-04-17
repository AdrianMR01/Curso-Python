import sqlite3

Data_Base = sqlite3.connect("Data_Base.db")

cursor = Data_Base.cursor()

cursor.execute("DELETE FROM PEOPLE WHERE nombre = 'Adrian'")

Data_Base.commit()
Data_Base.close()