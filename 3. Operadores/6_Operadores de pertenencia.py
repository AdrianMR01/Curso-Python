# Operadores de pertenencia #
# Estos permiten verificar si un elemento/objeto esta o no dentro de una lista de valores #
frutas_1 = ['manzana','pera','mango']
frutas_2 = 'pera'
frutas_3 = 'uva'
########################### in ###########################
# Esto se puede ocupar cuando la lista sea muy grande #
print(frutas_2 in frutas_1) ;'¿frutas_2 esta en frutas_1?'
# La respuesta sera True o False dependiendo el caso #
# En este caso arroja True #
##########################################################

############################# not in #############################
print(frutas_2 not in frutas_1) ;'¿frutas_2 no esta en frutas_1?'
# La respuesta sera True o False dependiendo el caso #
# En este caso arroja False #
print(frutas_3 not in frutas_1) ;'¿frutas_3 no esta en frutas_1?'
# En este caso arroja True #
#################################################################