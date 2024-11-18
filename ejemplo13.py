import random
numero_adivinar = random.randint(1,10)
intentos_max = 3
for intento in range(1,intentos_max+1):
    numero_ingresado = int(input(f"Intento N° {intento}: Ingrese un número entre 1 y 10:\n"))
    if numero_ingresado == numero_adivinar:
        print("¡felicidades adivinaste el número!")
        break
    if intento < intentos_max:
        if numero_ingresado < numero_adivinar:
            print("El número que quiere adivinar es mayor que el ingresado")
        else:
            print("El número que quiere adivinar es menor que el ingresado")
    

else:
    print("¡Lo siento no adivinaste el número ")
    print(f"Elnúmero era {numero_adivinar}")   

  
    