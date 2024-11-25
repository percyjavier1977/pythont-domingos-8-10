try:
    numero = float(input("Ingrese un número: "))
    divisor = float(input("Ingrese el divisor: "))
    divi = numero / divisor
except ZeroDivisionError:
    print("No se puede dividir un número entre cero")
else:
    print("Se calculo correctamente")
finally:
    print("Fin de la aplicación")
