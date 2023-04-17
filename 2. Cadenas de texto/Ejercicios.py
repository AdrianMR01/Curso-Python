############# Ejercicio 1 #############
# Crear una variable llamada 'cadena' que contiene el texto 'Esto es un texto de ejemplo'...
#...Segun la posición de cada letra en la cadena, calcular los valores (x,y) paraseleccionar solo...
#... la cadena 'texto' #
cadena = 'Esto es un texto de ejemplo'
print(cadena[11:16])
######################################

######################### Ejercicio 2 #########################
# 1. Crear una variable 'cadena' que contiene el texto 'Esto es un texto de ejemplo' #
cadena = 'Esto es un texto de ejemplo'
print(cadena)
# 2. Crear una variable 'longitud' que contiene la longitud de la variable 'cadena' #
longitud = len(cadena)
print(longitud)
# 3. Crear una variable 'strlongitud' que tenca el valor de 'longitud' pero...
# ... convertida a string #
strlongitud = str(longitud)
print(strlongitud)
# 4. Crear una variable 'mayusculas' que contiene la variable cadena en mayusculas #
mayusculas = cadena.upper()
print(mayusculas)
# 5. Crear una variable 'resultado' que concatene 'mayusculas'...
# ... con el texto ' tiene longitud de ' y strlongitud #
resultado = mayusculas + ' tiene longitud de: ' + strlongitud
print(resultado)
##############################################################

###################### Ejercicio 3 ######################
# 1. Crear la variable "num_1" con el valor 5 #
num_1 = 5
# 2. Crear la variable "num_2" con el valor 8 #
num_2 = 8
# 3. Crear la variable "suma" con el valor de la suma de num_1 y num_2 #
suma = num_1 + num_2
# 4. Imprimir por pantalla el resultado, utilizando la función 'print' #
print(f'El resultado de {num_1} más {num_2} es: {suma}')
#########################################################

############### Ejercicio 4 ###############
# 1. Imprime el texto 'Introduce el primer número' #
print('Introduce el primer numero')
# 2. Crea la variable 'dato_1' con el primer valor introducido en el paso anterior #
dato_1 = input()
# 3. Imprime el texto 'Introduce el segundo número' #
print('Introduce el segundo numero')
# 4. Crea la variable 'dato_2' con el primer valor introducido en el paso anterior #
dato_2 = input()
# 5. Convertir la variable 'dato_1' en una variable númerica llamada 'num_1' #
num_1 = int(dato_1)
# 6. Convertir la variable 'dato_2' en una variable númerica llamada 'num_2' #
num_2 = int(dato_2)
# 7. Crea la variable 'suma' con la súma de 'num_1' y 'num_2' #
suma = num_1 + num_2
# 8. Convertir la variable suma en una variable de texto denominada 'strsuma' #
str_suma = str(suma)
# 9. Crear la variable 'resultado' con la concatenación de 'La suma ' y 'strsuma' #
resultado = 'La suma es: ' + str_suma
# 10. Imprimir el valor de 'resultado' #
print(resultado)
##########################################