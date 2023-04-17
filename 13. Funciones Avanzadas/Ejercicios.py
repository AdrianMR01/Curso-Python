# Imprimir numeros primos menores que 50 #

# Función para verificar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

# Generar lista de números primos en un rango
primos = []
numeros = []
for numero in range(1, 101):
    if es_primo(numero):
        primos.append(numero)

def prim (max):
    for num in range(max):
        if num in primos:
            yield num
        if num > 100:
            break
val = 50

for num in prim(val):
    numeros.append(num)

print(f'Valores: {primos}\nValores menores a 50: {numeros}\n')

#----------------------------------------#

# Filtro de numeros pares #
numeros = list(range(1,11))

result = list(filter(lambda numero: numero % 2 == 0,numeros))

print(f'Lista original: {numeros}\nLista filtrada: {result}\n')
#-------------------------#

# Mapeo de numeros incrementando en 10 unidades #
result = list(map(lambda numero: numero + 10, numeros))

print(f'Lista mapeada: {result}')
#---------------------------------#