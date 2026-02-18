class vehiculo:
    def __init__(self, matricula, marca, modelo, color):
        self.matricula = matricula
        self.marca =  marca
        self.modelo = modelo
        self.color = color
        self.avanzar = False
        self.frenar = False
        self.girar = False

    def Avanzar(self):
        self.avanzar = True

    def Frenar(self):
        self.frenar = True

    def Girar(self):
        self.girar =  True

    def imprimir(self):
        print(f'Matricala: {self.matricula} \nMarca: {self.marca} \nModelo: {self.marca} \n'
              f'Color: {self.color} \nAvanzar: {self.avanzar} \n' 
              f'Frenar: {self.frenar} \nGirar: {self.girar}')

class Moto(vehiculo):
    def __init__(self, matricula, marca, modelo, color, cilindraje):
        super().__init__(matricula, marca, modelo, color)
        self.cilindraje =  cilindraje

Moto1 = Moto("GHT158", "Italika", 1982, "Azul", 160)
Moto1.Avanzar()
Moto1.Girar()
Moto1.imprimir()
print("Cilindraje: " + str(Moto1.cilindraje))