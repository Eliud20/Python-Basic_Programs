num = int(input("Ingrese el numero: "))
res = num
cad = ""
for i in range(num, 1, -1):
    res = res * (res-1)
    cad = cad + str(res) + " "
    
print(cad)
