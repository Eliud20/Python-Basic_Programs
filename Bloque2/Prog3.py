num = int(input("Ingrese un numero: "))

if(num < 0):
    print("Numero negativo ", str(num))
elif num < 10:
    print("El numero es de un digito ", str(num))
else:
    print("El numero es de dos digitos ", str(num))
