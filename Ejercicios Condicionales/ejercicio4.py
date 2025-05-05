edad = float (input("ingrese edad"))
licencia = input("ingrese licencia si o no")
if edad>=18 and licencia == "si":
    print ("puede conducir")
elif edad<=18 and licencia == "no":
    print("no puede conducir")
else:
    print("Error")