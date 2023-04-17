# Operadores de comparación #
# Estos pueden ser utilizados con cadenas y números #
num_1 = 10
num_2 = 4
cadena_1 = 'Hola'
cadena_2 = 'Hola'
############### == ###############
# Compara si ambos variables son iguales, arrojara un True o un False dependiendo el caso #
print(num_1 == num_2)
print(cadena_1 == cadena_2)
#----------- Ejemplo -----------#
if (cadena_1 == 'Hola'):
	print('El usuario te saluda')
#-------------------------------#
#################################

################## != ##################
# Compara si las variables son distintas, arrojara un True o un False dependiendo el caso #
print(num_1 != num_2)
print(cadena_1 != cadena_2)
#-------------- Ejemplo --------------#
if (num_1 != num_2):
	print('Los números no son iguales')
#-------------------------------------#
#######################################

############ > ############
# Compara si una variable es mayor a otra, arrojara un True o un False dependiendo el caso #
print(num_1 > num_2)
print(cadena_1 > cadena_2)
# En el caso de una cadena de caracteres, lo que se tiene en cuenta es el número de elementos que tiene #
###########################

############ < ############
# Compara si una variable es menor a otra, arrojara un True o un False dependiendo el caso #
print(num_1 < num_2)
print(cadena_1 < cadena_2)
###########################

############ >= ############
# Compara si una variable es mayor o igual a otra, arrojara un True o un False dependiendo el caso #
print(num_1 >= num_2)
print(cadena_1 >= cadena_2)
###########################

############ <= ############
# Compara si una variable es menor o igual a otra, arrojara un True o un False dependiendo el caso #
print(num_1 <= num_2)
print(cadena_1 <= cadena_2)
###########################