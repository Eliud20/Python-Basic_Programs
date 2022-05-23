preguntas = int(input("Cuantas preguntas fueron? "))
correctas = int(input("Cuantas correctas? "))

porc = (correctas * 100) / preguntas

if porc >= 90:
    print("Nivel maximo " + str(porc))
else:
    if porc >= 75:
        print("Nivel medio " + str(porc))
    else:
        if porc >= 50 and porc < 75:
            print("Nivel regular " + str(porc))
        else:
            print("Nivel bajo " + str(porc))
        
