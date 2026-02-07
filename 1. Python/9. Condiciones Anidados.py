# Condiciones Anidados

edad = int(input("Ingresa tu edad: ").strip())
graduacion = input("Estas graduado (Si o No): ").strip().capitalize()

if edad > 17:
    print("Felicidades ya eres mayor de edad")
    if graduacion == "Si":
        print("Felicidades por tu graduación")
    else:
        print("Falta poco, tu puedes")
else:
    print("Eres menor de edad")
