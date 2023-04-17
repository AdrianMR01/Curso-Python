# Ejercicio 1 #

# Dada la siguiente lista = [1,2,5,25,33,56,75,21,56,89,43,13,62,24]...
# mostrar mediante el metodo 'print' y el operador 'in', si el número 21 esta en la lista #

lista = [1,2,5,25,33,56,75,21,56,89,43,13,62,24]
numero = int(input('¿Que valor necesitas?\n'))

if numero in lista:
	print(f'El numero {numero} si esta en la lista')
else:
	print(f'El numero {numero} no esta en la lista')
#####################################################

# Ejercicio 2 #
#1. Crear una variable 'tupla' que sea una tupla de los siguientes nombres...
# Antonio, Pedro y Maria #
tupla = ('Antonio','Pedro','Maria')
#2. Mostrar el valor de la variable 'tupla' #
print(tupla)
#3. Recoger un dato por teclado y almacenarlo en la variable dato #
dato = input('¿Que nombre deseas buscar?\n')
#4. Si el valor 'dato' está dentro de los valores de la variable 'tupla', mostrar 'si' #
if dato in tupla:
	print(f'El nombre {dato} si se encuentra en la lista')
#5. Si el valor 'dato' no está dentro de los valores de la variable 'tupla', mostrar 'no' #
elif dato not in tupla:
	print(f'El nombre {dato} no se encuentra en la lista')
###############################################################

# Ejercicio 3 #
#1. Crear una variable 'conjunto' que sea un conjunto de los valores 1,2,3,4 y 5#
conjunto = {1,2,3,4,5}
#2. Mostrar el valor de la variable conjunto #
print(conjunto)
#3. Añadir los números 6,7,8 y 9 a la variable #
conjunto.add(6);conjunto.add(7);conjunto.add(8);conjunto.add(9)
#4. Mostrar ahora el valor de la variable conjunto #
print(conjunto)
#5. Eliminar el número 9 de la variable #
conjunto.remove(9)
#6. Mostrar el valor de la variable #
print(conjunto)
#7. Verificar de que tipo de dato es la variable mediante type() # 
print(type(conjunto))
######################

# Ejercicio 4 #
#1. Crea una variable 'diccionario' con los pares de valores siguientes 
# ... uno:one,dos:two,tres:three#
diccionario = {'uno':'one','dos':'two','tres':'three'}
#2. Mostrar por pantalla el valor de la variable#
print(diccionario)
#3. Añadir un nuevo elemento cuatro:four#
diccionario['cuatro'] = 'four'
#4. Mostrar ahora el valor del diccionario#
print(diccionario)
#5. Recoger un valor introducido por teclado y almacenarlo en 'dato' #
dato = input()
#6. Utilizar 'dato como clave del diccionario para recuperar su valor #
valor = diccionario[dato]
print(valor)