from sys import argv

if len(argv) < 2:
    print("Son poco argumentos")
elif len(argv) > 2:
    print("Son muchos argumentos")

print("hola, mi nombre es", argv[1])

'''
# Libreria Sys

La biblioteca sys de Python es un módulo integrado que proporciona acceso a variables y funciones que interactúan directamente con el intérprete de Python. A diferencia del módulo os (que se enfoca en el sistema operativo), sys se utiliza para manipular el entorno de ejecución de Python. 

# Funciones y Variables Principales

Según la documentación oficial de Python, estas son sus herramientas más esenciales:
sys.argv: Una lista que contiene los argumentos de la línea de comandos pasados al script.
sys.argv[0] es siempre el nombre del script.
sys.path: Una lista de cadenas que especifica la ruta de búsqueda de módulos. Puedes modificarla con .append() para importar módulos desde directorios personalizados.
sys.exit([arg]): Finaliza la ejecución del script. Un argumento 0 indica éxito, mientras que cualquier otro número indica un error.
sys.platform: Devuelve una cadena que identifica la plataforma (ej. 'win32', 'linux', 'darwin').
sys.stdin, sys.stdout, sys.stderr: Objetos de archivo que corresponden a la entrada, salida y errores estándar del intérprete.
sys.getsizeof(obj): Devuelve el tamaño de un objeto en bytes
'''