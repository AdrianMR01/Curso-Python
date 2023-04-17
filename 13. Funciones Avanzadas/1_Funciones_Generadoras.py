'''
Las funciones generadoras son aquellas que generan valores sobre la marcha 
'''
def pares (max):
	for num in range(max):
		if (num % 2 == 0):
			yield num

val = 100

for num in pares(val):
	print(num)

# Funcion filter #
'''
Filtro de datos a partir de una función condicional en una lista 
'''
import random

numeros = []

for i in range(10):
    numero = random.randint(-100, 100)
    numeros.append(numero)


def positivo(number):
	if number > 0:
		return True
	else:
		return False

result = list(filter(positivo,numeros))

print(f'Lista original: {numeros}\nLista filtrada: {result}\n')
#----------------#

# Funcion map #
factor_2 = int(input('Introduce el factor 2 de la multiplicacion: '))

def multiplicar(numero):
	mult = numero * factor_2
	return mult

result = list(map(multiplicar, numeros))

lam = list(map(lambda numero: numero * factor_2, numeros))

print(f'Lista mapeada: {lam}')


#-------------#