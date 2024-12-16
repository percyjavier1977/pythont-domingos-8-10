print("=========PROCESO DE VENTA=============")
while True:
    try:
        cantidad = int(input("Ingrese la cantidad de compra (Mayor a  0): ").strip())
        if cantidad <=0:
            raise ValueError ("La cantidad debese ser mayor a 0")
        break
    except ValueError as e:
        print(f"¡ERROR! {e}. Por favor intente nuevamente \n")
        

while True:
    try:
        precio = float(input("Ingrese el precio de compra (Mayor a 0): "))
        if precio <=0:
            raise ValueError ("El precio debe ser mayor a 0")
        break
    except ValueError as e:
        print(f"¡ERROR! {e}. Por favor intente nuevamente \n")

while True:
    try:
        descuento = float(input("Ingrese el porcentaje de descuento (0 a 100): "))
        if descuento <0 or descuento > 100 :
            raise ValueError("El descuento debe se entre 0 y 100")
        break
    except ValueError as e:
          print(f"¡ERROR! {e}. Por favor intente nuevamente \n")
          
importe = cantidad * precio
descuento_aplicado  = importe * (descuento / 100 ) 
total = importe - descuento_aplicado

#Mostrar el detalle de la venta
print("\n========DETALLE DE LA VENTA==========")
print(f"Cantidad de productos {cantidad}")
print(f"Precio unitario: S/{precio:.2f}")
print(f"El importe es: S/{importe:.2f}")
print(f"Descuento aplicado es: {descuento}%: S/{descuento_aplicado:.2f}")
print(f"El Total a pagar: S/{total:.2f}")

