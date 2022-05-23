lista = ['Raul', 'Carmen', 'Gabriel', 'Rosa', 'Mario']
x = 0

for i in range(len(lista)):
    if len(lista[i]) >= 5:
        x += 1


print("Nombres:", lista)
print("Mas de 5: ", x)
