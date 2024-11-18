contador = 0
logico = True
while logico:
    numero = int(input("Ingrese un numero menor o igual a 50 para cerrar:\n"))
    if numero > 50:
        contador +=1
    else:
        logico = False


print(f"Numero ingresados mayores que 50 son: {contador}")