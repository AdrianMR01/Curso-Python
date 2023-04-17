import Ficheros as fch

texto = ''

nombre_fichero = 'Fichero Ejercicio.txt'

fichero = fch.Fichero(nombre_fichero)

fichero.grabar_fichero(texto)

fichero.incluir_fichero(texto)

leer_fichero = fichero.leer_fichero()
print('\n'+leer_fichero)