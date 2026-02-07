# Condicionales

# If, Else
anio =  int(input("Ingresa los años que tiene tu computadora: ").strip())

if anio <= 0 or anio >= 2:
    print("Tu computador es nuevo")
else:
    print("Tu computador es viejo")

edad = int(input("Cuantos años tienes: ").strip())

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
print("¡Hasta la proxima!")

# If, Else y Elif
if 0 <= edad <= 10:
    print("Eres un niño")
elif 11 <= edad <= 18:
    print("Eres un joven")
elif 19 <= edad <= 60:
    print("Eres un adulto")
else:
    print("Eres un anciano")
