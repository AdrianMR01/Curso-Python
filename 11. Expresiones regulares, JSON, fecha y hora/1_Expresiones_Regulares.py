# Expresiones regulares (search, findall, split, sub)

text = 'Hola mi nombre es Adrian'

import re # Modulo re(Regular Expressions)
#-------------Search-------------#
buscar = re.search('nombre',text)
# re.search('Texto a buscar', variable donde buscar)
print(buscar)
''' 
Si el texto se encuentra en la variable arroja esto
<re.Match object; span=(8, 14), match='nombre'>
'''
if buscar:
	print('Texto encontrado')
else:
	print('No se enctro el texto')

buscar = re.search('Adrian',text)
'''
palabra$ indica si el texto termina con esa palabra
^palabra indica si el texto inicia con esa palabra
palabra1.palabra2 puede haber caracteres en medio
palabra1.*palabra2 hay 0 o más caracteres en medio
'''
print(buscar)
#--------------------------------#
#-------------Findall-------------#
texto_2 = '''
El coche de Luis es rojo,
coche de Antonio blanco
y el coche de Maria es rojo
'''
buscar_2 = re.findall('coche.*rojo',texto_2)
'''
['coche de Luis es rojo', 'coche de Maria es rojo']
'''
print(buscar_2)
#---------------------------------#
#--------------split--------------#
texto_3 = 'la silla es blanca y vale 80'
split = re.split('\s',texto_3)# divide el texto en las palabras que
# lo forman en cada espacio en blanco, devolviendo una lista
# de las palabras que hay en el texto
'''
\s espacio en blanco
'''
print(split)
'''
['la', 'silla', 'es', 'blanca', 'y', 'vale', '80']
'''
#---------------------------------#
#---------------sub---------------#
'''
Sustituye todas las coincidencias de una cadena
'''
sub = re.sub('silla','mesa',texto_3)
'''
re.sub('palabra a buscar','cambio',variable)
'''
print(sub)
#---------------------------------#