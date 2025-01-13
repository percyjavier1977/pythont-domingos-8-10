
import time
estudiantes = []


def mostrar_menu():
    print("Opciones del sistema")
    print("1. Añadir estudiante")
    print("2. Mostrar estuantes")
    print("3. Buscar estudiante")
    print("4. Eliminar estudiante")
    print("5. Ordenar estudiantes")
    print("6. Mostrar el total de estudiantes")
    print("7. Salir")

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estufiante: ")
    estudiantes.append(nombre)
    print(f"El estudiante {nombre} se agrego correctamente")
    time.sleep(2)

def mostrar_estudiantes():
    print("==Lista de estudiantes==")
    for estudiante in estudiantes:
        print(f"- {estudiante}")
    time.sleep(2)

def buscar_estudiante():
    nombre = input("Ingrese el nombre a buscar: ")
    if nombre in estudiantes:
        print(f"El estudiante {nombre} si esta en la lista")
    else:
        print(f"El estudiante {nombre} no esta en la lista")
    time.sleep(2)

def eliminar_estudiante():
    nombre = input("Ingrese el nombre a buscar: ")
    if nombre in estudiantes:
        estudiantes.remove(nombre)
    else:
        print(f"El estudiante {nombre} no esta en la lista")
    time.sleep(2)
def ordenar_estudiantes():
    estudiantes.sort()
    print("==Lista de estudiantes==")
    for estudiante in estudiantes:
        print(f"- {estudiante}")
        print("La lista ha sido ordenada")
    time.sleep(2)

def mostrar_total_estudiantes():
    print(f"Total de estudiantes: {len(estudiantes)}")
    time.sleep(2)