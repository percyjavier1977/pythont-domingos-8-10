#datos simulados del cajero
pin_correcto = "1234"
saldo = 5800
intentos = 3
#verificar el PIN
while intentos > 0:
    pin_ingresado = input("Por favor ingrese su PIN: ")
    if pin_ingresado == pin_correcto:
        print("PIN correto. Bienvenido al cajero")
        break
    else:
        intentos -=1
        print(f"PIN Incorrecto. te quedan {intentos}")


if intentos == 0:
    print("Has agotado todos los intenetos. ¡TARJETA BLOQUEDA!")
else:
    #Menú de opciones
    while True:
        print("-----MENÚ DEL CAJERO-----")
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ")
        if opcion == "1":
            print(f"Tu saldo actual es: {saldo}")
        elif opcion == "2":
            monto = float(input("Ingrese el monto a retirar: "))
            if monto <= saldo:
                saldo -= monto
                print(f"Has retirado {monto:.2f}. Tu nuevo saldo es: S/{saldo:.2f}")
            else:
                print("Fondos insufucientes")
        elif opcion == "3":
            print("GRACIAS.. por usar el cajero automatico")
            break
        else:
            print("Opcion no valida. Intente de nuevo")
            
