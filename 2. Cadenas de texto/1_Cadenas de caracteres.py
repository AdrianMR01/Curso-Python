# Cadenas de caracteres (Strings)#
#!!!! Esto solo es para consultar un elemento no para modificarlo ¡¡¡¡#

cadena = 'Hola Mundo'
print(cadena)
#########################

# A cada elemento de un string se le asigna un valor
####### Ejemplo #######
'H o l a  M u n d o'
'0 1 2 3 4 5 6 7 8 9'
#######################

################### Obtener un cierto elemento de la cadena ###################
'nombre de la variable[elemento que se requiere]'
print(cadena[7])
# En corchetes va el valor que deseamos obtener en este caso arrojara una 'n' #
# Si se coloca un número negativo, se comienza a contar desde la izquierda #
print(cadena[-1])
###############################################################################

############### Obtener solo ciertos elementos de una cadena ###############
'nombre de la variable[pos_inicial:pos_final]'
# En pos_final no se cuenta como tal esa variable, se cuenta una antes
print(cadena[0:2]) # Solo imprime el elemento 0 y 1
# En caso de no poner nada en pos_final solo se toma el resto de la cadena
print(cadena[3:]) # Imprime del elemento 3 hasta el ultimo
############################################################################

############# Concatenar cadenas #############
cadena_1 = 'Hola'
cadena_2 = 'Mundo'
cadena_3 = ' '
cadena_nueva = cadena_1 + cadena_3 + cadena_2
print(cadena_nueva)
##############################################