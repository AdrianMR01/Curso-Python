# Condiciones #
# Verifican si una condición/expresion es cierta o no #
a = 8
b = 4
c = 2
d = 6
#---------------- if ----------------#
# Indica que si tal condición se cumple, hacer cierta acción #
if a > b:
	print(f'{a} es mayor que {b}')
# Se mostrara lo siguiente solo si la condición se cumple #
# Se pueden incluir dos o mas condiciones dentro de un if #
if (a > c) and (b < d):
	print('La expresión es correcta')
# Para estos casos se tienen que cumplir todas las condiciones para...
# que se pueda ejecutar la siguiente acción #
#-----------------------------------#

#------------------ else ------------------#
# En caso de que np se cumpla la condición el if pasa al else #
if (a > c) and (b > d):
	print('La expresión es correcta')
else: 
	print('La expresión no es correcta')
#-----------------------------------------#

#------------------ elif ------------------#
# Es para incluir mas condiciones dentro de una sentencia #
# En caso de que no se cumpla alguna condición, verificara cual es la que si se cumple #
a = int(input('Introduce un número: '))
b = int(input('Introduce otro número: '))
if (a > b):
	print(f'{a} es mayor que {b}')
elif (a == b):
	print(f'{a} es igual a {b}')
else:
	print('Ninguna expresión es correcta')
#--------------------------------------------#