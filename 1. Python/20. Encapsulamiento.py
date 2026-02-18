class persona:
    def __init__(self, identificacion, nombre, edad):
        self.__identificacion = identificacion # Dato privado con __
        self.nombre = nombre
        self.edad = edad

    def saludo(self):
        return ("Hola" + str(self.nombre))

    def getIdentificacion(self):
        return self.__identificacion

    def setIdentificacion(self, valor):
        self.__identificacion = valor

persona1 = persona(4521, "Luis", 45)
persona1.setIdentificacion(123456)

print(persona1._persona__identificacion)
print(persona1.getIdentificacion())
print(persona1.nombre)
print(persona1.edad)
