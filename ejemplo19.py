contador = 0
while True:
    contraseña  = input("Ingrese la contraseña: ").lower()
    contador +=1
    if contraseña =="1234peru":
        print("Ingresando al sistema:")
        break #cerrar el bucle
        
    else:
        print("Contraseña incorrecta")
        
print(f"Número de intentos {contador}")