import pickle

lista = ['azul','rojo','verde','amarillo']

file = open('Fichero_Colores.pckl','wb') # b cuando se trata de archivo binario

# pickle.dump("nombre de la lista","en donde lo va a guardar") 
pickle.dump(lista,file)

file.close()