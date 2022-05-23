class Persona:

    def iniciar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


    def mostrarEdad(self):
        if self.edad >= 18:
            print("Mayor de edad")
        else:
            print("Menor de edad")


#main
persona1 = Persona()
persona1.iniciar("Ramon", 15)
persona1.imprimir()
persona1. mostrarEdad()
print("*" * 10)

persona2 = Persona()
persona2.iniciar("Monica", 25)
persona2.imprimir()
persona2. mostrarEdad()
