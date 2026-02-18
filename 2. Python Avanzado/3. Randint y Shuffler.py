from random import randint, shuffle

numero = randint(1, 10) # Números aleatorios

print(f'Tu número es: {numero}')

cartas = ["Jota", "Reina", "Rey"]
shuffle(cartas)

for carta in cartas:
    print(carta)


'''
# Libreria Random
La biblioteca random de Python es un módulo integrado que permite generar números pseudoaleatorios y realizar operaciones basadas en el azar, como barajar listas o seleccionar elementos aleatorios. 

Debido a que utiliza el algoritmo Mersenne Twister, es determinista y no es apto para fines criptográficos (para seguridad, usa el módulo secrets)

# Funciones Principales
A continuación se presentan las herramientas más utilizadas del módulo, disponibles en la documentación  oficial de Python:

# Generación de Números:
random.random(): Devuelve un número flotante entre 0.0 y 1.0.
random.randint(a, b): Devuelve un entero aleatorio en el rango [a, b] (incluye ambos extremos).
random.uniform(a, b): Devuelve un número flotante aleatorio entre a y b.

# Manipulación de Secuencias:
random.choice(lista): Selecciona un único elemento aleatorio de una secuencia no vacía.
random.sample(lista, k): Devuelve una lista de k elementos únicos elegidos de una población (muestreo sin reemplazo).
random.shuffle(lista): Mezcla los elementos de una lista en su lugar (modifica la lista original).

# Control de Reproducibilidad:
random.seed(x): Inicializa el generador. Usar la misma semilla producirá siempre la misma secuencia de números, lo cual es ideal para pruebas y depuración
'''