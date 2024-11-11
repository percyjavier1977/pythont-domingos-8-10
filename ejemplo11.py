nnotas = int(input("Ingrese el n° de notas que quiere ingersar:\n"))
sumaNotas = 0

for i in range(nnotas):
    nota = float(input(f"Ingrese la nota N° {i+1}\n"))
    sumaNotas = sumaNotas + nota


promedio = sumaNotas / nnotas
print(f"El promedio de las {nnotas} ingresadas es: {promedio:.2f}")

