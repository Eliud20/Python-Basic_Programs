lista = []
prom = 0

for i in range(5):
    alt = float(input("Ingrese la altura " + str(i) + ": "))
    lista.append(alt)
    prom += lista[i]

tot = prom / 5

cont1 = 0
cont2 = 0

for x in range(len(lista)):
    if lista[x] > tot:
        cont1 += 1
    else:
        cont2 += 1

print("Alturas:", lista)
print("Promedio:", tot)
print("Personas altas:", cont1)
print("Personas bajas:", cont2)
        
