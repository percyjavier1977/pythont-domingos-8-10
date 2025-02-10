import mysql.connector
conexion = mysql.connector.Connect(
    host ="localhost",
    user = "root",
    password = "toor",
    database = "tienda"
)

cursor = conexion.cursor()

#Insertar el registro
nombre = input("Ingrese el producto: ").capitalize()
precio = float(input("Ingrese el precio del producto : "))

consulta = "INSERT INTO productos (nombre,precio) VALUES (%s, %s)"
valores = (nombre,precio)

#Insertar el registro
cursor.execute(consulta,valores)
conexion.commit()
print(f"Producto: {nombre} agregado con exito")

#Mostrar los registros
consulta_select ="SELECT * FROM productos"
cursor.execute(consulta_select)

print("\nRegistros de la tabla: Productos")
for (id,nombre,precio) in cursor.fetchall():
    print(f"ID: {id}, Nombre: {nombre}, Preecio: {precio}")

#cerra la conexion
cursor.close()
conexion.close()

