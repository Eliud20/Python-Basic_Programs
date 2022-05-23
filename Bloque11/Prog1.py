nomb = []
sueldo = []
for x in range(5):
    nom = input("Ingrese el nombre: ")
    nomb.append(nom)
    canti = int(input("Ingrese el sueldo: "))
    sueldo.append(canti)

print(nomb)
print(sueldo)

i = 0
while i < len(sueldo):
    
    if sueldo[i] > 10000:
        nomb.pop(i)
        sueldo.pop(i)
    else:
        i = i + 1

print(nomb)
print(sueldo)
