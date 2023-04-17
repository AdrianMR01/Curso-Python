# Existen diversos tipos de bloques para verificar
# los errores en un codigo
# try ··· except ··· else ··· finally 
'''
num_1 = 5;num_2 = 0 
div = num_1/num_2

ZeroDivisionError: division by zero

# Para evitar este error se usa el comando try
'''
#------Bloque try------#
try: 
	# Prueba las instrucciones
	# si se pueden realizar proceden las instrucciones
	num1 = 5
	num2 = 0
	div = num1/num2
	print(div)
#------Bloque except---#
except ZeroDivisionError:# Si el error es este
	print('Error, division entre cero')
except: 
	# Si encuentras otro error
	print('Error')
#------Bloque else------#
else: # Si todo funciona bien
	print('No hay error')

#------Bloque finally------#
'''Permite ejecutar el codigo
independientemente de try o except'''
try: 
	# Prueba las instrucciones
	# si se pueden realizar proceden las instrucciones
	num1 = 5
	num2 = 3
	div = num1/num2
	print(div)
#------Bloque except---#
except ZeroDivisionError:# Si el error es este
	print('Error, division entre cero')
except: 
	# Si encuentras otro error
	print('Error')
#------Bloque else------#
else: # Si todo funciona bien
	print('No hay error')
finally:
	print('Esta prueba del try se ha acabado')
