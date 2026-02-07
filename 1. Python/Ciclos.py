# Ciclo For
word = input("Ingresa una palabra: ").strip().capitalize()

print("Comienzo")

for iterar in range(10):
    print(word)

for i in [3, 4, 5]:
    print(f'Hola!! Ahora i vale {i} y su cuadrado es {i ** 2}')

print('Finalizo')

Contador = 1

for i in range(10):
    print(f'Estoy en la vuelta {Contador}')
    Contador += 1

# Ciclo While