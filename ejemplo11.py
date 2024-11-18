nnotas = int(input("Ingrese el n° de notas que quiere ingersar:\n"))
sumaNotas = 0
notaMaxima = float('-inf') #Iniicar con un valor bajo
notaMinima = float('inf')#Iniciar con un valor muy alto

for i in range(nnotas):
    nota = float(input(f"Ingrese la nota N° {i+1}\n"))
    sumaNotas = sumaNotas + nota
    if nota > notaMaxima:
        notaMaxima = nota
    if nota < notaMinima:
        notaMinima = nota
        
promedio = sumaNotas / nnotas
print(f"El promedio de las {nnotas} ingresadas es: {promedio:.2f}")
print(f"La nota máxima es: {notaMaxima:.2f}")
print(f"La nota mínima es: {notaMinima:.2f}")
