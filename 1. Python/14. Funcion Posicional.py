from numpy.polynomial.legendre import legtrim


def suma (*args):
    s = 0
    for i in args:
        s += i

    return s

resultado = suma(4, 4, 5, 7, 8, 9, 10)
print(resultado)

def lenguaje(nombre, *args):
    print(f'hola {nombre}')
    print(f'Tus lenguajes favoritos son: {args}')

lenguaje("Isai", "JavaScript", "Python")


def lenguaje(nombre, **kwargs):
    print(f'hola {nombre}')
    contador = 0

    for i in kwargs:
        contador += 1
        print(f'Tu {contador} lenguaje favorito es: {kwargs[i]}')

lenguaje("Isai", lenguaje1 = "JavaScript", lenguaje2 = "Python")