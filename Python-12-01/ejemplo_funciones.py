import time
from funciones import(
    mostrar_menu,
    agregar_estudiante,
    mostrar_estudiantes,
    buscar_estudiante,
    eliminar_estudiante,
    ordenar_estudiantes,
    mostrar_total_estudiantes,
    
)

print("===MANTENIMIENTO DE ESTUDIANTES===")
while True:
    mostrar_menu()
    opcion = int(input("Selecione una opción del (1-7): "))
    if opcion == 1:
        agregar_estudiante()
    elif opcion == 2:
        mostrar_estudiantes()
    elif opcion == 3:
        buscar_estudiante()
    elif opcion == 4:
        eliminar_estudiante()
    elif opcion == 5:
        ordenar_estudiantes()
    elif opcion == 6:
        mostrar_total_estudiantes()
    elif opcion == 7:
        print("Saliendo del sistema")
        break
    else:
        print("Opcion invalidad. Por favor seleccione una opción del (1-7)")
        time.sleep(3)

