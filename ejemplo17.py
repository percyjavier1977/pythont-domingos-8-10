import random
suma = 0
intentos = 0
while intentos < 3:
    dado = random.randint(1,6)
    print(f"Tiro del dado es: {dado}")
    intentos+=1
    suma +=dado
    
print(f"La suma total de los tres tiros es: {suma}")

    
    