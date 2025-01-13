#Declarar una lista
frutas = ["manzana","platano","naranja","uva","manzana"]

print(frutas)

#Acceder a un elemento de la lista

elemento1 = frutas[0]
print(elemento1)
print(frutas[3])

frutas[1]="Banana"
print(frutas)

#Añadir elementos a la lista
frutas.append("Pera")
print(frutas)

frutas.insert(2,"mango")
print(frutas)

#Eliminar elemento de la lista

frutas.remove("uva")
print(frutas)

frutas.pop(1)
print(frutas)

for fruta in frutas:
    print(fruta)

#Mostrar la cantidad de elementos de la lista
n_frutas = len(frutas)
print(n_frutas)


#verificar si un elento esta en la lista
print("mango" in frutas)
print("zandia" in frutas)

if "fresa" in frutas:
    print("Elemento si existe")
else:
    print("Elemento no existe")


nindice = frutas.index("manzana")
print(nindice)

repeticion = frutas.count("manzana")
print("Existen: ",repeticion)

frutas.sort()
for fruta in frutas:
    print(fruta)