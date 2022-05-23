lista = [6, 7, 8, 4, 12]
con = ""

for i in range(len(lista)):
    if lista[i] >= 7:
        con += str(lista[i]) + " "


print("Lista:", lista)
print("Mayores:", con)
