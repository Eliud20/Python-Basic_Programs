class Triangulo:

    def iniciar(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3


    def imprimir(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:

            print("El mayor es el lado 1:", self.lado1)
            
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:

            print("El mayor es el lado 2:", self.lado2)

        elif self.lado3 > self.lado1 and self.lado3 > self.lado2:

            print("El mayor es el lado 3:", self.lado3)

        else:
            print("Hay iguales")


    def equilatero(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("Es equilatero")
        else:
            print("No es equilatero")


#main
triangulo1 = Triangulo()
triangulo1.iniciar(8, 5, 3)
triangulo1.imprimir()
triangulo1.equilatero()



