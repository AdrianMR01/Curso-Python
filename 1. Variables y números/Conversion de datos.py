# Conversion de datos #
## int -> str ##
num = 5
cadena = str(num)
# str(nombre de la variable) convierte la variable a tipo string
print(num, type(num))
print(cadena, type(cadena)) 
########################

## str -> int ##
string = '25'
num_int = int(string)
# int(Nombre de la variable) convierte la variable en tipo entero
print(string, type(string))
print(num_int, type(num_int))
########################

## str -> float ##
string = '25.7'
num_float = float(string)
# int(Nombre de la variable) convierte la variable en tipo entero
print(string, type(string))
print(num_float, type(num_float))
########################

## Ejercicio ##
# Se hace la suma de 2 variables (num y number) #
new_num_int = num + num_int
print(new_num_int)

new_num_float = num + num_float
print(new_num_float)