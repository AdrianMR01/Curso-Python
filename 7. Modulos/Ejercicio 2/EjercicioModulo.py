# Crear un modulo #
# Añadir la clase 'Coche' creada en un ejercicio anterior #
class Coche:
	def __init__(self,marca,color,combustible,cilindrada):
		self.marca = marca
		self.color = color
		self.combustible = combustible
		self.cilindrada = cilindrada
	def mostrar_caracteristicas(self):
		print("""¿Que desea consultar sobre su vehiculo?
1) Marca       3) Combustible	5) Todo
2) Color       4) Cilindrada""")
		consulta = input('- Seleccione una opción -\n')
		if consulta == '1':
			print(f'La marca de su vehiculo es {self.marca}')
		elif consulta == '2':
			print(f'El color de su vehiculo es {self.color}')
		elif consulta == '3':
			print(f'El combustible de su vehiculo es {self.combustible}')
		elif consulta == '4':
			print(f'La cilindrada de su vehiculo es {self.cilindrada}')
		elif consulta == '5':
			print(f"""Marca: {self.marca}		Color: {self.color}
Combustible: {self.combustible}	 Cilindrada: {self.cilindrada}""")
		else:
			print('Ninguna opción fue seleccionada')
# Añadir la función lambda creada en un ejercicio anterior #
media = lambda calif_1,calif_2,calif_3 : (calif_1+calif_2+calif_3)/3
