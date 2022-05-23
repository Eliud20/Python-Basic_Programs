prod = []
prec = []

for i in range(5):
    nom = input("Ingresa el nombre " + str(i) + ": ")
    prod.append(nom)
    pre = int(input("Ingresa precio " + str(i) + ": "))
    prec.append(pre)

cont = 0
for x in range(5):
    if prec[x] > prec[0]:
        cont += 1

print("Productos:", prod)
print("Precio:", prec)
print("Productos mayores al primero:", cont)
