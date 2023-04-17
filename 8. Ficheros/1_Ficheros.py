# Leer el fichero de texto #
fichero = open('2_pip.txt','rt') # r es read - modo lectura
# t es texto - fichero de caracteres

dato = fichero.read()

print(dato)