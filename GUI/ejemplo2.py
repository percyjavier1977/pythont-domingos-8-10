import tkinter as tk
ventana = tk.Tk()
ventana.title("Mi primera aplicación")
ventana.geometry("400x300")
ventana.configure(bg="lightblue")

etiqueta = tk.Label(ventana,text="¡Hola bienvenido a Tkinter!", font=("arial",14), bg="lightblue",fg="blue")
etiqueta.pack(pady=10)

entrada = tk.Entry(ventana, font=("Arial",12))
entrada.pack(pady=10)

#Funcion
def mostrar_saludo():
    texto = entrada.get() #Obtener el texto del cuadro de texto entrada
    etiqueta.config(text=f"¡Hola, {texto.upper()}!")

boton = tk.Button(ventana,
                  text="Mostrar saludo",
                  command=mostrar_saludo,
                  font=("Arial",12))

boton.pack(pady=20)
ventana.mainloop()
