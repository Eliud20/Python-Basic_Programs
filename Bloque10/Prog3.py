lis1 = []
lis2 = []
lis3 = []

for i in range(5):
    num1 = int(input("Ingrese en la lista1: "))
    lis1.append(num1)
    num2 = int(input("Ingrese en la lista2: "))
    lis2.append(num2)

for x in range(5):
    num3 = lis1[x] + lis2[x]
    lis3.append(num3)


print("Lista1:", lis1)
print("Lista2:", lis2)
print("Sumas:", lis3)
