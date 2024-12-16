suma_notas = 0
nota_maxima = None
nota_minina = None

#Se debe ingresar 3 notas
for i in range(1,4):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {i}: "))
            if nota < 0 or nota >20:
                raise ValueError ("Ingrese la nota entre 0 y 20")
            suma_notas = suma_notas + nota
            if nota_maxima is None or nota > nota_maxima:
                nota_maxima = nota
            if nota_minina is None or nota < nota_minina:
                nota_minina = nota
                
            break
        except ValueError as e:
            print(f"¡ERROR!..{e}. Intente nuevamente")

promedio = suma_notas / 3
print(f"El promedio es: {promedio:.2f}")
print(f"La nota maxima es: {nota_maxima:.2f}")
print(f"La nota mínima es: {nota_minina:.2f}")