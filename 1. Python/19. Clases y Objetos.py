class bicicleta:
    def __init__(self, color, cambio, rin):
        self.color = color
        self.cambio =  cambio
        self.rin = rin

    def frenar(self):
        return "La bicicleta esta frenando"

    def avanzar(self):
        return "La bicicleta esta avanzando"

    def girar(self):
        return "La bicicleta esta girando"


urbana = bicicleta("Rojo", 8, 27.5)
hibrida = bicicleta("Azul", 1, 29)

print("Urbana: " + str(urbana.color))
print("Comportamiento de la bicicleta: " + str(urbana.girar()))
print("\n")
print("Urbana: " + str(urbana.cambio))
print("Comportamiento de la bicicleta: " + str(urbana.avanzar()))