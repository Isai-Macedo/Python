asignaturas =["matematicas", "fisica", "ingles", "español"]

print(asignaturas[1])

numeros = []
for i in range(6):
    numeros.append(int(input("Introduce u número: ").strip()))
numeros.sort()
print(f'Los números ganadores son: {numeros}')

lista = [1, 2, 3, 4, 5, 6, 7, 8, 'Hola']

for i in lista:
    print(i)

lista.reverse()
lista.count(2)
lista.index("Hola")
lista.remove('Hola')
lista.pop(5)
del lista[0]
lista.clear()

for i in lista:
    print(i)