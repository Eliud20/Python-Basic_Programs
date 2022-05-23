lista = [50, 45, 65, 101, 805, 1000, 750, 1200]
contador = 0
for i in range(len(lista)):
    if lista[i] > 100:
        contador += 1

print(lista)
print("Numeros mayores a 100:", contador)
