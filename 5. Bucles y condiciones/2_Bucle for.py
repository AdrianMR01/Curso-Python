# Bucle for #
# Es utilizado para iterar en una secuencia de elementos...
#  los elementos seran mostrados por linea # 

# Despues del for puede ir el nombre que nosotros queramos...
# asignarle a los elementos de una lista #

#------------ listas ------------#
colores = ['rojo','verde','azul']

# Esto es lo mismo que...
# for col in colores: 
# 	print (col) 

# Esto #
for color in colores: # <- Por cada color en la lista colores #
	print (color) # imprime color #
#--------------------------------#

#------- Cadenas -------#
cadena = 'Hola Mundo'

for caracter in cadena:
	print (caracter)
#-----------------------#

#---- Rango de valores ----#
# Cuando usamos la función range, esta hace...
# una numeración iniciando desde el 0, por lo tanto si ponemos un 4
# sera 0,1,2,3 y ahi son 4 elementos #

# Si a la función range solamente le agregamos un número...
# hara el conteo hasta ese límite #
'range(4)' # Contara del 0 al 3 #
for numero in range(8): 
	print(numero)

# Si se le agregamos otro numero, el conteo empezara desde el primer valor...
# que le asignamos pero sin modificar la lista original #
# Ejemplo #
'range(1,8)'
# La lista original es del 0 al 7 #
# Y en este caso, indicamos que el conteo comienza desde el 1 hasta el 7 #
for numero in range(1,8): 
	print(numero)

# Si le agregamos otro valor al final, en este indicamos el paso/avance... 
# por elemento que tendra esta numeración, iniciando desde el primer elemento...

# Ejemplo #
'range(1,8,2)'
# La lista va 1,2,3,4,5,6,7 y si lleva un paso de dos entonces...
# muestra 1,3,5,7, si fuera de tres seria 1,4,7 y asi sucesivamente #
for numero in range(1,8,2): 
	print(numero)
#------------------------#

#------------- break -------------#
# Es para arar un bucle #
for numero in range(10):# Por cada número en un rango de 0 a 9 #
	if numero == 5: # Si el numero es igual a 5 #
		break # Para el bucle #
	print(numero) # Si no es el numero 5 sigue el bucle#
#--------------------------------#

#----------- continue -----------#
# Para solo una iteración siendo esta la actual #
for numero in range(10):# Por cada número en un rango de 0 a 9 #
	if numero == 6: # Si el numero es igual a 6 #
		continue # emite la teración 6 #
	print(numero) # Si no es el numero 5 sigue el bucle#
#--------------------------------#
#- Doble for -#
for numero1 in range(4):
	for numero2 in range(3):
		print(numero1,numero2)
# Por cada elemento del primer rango, mostrar...
# los elementos del segundo rango #