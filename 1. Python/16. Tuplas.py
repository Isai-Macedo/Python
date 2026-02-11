numeros = (5, 6, 7, 8, 5, 5, 6, 7, 90, 12, 14, 72)

numero = int(input("Ingresa un número: ").strip())

print("El número se repite: " + str(numeros.count(numero)) + " veces")
print("El número " + str(numero) + " Se encuentra en el indice: " + str(numeros.index(numero)))