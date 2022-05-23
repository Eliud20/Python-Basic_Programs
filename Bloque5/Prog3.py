empleados = int(input("Cuantos empleados? "))
menos_tresc = 0
mas_tresc = 0
total = 0
i = 0
while i < empleados:
    sueldo = int(input("Ingrese el sueldo: "))
    if sueldo >= 100 and sueldo <= 300:
        menos_tresc = menos_tresc + 1
    else:
        mas_tresc = mas_tresc + 1
    total = total + sueldo
    i = i + 1

print("Personas con sueldo entre $100 y $300: " + str(menos_tresc))
print("Personas con sueldo mayor de $300: " + str(mas_tresc))
print("Total de sueldos: " + str(total))
