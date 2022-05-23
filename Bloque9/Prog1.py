lista = []
prom = 0

for i in range(5):
    valor = float(input("Ingrese el sueldo " + str(i) + ": "))
    lista.append(valor)
    prom += lista[i]

tot = prom / 5

print("Sueldos:", lista)
print("Promedio:", tot)
