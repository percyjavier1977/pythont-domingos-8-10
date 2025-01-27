import tkinter as tk
#Funcion
def calcular_promedio():
    try:
        nota1 = float(entrada1.get())
        nota2 = float(entrada2.get())
        nota3 = float(entrada3.get())

        promedio = (nota1+nota2+nota3)/3
        resultado.config(text=f"Promedio: {promedio:.2f}")
        if promedio > 10.5:
            observacion.config(text="Aprobado", fg="blue")
            resultado.config(fg="blue")
        else:
            observacion.config(text="Desaprobado", fg="red")
            resultado.config(fg="red")
    except ValueError:
            observacion.config(text="")
            resultado.config(text="Por favor, ingrese número válidos", fg="red")
            entrada1.delete(0,tk.END)
            entrada2.delete(0,tk.END)
            entrada3.delete(0,tk.END)
            entrada1.focus()



ventana = tk.Tk()
ventana.title("Sistema de notas")
ventana.geometry("400x400")


etiqueta = tk.Label(ventana,text="Ingrese las tres notas:", font=("arial",14))
etiqueta.pack(pady=20)

#Entradas de las tres notas

entrada1 = tk.Entry(ventana, font=("Arial",12))
entrada1.pack(pady=10)

entrada2 = tk.Entry(ventana, font=("Arial",12))
entrada2.pack(pady=10)

entrada3 = tk.Entry(ventana, font=("Arial",12))
entrada3.pack(pady=10)

#Mostrar los resultados en etiquetas
resultado = tk.Label(ventana,text="",font=("Arial",14))
resultado.pack(pady=10)

observacion = tk.Label(ventana,text="",font=("Arial",14))
observacion.pack(pady=10)
            
boton = tk.Button(ventana,
                  text="Calcular promedio",
                  command=calcular_promedio,
                  font=("Arial",12))

boton.pack(pady=10)
entrada1.focus()
ventana.mainloop()