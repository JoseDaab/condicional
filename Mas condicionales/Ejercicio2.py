nombre1 = input("Ingrese el nombre del primer hermano: ")
edad1 = int(input("Ingrese la edad del primer hermano: "))

nombre2 = input("Ingrese el nombre del segundo hermano: ")
edad2 = int(input("Ingrese la edad del segundo hermano: "))

if edad1 > edad2:
    print("El hermano mayor es:", nombre1)
elif edad2 > edad1:
    print("El hermano mayor es: ",nombre2)
else:
    print("Ambos tienen la misma edad.")
