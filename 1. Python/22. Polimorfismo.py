class Gato():
    def sonido(self):
        print("Miuaaau")

class Perro():
    def sonido(self):
        print("Guaaaau")

class Cerdo():
    def sonido(self):
        print("Grrrrrrr Grrr")
def EscucharSonido(animal):
    animal.sonido()

gato1 = Gato()
perro1 = Perro()
cerdo1 = Cerdo()

EscucharSonido(gato1)
EscucharSonido(perro1)
EscucharSonido(cerdo1)
