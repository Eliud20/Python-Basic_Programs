alumnos = 0
mayor = 0
menor = 0
while alumnos <= 10:
    calif = int(input("Ingrese la calificacion: "))
    if calif >= 7:
        mayor = mayor + 1
    else:
        menor = menor + 1
    alumnos = alumnos + 1
print("Alumnos con mas o 7: " + str(mayor))
print("Alumnos con menos de 7: " + str(menor))
