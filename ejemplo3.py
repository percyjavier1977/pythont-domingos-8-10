promedio = float(input("Ingrese su promedio:\n"))
aprobacion = input("¿Tiene aprobación del profesor (si/n2):").lower()
if promedio >=10.5 or aprobacion == "si":
    print("Puede ingresar a la clase")
else:
    print("No puede ingresar a la clase")