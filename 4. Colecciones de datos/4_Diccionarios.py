# Diccionarios #
# Son colecciones de elementos que estan indexados, desordenados y se pueden modificar #
# Estos son entre llaves y tienen ares de elementos clave:valor #
diccionario_colores = {'rojo':'red','azul':'blue','amarillo':'yellow'}; print(diccionario_colores)

#- Muestra el valor que esta anclado a la clave -#
print(diccionario_colores['rojo'])
#------------------------------------------------#

# Estos pueden ser guardados dentro de variables #
valor = diccionario_colores['azul'] ; print(valor)
##################################################

#- Añadir elementos -#
'diccionario["clave"] = "valor"'
diccionario_colores['negro'] = 'black' ; print(diccionario_colores)
#------------------------------------------------------------------#

#- Borrar valor -#
'diccionario.pop("clave")'
diccionario_colores.pop('azul'); print(diccionario_colores)

'del(diccionario["clave"])'
del(diccionario_colores['negro']); print(diccionario_colores)
#----------------------------------------------------------#

# Solo imprime clave #
for color in diccionario_colores:
	print(color)

# 
for clave,valor in diccionario_colores.items():
	print(clave,valor)