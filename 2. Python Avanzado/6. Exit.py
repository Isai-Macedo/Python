from sys import argv

if len(argv) < 2:
    print("Son poco argumentos")
elif len(argv) > 2:
    print("Son muchos argumentos")

print("hola, mi nombre es", argv[1])