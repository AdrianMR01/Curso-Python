# Funciones de cadenas #
cadena = 'Hola Mundo'
# Longitud de una cadena cadena #
'len(nombre de la cadena)'
print(len(cadena))
#################################

############################ .upper() ############################
'nombre de la cadena.upper()'
print(cadena.upper())
# Solo muestra la cadena en mayusculas pero no cambia la variable #
# Para cambiar la variable por completo es de la siguiente manera #
cadena = cadena.upper()
##################################################################

############################# .lower() #############################
'nombre de la cadena.lower()'
print(cadena.lower())
# Solo muestra la cadena en minusculas pero no cambia la variable #
# cadena = cadena.lower()
###################################################################

######################## .split() ########################
# Hace una lista con las palabras que contiene la cadena#
'nombre de la cadena.split()'
cadena_2 = 'uva_pera_manzana_mango'
print(cadena_2.split('_'))
# split(',') indica que en la cadena de texto cada que haya una ',' es otra palabra #
# La ',' puede ser tambien ':','.',';','-','_',etc...#
##########################################################

#### list(cadena) ####
# Crea una lista de todos los caracteres que tiene una cadena #
lista = list(cadena)
print(lista)
#####################