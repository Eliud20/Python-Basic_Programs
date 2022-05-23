n1 = float(input("Ingrese la primera calificacion: "))
n2 = float(input("Ingrese la segunda calificacion: "))
n3 = float(input("Ingrese la tercera calificacion: "))

prom = (n1+n2+n3) / 3

if(prom > 7):
    print("Promocionado")
else:
    print("No promocionado")
