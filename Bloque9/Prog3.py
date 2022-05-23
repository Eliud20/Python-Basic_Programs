man = []
tar = []

print("Mañana: ")
for i in range(4):
    suel = float(input("Ingrese el sueldo " + str(i) + ": "))
    man.append(suel)


print("Tarde: ")
for x in range(4):
    sueld = float(input("Ingrese el sueldo " + str(x) + ": "))
    tar.append(sueld)


print("Sueldos mañana:", man)
print("Sueldos tarde:", tar)
