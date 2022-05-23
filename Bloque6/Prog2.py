pos = 0
neg = 0
multi = 0
par = 0
acumu = 0
for i in range (10):
    num = int(input("Ingrese el numero: "))
    if num > 0:
        pos = pos + 1
        if ((num % 15) == 0):
            multi = multi + 1
        if num % 2 == 0:
            par = par + 1
            acumu = acumu + num
    else:
        neg = neg + 1


print("Valores negativos: ", neg)
print("Valores positivos: ", pos)
print("Valores multiplos de 15: ", multi)
print("Valores pares: ",par,", total acumulado: ",acumu)
