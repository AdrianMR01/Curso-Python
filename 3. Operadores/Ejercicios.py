############### Ejercicio 1 ###############
## Crear una variable 'nota_1' que tenga el valor de 6 ##
nota_1 = 6
## Crear otra variable 'nota_2' que tenga el valor de 4 ##
nota_2 = 4
## Crear otra variable 'nota_3' que tenga el valor de 7 ##
nota_3 = 7
## Crear otra variable 'nota_media' que tenga el valor medio de las 3 notas anteriores ##
nota_media = (nota_1 + nota_2 + nota_3)/3
## Crear otra variable 'nota_final' que tenga el valor 'aprobado' (mayor o igual a 5)##
if (nota_media >= 5):
	nota_final = 'aprobado'
print(f'El estudiante tiene un promedio de {nota_media:1.1f} por lo tanto esta {nota_final}')
############################################

################### Ejercicio 2 ###################
## Crea una variable 'minimo' con el valor de 20 ##
minimo = 20
## Crea una variable 'maximo' con el valor de 500 ##
maximo = 500
## Recoge un valor del teclado y almacenalo en la variable 'dato' ##
dato = input('Introduce un número: ')
## Convierte la variable 'dato' en un número y almacenalo en la variable 'numero' ##
numero = int(dato)
## Si el 'numero' es menor que el valor 'minimo', mostar el texto 'Valor bajo' ##
if (numero < minimo):
	print('Valor bajo')
## Si el 'numero' es mayor que el valor 'maximo', mostar el texto 'Valor alto' ##
elif (numero > maximo):
	print('Valor alto')
## Si el 'numero' esta entre el valor 'minimo' y el valor 'maximo', mostar el texto 'Valor medio' ##
elif (numero > minimo) and (numero < maximo):
	print('Valor medio')
else:
	print('No se escriibio ningun valor')
##############################################

############################# Ejercicio 3 #############################
## Crear una variable 'numeros' con la lista de los números del 1 al 10 ##
numeros = [1,2,3,4,5,6,7,8,9,10]
## Mostrar el valor de la variable ##
print(numeros)
## Recoge un valor del teclado y almacenalo en la variable 'dato' ##
dato = input('Introduce un número: ')
## Convierte la variable 'dato' en un número y almacenalo en la variable 'numero' ##
numero = int(dato)
## Si el valor de numero esta en la lista, mostrar el mensaje 'Si' ##
if (numero in numeros):
	print(f'El valor {numero} se encuentra en la lista números')
## Si el valor no esta en la lista, mostrar el texto 'No' ##
elif (numero not in numeros):
	print(f'El valor {numero} no se encuentra en la lista números')
######################################################################