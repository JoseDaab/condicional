calificacion = float (input("ingrese nota"))

if calificacion >=4.5:
    print ("superior")
elif calificacion>=3.9 and calificacion<4.5:
    print ("alto")
elif calificacion>=3.0 and calificacion<3.9:
    print ("basico")
elif calificacion>=1.0 and calificacion<3.0:
    print ("bajo")
else:
    print ("estudiante no evaluado")