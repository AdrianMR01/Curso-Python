#- Como el modulo ya cuenta con dos funciones, se puede importar solo la funcion a ocupar -#
# from 'nombre del modulo' import 'nombre de la función' #
from Modulos import despedirse as des

# Como importamos solo la función despedirse, solo hay que poner el nombre de la función...
# y los parametros que se le van a dar #
name = input('Introduce tu nombre\n')
des(name)
