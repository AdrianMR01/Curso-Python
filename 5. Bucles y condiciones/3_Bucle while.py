# Bucle while #
# Este nos permite ejecutar un bloque de acciones mientras...
#...que una condición sea cierta #
valor = 1
fin = 10

while valor < fin: # Mientras que valor sea menor que fin...
	print(valor) # Imprime valor
	valor += 1 # A valor sumale 1

# Para detener en una iteración (break) #
while valor < fin:
	print(valor)
	valor += 1
	if valor == 5:
		break
#################################

# Para evitar una iteración (continue) #
while valor < fin:
	valor += 1
	if valor == 5:
		continue # Evita la iteración 5
	print(valor)
#################################