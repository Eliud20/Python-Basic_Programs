num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
if(num1 > num2):
    suma = num1 + num2
    resta = num1 - num2
    print("La suma es: " + str(suma))
    print("La resta es: " + str(resta))
else:
    mult = num1 * num2
    div = num1 // num2
    print("La suma es: " + str(mult))
    print("La resta es: " + str(div))
