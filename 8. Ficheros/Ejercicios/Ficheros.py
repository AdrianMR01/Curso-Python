# Crear el modulo fichero que tenga las funciones
# leer un fichero
# grabar un fichero
# incluir un fichero
class Fichero:

	def __init__(self, nombre):
		self.nombre = nombre

	def leer_fichero(self):
		file = open(self.nombre,'rt')
		fichero = file.read()
		return fichero

	def grabar_fichero(self,fichero):
		file = open(self.nombre,'wt')
		fichero = input(str('Introduce el texto del fichero:\n'))
		file.write(fichero)
		file.close()

	def incluir_fichero(self,fichero):
		file = open(self.nombre,'at')
		fichero = input(str('Introduce el texto a añadir:\n')) 
		fichero = '\n'+fichero
		file.write(fichero)
		file.close()