monto = float(input("Ingrese el monto total de su compra: "))

if monto >= 200:
    descuento = 0.20
elif monto >= 100:
    descuento = 0.10
else:
    descuento = 0

total = monto - (monto * descuento)

print("Monto con descuento aplicado: ",total)