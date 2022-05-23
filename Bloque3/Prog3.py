num = int(input("Ingrese un numero: "))

if(num >= 0 and num <= 9):
    print("Un digito")
else:
    if(num >= 10 and num <= 99):
        print("Dos digitos")
    else:
        if(num >= 100 and num <= 999):
            print("Tres digitos")
        else:
            print("Error, mas de 3 digitos")
