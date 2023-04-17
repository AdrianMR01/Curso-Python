# Clases y objetos #
# Una clase es un contructor de objetos #
class ClaseSilla: # Clase #
	color = 'blanco' # Propiedades de la clase
	precio = 100

objeto_silla = ClaseSilla() # A una variables se le puede asignar la clase #

# Si se coloca la variable que contiene la clase + .propiedad de la clase...
# arroja el valor que tiene asignado la propiedad #
print(objeto_silla.color);print(objeto_silla.precio)

objeto_silla_2 = ClaseSilla()
# Se pueden cambiar los atributos de la clase para un solo uso #
objeto_silla_2.color = 'verde'
objeto_silla_2.precio = 200

print(objeto_silla_2.color);print(objeto_silla_2.precio)
# Creando asi otro objeto y teniendo ahora 2 objetos #

class Persona:

	def __init__(self,nombre,edad):# Los atributos de una clase son las caracteristicas...
	 # estos se colocan despues del self #
		self.nombre = nombre
		self.edad = edad

	def saludar(self):
		print(f'Hola, me llamo {self.nombre} y tengo {self.edad} años')

nombre = input('Introduce tu nombre: ')
edad = int(input('Introduce tu edad: '))

persona_1 = Persona(nombre,edad) # Para poder trabajar con las clases, a una variable...
# variable = Nompre de la clase(atributos separados or comas) #

# Una vez asignados los valores a los atributos, para visualizar el resultado... # 
print(persona_1.nombre);print(persona_1.edad)
# En el caso de saludar, como se tiene como otra acción dentri de la clase se coloca... # 
persona_1.saludar()