peso = float(input("Ingrese su pero en kilogramos:\n"))
altura =float(input("Ingrese su altura en metros:\n"))

imc = peso / (altura**2)

if imc < 18.5:
    obs = "Bajo de peso"
elif imc >=18.5 and imc <= 24.9:
    obs = "Peso normal"
elif imc >=25 and imc <=29.9:
    obs = "Sobre peso"
else:
    obs = "Obesidad"
    

print(f"Tu IMC ES: {imc:.2f}")
print(f"La observación es: {obs}")
    
