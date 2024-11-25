try:
    edad = int(input("Ingrese su edad: "))
    try:
        if edad < 0:
            raise ValueError("Ingrese edades mayores a cero")
        print(f"Ingreso la edad {edad}")
    except ValueError as c:
        print("¡ERROR!",c)
except ValueError:
    print("Ingrese correctamente el número")

finally:
    print("FIN DEL PROCESO")
 
        
    