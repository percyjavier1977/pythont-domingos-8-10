def ingresar_nota(numero):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {numero} (0 a 20): "))
            if 0 <= nota <= 20:
                return nota
            else:
                print("La nota debe estar entre 0 y 20. Intenete nuevamente")
        except ValueError:
            print("Entrada invalida. Por favor ingrese un número ")
            


def calcular_promedio(nota1,nota2,nota3,nota4):
    return (nota1+nota2+nota3+nota4)/4

def mostrar_resultado(promedio):
    print(f"El promedio calculado es: {promedio:.2f}")
    if promedio >10:
        print("¡Aprobado! :)")
    else:
        print("Desaprobado :(")

def sistema_de_notas():
    print("=======SISTEMA DE NOTAS======")
    nota1 = ingresar_nota(1)
    nota2 = ingresar_nota(2)
    nota3 = ingresar_nota(3)
    nota4 = ingresar_nota(4)
    promedio = calcular_promedio(nota1,nota2,nota3,nota4)
    mostrar_resultado(promedio)
    
sistema_de_notas()