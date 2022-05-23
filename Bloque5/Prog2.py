personas = int(input("Cuantas personas? "))
i = 0
tot = 0
while i < personas:
    alt = float(input("Altura: "))
    tot = tot + alt
    i = i + 1
prom = tot / personas
print("El promedio fue: " + str(prom))
    
