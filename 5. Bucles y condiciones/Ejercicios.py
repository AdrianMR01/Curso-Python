# Ejercicio 1 #
#  Crea un diccionario con los siguientes pares de valores...
# {manzana:apple,naranja:orange,plantano:banana,limon:lemon} #
frutas = {'manzana':'apple','naranja':'orange','plantano':'banana','limon':'lemon'}
# Muestra la traducción de la palabra 'naranja' #
print(frutas['naranja'])
# Añade un nuevo elemento 'piña' y 'pineapple' #
frutas['piña'] = 'pineapple'
# Haz un bucle para mostrar todos los elementos del diccionario #
for esp,ing in frutas.items():
	print(f'{esp} se traduce al inglés como {ing}')
#################################################################

# Ejercicio 2 #
# Crear una variable 'nota' con el valor de 4.5 # 
nota = 4.5
# Crear una variable 'trabajo_realizado' con valor 'si'#
trabajo_realizado = 'si'
# Calcular el valor de la variable 'nota_final', teniendo en cuenta que,...
# si la nota_final es mayor o igual a 4 y el valor de la variable trabajo_final...
if (nota >= 4) and (trabajo_realizado == 'si'):
# es 'si', nota_final es 'aprovado' y en caso contrario sera 'suspendido' #
	nota_final = 'aprovado'
else:
	nota_final = 'suspendido'

print(nota_final)
###############################################

# Ejercicio 3 #
# Crear una variable 'inicio' con el valor de 1 #
inicio = 1
# Crear una variable 'fin' con el valor de 6 #
fin = 6
# Hacer un bucle while que muestre tantas filas...
# como valores haya entre 'inicio' y 'fin'#
while(inicio < fin):
# En cada iteración del bucle mostrar el texto 'esta es la fila' + num de fila #
	print(f'Esta es la fila {inicio}')
	inicio += 1
################################################
i = 0
while(i < 3):
	i += 1
	calificacion = int(input(f'Introduce tu calificación {i}'))
