# Este programa llama al modulo 'Modulo.py' #
# en caso de que el nombre del modulo sea muy largo, se le puede cambiar el nombre #

import Modulos as md # despues del import tiene que ir el nombre del modulo tal cual se guardo #

md.saludar('Adrian') # Para ocupar las funciones de un modulo hay que...
# llamar al modulo + .funcion que se ocupara(parametros de dicha función) #
md.despedirse('Adrian')

nombre = 'Abigail'
md.saludar(nombre)
md.despedirse(nombre)