def menor():
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    num3 = int(input("Ingrese el tercer numero: "))

    if num1 > num2 and num1 > num3:
        print("El primero:", num1, "es mayor")
    elif num2 > num1 and num2 > num3:
        print("El segundo:", num2, "es mayor")
    else:
        print("El tercero:", num3, "es mayor")
        
    print("**************************************")


#main
menor()
menor()
