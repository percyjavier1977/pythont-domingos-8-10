edad = int(input("Ingrese la edad:\n"))
nacionalidad = input("Ingrese su nacionalidad (peruano,extranjero)\n").lower()
#Verificar si es mayor de edad y peruano
if edad >17 and nacionalidad == "peruano":
    print("Usted puede votar")
else:
    print("Usted no puede votar")
