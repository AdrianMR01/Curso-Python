'''Crear una funcion que reciba 3 números
el pirmero lo divida entre la resta de los
dos restantes'''
def operacion(num1,num2,num3):
	val = num1/(num2-num3)
	return val

num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))

'''Utilizar bloques de error para solventar
problemas y/o errores'''
try:
	val = operacion(num1,num2,num3)
	print(val)
except ZeroDivisionError:
	print(f'Número 2 ({num2}) y número 3 ({num3}) deben ser distintos')
