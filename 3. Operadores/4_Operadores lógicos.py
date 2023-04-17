# Operadores lógicos #
num_1 = 10 ; num_2 = 7 ; num_3 = 2 ; num_4 = 9
################### and ###################
# Se usa para hacer dos comparaciones de variables #
'si (condición 1) y (condición 2) son verdaderas\
Arroja un True'
print(num_1 > num_2) ; print(num_3 < num_4)
# Arrojara un True si ambas condiciones de cumplen y en caso de que no, arroja False
print((num_1 > num_2) and (num_3 < num_4))
###########################################

################### or ###################
# Si alguna de las condiciones establecidas es verdadera, arrojara un True #
'si (condición 1) o (condición 2) son verdaderas\
Arroja un True'
print((num_1 > num_2) or (num_3 > num_4))
###########################################

############### not ###############
# Si la condición de adentro es False, arroja un True y si es True, arroja un False #
'not(condicion falsa) = True\
 not(condicion verdadera) = False'
print(not(num_3 > num_4))
###################################