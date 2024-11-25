try:
    edad = int(input("Ingrese su edad: "))
    if edad <=0:
        raise ValueError("La edad no puede ser número negativo")
    print("Ingreso la edad:",edad)
except ValueError as e:
    print("¡ERROR!",e)
    
    
    