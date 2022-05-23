sueldo = int(input("Ingrese el sueldo: "))
anti = int(input("Ingrese la antigüedad: "))

if sueldo < 500 and anti >= 10:
    print("Aumento 20%:", (sueldo * .20) + sueldo)
elif sueldo < 500 and anti < 10:
    print("Aumento 5%:", (sueldo * .05) + sueldo)
elif sueldo >= 500:
    print("Sueldo:", sueldo)
