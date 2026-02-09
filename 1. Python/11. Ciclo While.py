# Ciclo While
contador = 0

print("Calculadora de Indice de Masa Corporal IMC")
while contador != 2:
    contador = int(input("¿Quieres seguir calculando la masa corporal? 1. Si 2. No /n").strip())

    if contador == 1:
        estatura = float(input("Ingrese la estatura: ").strip())
        peso =  float(input("Ingrese el peso: ").strip())
        resultadoIMC = round((peso / estatura ** 2), 2)

        if resultadoIMC < 18.5:
            print(f'IMC {resultadoIMC} = Bajo de Peso')
        elif 18.5 < resultadoIMC < 24.99:
            print(f'IMC {resultadoIMC} = Peso Normal')
        elif 25 < resultadoIMC < 30:
            print(f'IMC {resultadoIMC} = Sobre Peso')
        elif resultadoIMC > 30:
            print(f'IMC {resultadoIMC} = Obesidad')
    elif contador == 2:
        print("Hasta Pronto!")

print("Gracias por Usar la Calculadora de Indice de Masa Corporal IMC")




