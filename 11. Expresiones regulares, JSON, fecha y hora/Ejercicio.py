import re
'''
Crear una función que busque palabras en un texto
e indique la posición de las mismas
'''
def buscar(word_search,text):
	search = re.search(word_search,text)
	return search

text = input('Ingresa un texto: ')
word_search = input('Palabra a buscar: ')
search = buscar(word_search,text)

if search:
	start = search.start()
	end = search.end()
	print(f'''\nLa palabra: {word_search} 
Se encuentra en el texto: {text}
En la posición de {start} a {end}''')

else:
	print(f'''\nLa palabra: {word_search} 
No se encuentra en el texto: {text}''')