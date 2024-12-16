while True: #Bucle se va repetir hasta que el usuario ingrese correctamente el dato
    try:
        nota = float(input("Ingrese una nota de (0-20): "))
        if nota <0 or nota >20:
            raise ValueError("Debe ingresar la nota entre 0 y 20")
        print(f"La nota ingresada es: {nota}")
        if nota > 10:
            print("Nota Aprobada")
        else:
            print("Nota Desaprobada")
        print("Ingreso correctamente la nota")
        break
    except ValueError as e:
        print("¡ERROR!",e)
        print("Por favor, intente nuevamente")