# Grabar fichero de texto

fichero = open('Fichero_Grabado.txt','wt')#w es write - modo escritura

texto_del_fichero = """Se grabará en este fichero de texto lo que se está dictando por medio
del micrófono de Windows Para posteriormente realizar su lectura haciendo
uso de lenguaje python con el comando right"""

#nombre del fichero.write(texto a escribir)
#.write() sirve para escribir algo en el fichero creado
fichero.write(texto_del_fichero) 

fichero.close()