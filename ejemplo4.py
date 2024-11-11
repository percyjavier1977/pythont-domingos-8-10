años = int(input("Ingrese años de trabajo:\n"))
categoria = input("Ingre su categoria (a,b,c)\n").lower()

#Bonificacion solo a los que tienen mas de 10 años de servicio y tengan categoria a o b

if (categoria == "a" or categoria == "b")and años >10:
    print("Usted tiene acceso al bono")
else:
    print("usted no tiene acceso al bono")



