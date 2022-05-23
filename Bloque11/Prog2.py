lista = []
lista2 = []
for x in range(5):
    num = int(input("Ingrese un numero: "))
    lista.append(num)

print(lista)

pos = 0
while pos < len(lista):

    if lista[pos] >= 10:
        nue = lista.pop(pos)
        lista2.append(nue)
    else:
        pos = pos + 1

print("Lista anterior: ",lista)
print("Lista nueva: ",lista2)
