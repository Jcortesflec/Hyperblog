from Moneda import Conversion

opcion=input("¿Que moneda manejas en tu pais?\n\n1. Colombia \n2. Argentina \n3. Brazil \n\ningresa el numero de tu pais \n")
if opcion == "1":
    Conversion.Colombia()
elif opcion == "2":
    Conversion.Argentina()
elif opcion == "3":
    Conversion.Brazil()