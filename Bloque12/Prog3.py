def area():
    b = int(input("Dame la base: "))
    h = int(input("Dame la altura: "))
    res = (b * h) / 2
    print("El area es:", res)
    print("********************************")


def fibo():
    lim = int(input("Ingrese el limite: "))
    n1 = 0
    n2 = 1
    i = 0
    cadena = str(n1) + " " + str(n2) + " "
    while i < lim - 2:
        temp = n1 + n2
        cadena = cadena + str(temp) + " "
        n1 = n2
        n2 = temp
        i = i + 1

    print(cadena)
    print("*************************************")



#main
area()
fibo()
