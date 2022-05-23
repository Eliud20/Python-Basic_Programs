nomb = []
nota = []
lis = []

for i in range(4):
    nom = input("Ingresa el nombre " + str(i) + ": ")
    nomb.append(nom)
    cali = int(input("Ingresa nota " + str(i) + ": "))
    nota.append(cali)

cont = 0
for x in range(4):
    if nota[x] > 8:
        lis.append("Muy bueno")
        cont += 1
    elif nota[x] >= 4 and nota[x] <= 7:
        lis.append("Bueno")
    else:
        lis.append("Insuficiente")


print("Nombres:", nomb)
print("Notas:", nota)
print("Calificacion:",lis)
print("Muy buenos:", cont)
