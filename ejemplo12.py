for i in range(1,4):
    c = 12345
    contra = int(input("Ingrese su contraseña:\n"))
    if contra == c:
        print("Contraseña conrrecta...Ingresando al sistema")
        break
    else:
        print("Contraseña incorrecta")
    
if i == 3:
    print("¡Tarjeta Bloqueda!")
    