import math
def calcular_area_circulo():
    while True:
        try:
            radio = float(input("Ingre el radio del círculo: "))
            if radio < 0:
                print("El radio no puede ser negativo. Intentelo nuevamente")
            else:
                return math.pi * radio ** 2
        except ValueError:
            print("Entrada invalida. Ingrese nuevamente el número")


def calcular_area_rectangulo():
    while True:
        try:
            base = float(input("Ingrese la base del rectangulo: "))
            altura = float(input("Ingrese la altura del rectangulo: "))
            if base <0 or altura <0:
                print("La base y altura no pueden ser negativos. Intente nuevamente")
            else:
                return base * altura
        except ValueError:
            print("Entrada invalida. Ingrese nuevamente los números")

def calcular_area_cuadrado():
    while True:
        try:
            lado = float(input("Ingrese el lado del cuadrado: "))
            if lado <0:
                print("El lado no puede ser negativo. Intente nuevamente")
            else:
                return lado**2
        except ValueError:
             print("Entrada invalida. Ingrese nuevamente el número")


def calcular_area_triangulo():
    while True:
        try:
            base = float(input("Ingrese la base del triangulo: "))
            altura = float(input("Ingrese la altura del triangulo: "))
            if base <0 or altura <0:
                print("la base y la altura no pueden ser negativos. Intente nuevamente")
            else:
                return (base*altura)/2
        except ValueError:
             print("Entrada invalida. Ingrese nuevamente los números")
             

def sistema_de_calculo():
    while True:
        print("\n======SISTEMA DE CLACULO======")
        print("1. Círculo")
        print("2. Rectángulo")
        print("3. Cuadrado")
        print("4. Triángulo")
        print("5. Salir")
        
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
            if opcion == 1:
                area = calcular_area_circulo()
                print(f"El área del círculo es: {area:.2f}")
            elif opcion == 2:
                area = calcular_area_rectangulo()
                print(f"El área del rectángulo es: {area:.2f}")
            elif opcion == 3:
                area = calcular_area_cuadrado()
                print(f"El área del cuadrado es: {area:.2f}")
            elif opcion == 4:
                area = calcular_area_triangulo()
                print(f"El área del triángulo es: {area:.2f}")
            elif opcion == 5:
                print("¡Gracias por usar el sistema!")
                break
            else:
                print("Opción no válida. Por favor ingrese un número entre 1 y 5")
        except ValueError:
            print("Entrada invalidad por favor ingrese un número entre 1 y 5")
        
        
sistema_de_calculo()
