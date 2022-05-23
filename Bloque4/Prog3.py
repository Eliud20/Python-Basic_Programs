x = int(input("Ingrese la x: "))
y = int(input("Ingrese la y: "))

if x > 0 and y > 0:
    print("Cuadrante 1")
elif x > 0 and y < 0:
    print("Cuadrante 4")
elif x < 0 and y > 0:
    print("Cuadrante 3")
elif x < 0 and y < 0:
    print("Cuadrante 2")
else:
    print("Hay valor de 0")
