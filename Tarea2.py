import os
os.system("cls")

tabla_inicio = 1
tabla_fin = 12
inicio = 1
fin = 12

for factor1 in range(tabla_inicio, tabla_fin + 1):
	print(f'Tabla de multiplicar del {factor1}:')
	for factor2 in range(inicio, fin + 1):
		print(f'{factor1} x {factor2} = {factor1 * factor2}')