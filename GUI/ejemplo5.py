from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, Frame

#Funcion que calcula la venta
def calcular_venta():
    try:
        producto = entrada_producto.get()
        if not producto:
            raise ValueError("El Producto se debe ingresar")
        
        cantidad = int(entrada_cantidad.get())
        if cantidad <=0:
            raise ValueError("La cantidad debes ser mayor que cero")
        
        precio = float(entrada_precio.get())
        if precio <=0:
            raise ValueError("El precio debe ser mayor a cero")
        
    except ValueError as e:
        messagebox.showerror("Error de entra",str(e))
        return
    #Calculos del programa
    importe = cantidad * precio
    igv =importe * 0.18
    descuento = importe * 0.10 if importe > 200 else 0
    total = importe + igv - descuento

    #Mostrar los resultados
    var_importe.set(f"S/ {importe:.2f}")
    var_igv.set(f"S/ {igv:.2f}")
    var_descuento.set(f"S/ {descuento:.2f}")
    var_total.set(f"S/ {total}")

def limpiar_campos():
    entrada_producto.delete(0,"end")
    entrada_cantidad.delete(0,"end")
    entrada_precio.delete(0,"end")

    entrada_producto.focus()

    var_importe.set("")
    var_igv.set("")
    var_descuento.set("")
    var_total.set("")


ventana = Tk()
ventana.title("Ventas de Producto")
ventana.geometry("400x300")
ventana.configure(bg="#F3F4F6")

#variables para los resultados
var_importe = StringVar()
var_igv = StringVar()
var_descuento = StringVar()
var_total = StringVar()

#Contenedor
frame = Frame(ventana, bg="#F3F4F6")
frame.pack(padx=20, pady=20)

#diseñar la interface
Label(frame, text="Producto", bg="#F3F4F6",font=("Arial",12)).grid(row=0, column=0, sticky="w")
entrada_producto = Entry(frame,font=("Arial",12),width=10)
entrada_producto .grid(row=0, column=1,sticky="w")

Label(frame, text="Cantidad", bg="#F3F4F6",font=("Arial",12)).grid(row=1, column=0, sticky="w")
entrada_cantidad = Entry(frame,font=("Arial",12))
entrada_cantidad .grid(row=1, column=1)

Label(frame, text="Precio Unitario", bg="#F3F4F6",font=("Arial",12)).grid(row=2, column=0, sticky="w")
entrada_precio = Entry(frame,font=("Arial",12))
entrada_precio .grid(row=2, column=1)

#Crear el boton calcular

Button(frame, text="Calcular",command=calcular_venta, bg="#4CAF50", fg="white", font=("Arial",12),width=12).grid(row=3,column=0,pady=10)

Button(frame, text="Limpiar",command=limpiar_campos, bg="#4CAF50", fg="white", font=("Arial",12),width=12).grid(row=3,column=1,pady=10)

#Mostrar los resultados
Label(frame, text="Importe:",bg="#F3F4F6", font=("Arial",12)).grid(row=4,column=0,sticky="w")
Label(frame,textvariable=var_importe,bg="#F3F4F6",font=("Arial",12)).grid(row=4,column=1)

Label(frame, text="IGV(18%):",bg="#F3F4F6", font=("Arial",12)).grid(row=5,column=0,sticky="w")
Label(frame,textvariable=var_igv,bg="#F3F4F6",font=("Arial",12)).grid(row=5,column=1)

Label(frame, text="Descuento:",bg="#F3F4F6", font=("Arial",12)).grid(row=6,column=0,sticky="w")
Label(frame,textvariable=var_descuento,bg="#F3F4F6",font=("Arial",12)).grid(row=6,column=1)

Label(frame, text="Total a Pagar:",bg="#F3F4F6", font=("Arial",12)).grid(row=7,column=0,sticky="w")
Label(frame,textvariable=var_total,bg="#F3F4F6",font=("Arial",12)).grid(row=7,column=1)

ventana.mainloop()
  

