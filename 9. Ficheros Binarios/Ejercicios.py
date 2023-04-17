import pickle
# Crear el diccionario frutas
frutas = {}
valores = int(input('Valores a agregar: '))

for fruta in range(valores):
	valor = input('\nIngresa la fruta en español: ')
	clave = input('Ingresa la fruta en ingles: ')
	frutas[valor]=clave

print(frutas)
frutas.values()
# grabar frutas en fichero binario.pckl
file = open('Fichero_Frutas.pckl','wb')
pickle.dump(frutas,file)
file.close()

file_2 = open('Fichero_Frutas.pckl','rb')

print(pickle.load(file_2))