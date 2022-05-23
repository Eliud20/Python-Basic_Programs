num1 = int (input("Ingrese el primer numero: "))
num2 = int (input("Ingrese el segundo numero: "))
num3 = int (input("Ingrese el tercer numero: "))

if(num1 > num2):
    if(num1 > num3):
        print("El numero1 " + str(num1) + " es mayor que todos")
    else:
        if (num3 > num2):
            print("El numero3 " + str(num3) + " es mayor que todos")
        else:
            print("El numero2 " + str(num2) + " es mayor que todos")
else:
    if(num2 > num3):
        print("El numero2 " + str(num2) + " es mayor que todos")
    else:
        if num3 > num1:
            print("El numero3 " + str(num3) + " es mayor que todos")
