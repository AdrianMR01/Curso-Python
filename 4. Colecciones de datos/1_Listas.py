# Listas #
# Son una proyección de elementos la cual se puede modificar #
colores = ['rojo','amarillo','verde']
# Las listas se enumeran de izquierda a derecha, iniciando por el 0...
#... en este caso nuestra lista es de 0,1,2 #
#- Para modificar algun elemento de la lista -#
'lista[elemento] = valor nuevo '
colores[1] = 'azul'; print(colores)
#---------------------------------------------#

#- Longitud de la lista -#
'len(lista)'; print(len(colores))
#------------------------#

#-------- Añadir elemento --------#
'lista.append("nuevo elemento")'
colores.append('gris'); print(colores)
# El elemento sera añadido al final de la lista #
#--------------------------------#

#---------- Borrar elemento ----------#
'lista.remove("elemento a quitar")'
colores.remove('rojo'); print(colores)
# Una vez que se borre cierto elemento, los que quedan seran recorridos a la izquierda...
#... osea. Lista original: 0,1,2,3 eliminando el elemento 0: 0(1),1(2),2(3) #
## Borrar toda la lista ##
'lista.clear()'
#-------------------------------------#

#------- Insertar elemento -------#
'lista.insert(posicion,elemento)'
colores.insert(0,'rojo'); print(colores)
#---------------------------------#

#- Ordenar una lista -#
# Ordena las listas en orden alfabetico #
'lista.sort()'
colores.sort(); print(colores)
#---------------------#

#--- Invertir ---#
'lista.reverse()'
colores.reverse(); print(colores)
#----------------#