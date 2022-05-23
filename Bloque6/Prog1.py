coordenadas = int(input("Cuantas coordenadas quieres? "))
cuad1 = 0
cuad2 = 0
cuad3 = 0
cuad4 = 0
for i in range (coordenadas):
    x = int(input("X" + str(i) + ": "))
    y = int(input("Y" + str(i) + ": "))
    if x > 0 and y > 0:
        cuad1 = cuad1 + 1
    else:
        if x < 0 and y > 0:
            cuad2 = cuad2 + 1
        else:
            if x > 0 and y < 0:
                cuad4 = cuad4 + 1
            else:
                if x < 0 and y < 0:
                    cuad3 = cuad3 + 1
                else:
                    print("Esta en 0")


print("Cuadrante 1: ", cuad1)
print("Cuadrante 2: ", cuad2)
print("Cuadrante 3: ", cuad3)
print("Cuadrante 4: ", cuad4)
