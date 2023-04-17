# Ejercicio 1 #
# Crear una clase 'Coche' que tenga estos atributos:...
# marca,color,combustible y cilindrada #
class Choche:
# Crear la función __init__ que asigna los parametros de la clase...
# a los atributos de la clase #
	def __init__(self,marca,color,combustible,cilindrada):
		self.marca = marca
		self.color = color
		self.combustible = combustible
		self.cilindrada = cilindrada
# Crear otra función 'mostrar_caracteristicas' que mediante print...
# muestre por pantalla las caracteristicas (o atributos) que tiene el coche #
	def mostrar_caracteristicas(self):
		print("""¿Que desea consultar sobre su vehiculo?
1) Marca       3) Combustible	5) Todo
2) Color       4) Cilindrada""")
		consulta = int(input('- Seleccione una opción -\n'))
		if consulta == 1:
			print(f'La marca de su vehiculo es {self.marca}')
		elif consulta == 2:
			print(f'El color de su vehiculo es {self.color}')
		elif consulta == 3:
			print(f'El combustible de su vehiculo es {self.combustible}')
		elif consulta == 4:
			print(f'La cilindrada de su vehiculo es {self.cilindrada}')
		elif consulta == 5:
			print(f"""Marca: {self.marca}		Color: {self.color}
Combustible: {self.combustible}	 Cilindrada: {self.cilindrada}""")
		else:
			print('Ninguna opción fue seleccionada')
# Crear un objeto 'coche_1' de la clase 'Coche' con los atributos...
# 'Opel','rojo','gasolina','1.6' #
coche_1 = Choche('Opel','rojo','gasolina',1.6)
# Ejecutar la función 'mostrar_caracteristicas' del objeto 'cohche_1' #
coche_1.mostrar_caracteristicas()
#######################################################################

# Ejercicio 2 #
# Crear una función lambda que clacule la media de 3 calificaciones #
media = lambda calif_1,calif_2,calif_3 : (calif_1+calif_2+calif_3)/3
# i = 0
# while(i <= 3):
# 	i += 1
# 	calificacion = int(int(f'Introduce tu calificación {i}'))
print(f'La media de calificaciones es {media(6,5,6):.2f}')
#####################################