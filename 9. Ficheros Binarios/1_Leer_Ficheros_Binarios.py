import pickle

file = open('Fichero_Colores.pckl','rb')

lista_normal = pickle.load(file)#Devuelve los datos de binario a normal
print(lista_normal)