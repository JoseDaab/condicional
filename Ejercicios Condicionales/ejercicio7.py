edad = int(input("Ingrese la edad: "))

if edad < 10:
    print("Es un niño.")
elif 10 <= edad < 15:
    print("Es un preadolescente.")
elif 15 <= edad < 18:
    print("Es un adolescente.")
elif 18 <= edad <= 50:
    print("Es un adulto.")
else:
    print("Es un adulto mayor.")