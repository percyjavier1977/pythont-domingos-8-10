import tkinter as tk
#Crear la ventana
ventana = tk.Tk()
ventana.title("Sistema de datos")
ventana.geometry("500x450")

etiqueta = tk.Label(ventana, text="Hola bienvenido a Python",font=("Arial",14))
etiqueta.pack(pady=80)

#Inical el bucle principal de la aplicación
ventana.mainloop()

