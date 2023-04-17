# Conjuntos #
# Un conjunto es una proyección de elementos que esta desordenada #
# Estos no cuentan con un indice de los elementos #
# Estos van entre llaves {} #
conjunto_colores = {'rojo','verde','azul'}; print(conjunto_colores)

for color in conjunto_colores:
	print(color)

# En este caso nos manda un error #
# print(conjunto_colores[0])
###################################
#- Longitud -#
print(len(conjunto_colores))
#---------------------------#

#- Añadir elementos -#
conjunto_colores.add('gris'); print(conjunto_colores)
#---------------------------#

#- Borrar elementos -#
conjunto_colores.remove('verde'); print(conjunto_colores)
#-------------------------------#