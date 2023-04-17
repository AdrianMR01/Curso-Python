# Modificar datos de un fichero 

fichero = open("Fichero_Guardado.txt","at") # a significa append(añadir)

cadena_incluir = "\nFila infiltrada en el fichero"

fichero.write(cadena_incluir)
fichero.close()

# La cadena o el texto a incluir siempre se agregara despues de la ultima linea del fichero