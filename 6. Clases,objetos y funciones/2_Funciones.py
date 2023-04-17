# Funciones #
# Son bloques de código que se ejecutan cuando son llamados #

def saludar():
	print('Buenos días')

saludar() #Asi se manda a llamar la función #

# Dentro de la función podemos establecer ciertos parametros #
def saludar(nombre):
	print('Buenos días ' + nombre)

# La función la mandamos a llamar de la siguiente manera #

nombre = 'Adrian' # Hay que crear las variables que tiene la función #
saludar(nombre)
##################################

# return #
def sumar(num_1,num_2):
	suma = num_1 + num_2
	return suma
# Cuando no se usa un print dentro de la función, es necesario crear una variable #
num_1 = 5 ; num_2 = 3
resultado = sumar(num_1,num_2)
print(resultado)
############################

# Paso de valor por referencia #

colores = ['rojo','verde','azul']

def incluir_color(colores,color):
	colores.append(color)

color = input('¿Que color deseas agregar?\n')

incluir_color(colores,color)
print(colores)