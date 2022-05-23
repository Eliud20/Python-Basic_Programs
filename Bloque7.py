nom1 = input("Ingresa el primer nombre: ")
nom2 = input("Ingresa el segundo nombre: ")

if nom1 > nom2:
    print(nom1, "es mayor que", nom2)
    print("Ordenados:")
    nom1, nom2 = nom2, nom1
    print(nom1)
    print(nom2)
else:
    print(nom2, "es mayor que", nom1)
    print("Ordenados:")
    print(nom1)
    print(nom2)
