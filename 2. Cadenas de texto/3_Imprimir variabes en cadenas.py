# Imprimir variables en cadenas #

name = "Adrian"
print('Buenos dias ' + name)
# Se puede concatenar una cadena de caracteres con una cadena #

######################## .format ########################
# Se agregan llaves en la cadena de caracteres del print, una vez terminada la cadena... 
# ...de agrega .format(nombres de las variables en orden) #
'print("{variable_1} {variable_2}".format(variable_1,variable_2))'
name = 'Abigail'
age = 20
print('{}, {} años'.format(name,age))

## Para resultados númericos ##
# Dentro el format se puede definir una nueva variable para no alterar alguna ya establecida #
resultado = 10/3 
print('El resultado es {r}'.format(r=resultado))
# Para establecer el formato que va a tener el número es {variable abreviada:No de enteros.No de decimales f}#
'{r:1.3f}'
print('El resultado es {r:1.3f}'.format(r=resultado))
#########################################################

################# f-strings #################
name = 'Montse'
age = 25
print(f'Paciente: {name}		Edad: {age}')
# La 'f' antes del texto indica que se le esta dando un formato ... 
# ...en este caso en las llaves se colocan los nombres de las variables #
##############################################

# Entrada por teclado #

############ input() ############
print('Introduce tu nombre')
entrada = input()
print('Hola ' + entrada)
# el input() nos permite introducir cualquier tipo de dato #
#################################