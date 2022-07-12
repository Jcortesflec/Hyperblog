from moneda import moneda

opcion=input("¿Que moneda manejas en tu pais?\n\n1. Colombia \n2. Argentina \n3. Brazil \n\ningresa el numero de tu pais \n")
if opcion == "1":
    moneda.colombia()
elif opcion == "2":
    moneda.argentina()
elif opcion == "3":
    moneda.brazil()