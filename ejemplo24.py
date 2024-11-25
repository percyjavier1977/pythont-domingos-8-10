try:
    nota =float(input("Ingrese la nota: "))
    if nota <0 or nota >20:
        raise ValueError("Debe ingersar la nota entre 0 y 20")
    print(f"La nota ingresada es: {nota}")
    if nota >=10.5:
        print("Nota aprobatoria")
    else:
        print("Nota desaprobatoria")
except ValueError as e:
    print("¡ERROR!", e)

else:
    print("Ingreso correctamente la nota")
    
    
