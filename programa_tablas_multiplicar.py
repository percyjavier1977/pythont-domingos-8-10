import os
os.system("cls")

for i in range (1,13):
    print("------------------------------------")
    print (f"TABLA SE MULTIPLICAR DEL NÚMERO: {i}")
    print ("-----------------------------------")
    for j in range (13):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
    print(" ")