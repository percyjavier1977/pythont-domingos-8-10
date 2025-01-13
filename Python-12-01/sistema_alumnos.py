import time
estudiantes = []
print("===MANTENIMIENTO DE ESTUDIANTES===")
while True:
    print("Opciones del sistema")
    print("1. Añadir estudiante")
    print("2. Mostrar estuantes")
    print("3. Buscar estudiante")
    print("4. Eliminar estudiante")
    print("5. Ordenar estudiantes")
    print("6. Mostrar el total de estudiantes")
    print("7. Salir")
    try:
        opcion = int(input("Seleccione una opción (1-7): "))

        if opcion == 1:
            nombre = input("Ingrese el nombre del estufiante: ")
            estudiantes.append(nombre)
            print(f"El estudiante {nombre} se agrego correctamente")
            time.sleep(2)
        elif opcion == 2:
            print("==Lista de estudiantes==")
            for estudiante in estudiantes:
                print(f"- {estudiante}")
            time.sleep(2)
        elif opcion == 3:
            nombre = input("Ingrese el nombre a buscar: ")
            if nombre in estudiantes:
                print(f"El estudiante {nombre} si esta en la lista")
            else:
                print(f"El estudiante {nombre} no esta en la lista")
            time.sleep(2)
        elif opcion == 4:
            nombre = input("Ingrese el nombre a buscar: ")
            if nombre in estudiantes:
                estudiantes.remove(nombre)
            else:
                print(f"El estudiante {nombre} no esta en la lista")
            time.sleep(2)
        elif opcion == 5:
            estudiantes.sort()
            print("==Lista de estudiantes==")
            for estudiante in estudiantes:
                print(f"- {estudiante}")
            print("La lista ha sido ordenada")
            time.sleep(2)
        elif opcion == 6:
            print(f"Total de estudiantes: {len(estudiantes)}")
            time.sleep(2)
        elif opcion == 7:
            print("Saliendo del sistema")
            break
        else:
            print("Opcion invalidad. Por favor seleccione una opción del (1-7)")
            time.sleep(3)
    except ValueError:
        print("¡ERROR!..Entrada invalidad, ingres solo numeros del 1-7")
        time.sleep(2)
