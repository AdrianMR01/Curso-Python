# Operadores de identidad #
# Permite identificar si dos objetos son el mismo objeto o son distintos #
frutas_1 = ['manzana','pera']
frutas_2 = ['manzana','pera']
frutas_3 = frutas_1

########################################## is ##########################################
# Establece que si un objeto es lo mismo que otro #
'Frutas_3 es el mismo objeto que frutas_1'
'objeto_1 es igual a objeto_2'
print(frutas_3 is frutas_1)
# Si agregamos a frutas_3 otro elemento, automaticamente, se modifica frutas_1...
#... esto por que establecimos que frutas_3 = frutas_1
frutas_3.append('mango')
print(f'La lista de frutas 1 tiene: {frutas_1}\nLa lista de frutas 3 tiene: {frutas_3}')
########################################################################################

############ is not ############
# Establece que si un objeto no es lo mismo que otro #
'frutas_3 no es el mismo objeto que frutas_1'
print(frutas_3 is not frutas_1)
# Como frutas_3 y frutas_1 es lo mismo, esto arrojara un False #
###############################