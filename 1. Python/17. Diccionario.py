diccionario_primera_forma = {
    "Nombre" : "Isai"
    , "Apellido" : "Macedo"
    , "Edad" : 42
    , "Documento" : 12456
}

print(diccionario_primera_forma)
print(diccionario_primera_forma.keys())
print(diccionario_primera_forma.values())
print(diccionario_primera_forma.items())

diccionario_segunda_forma = dict(
    Nombre = 'Isai'
    , Edad = 37
    , Documento = 123654
)

print(diccionario_segunda_forma)

diccionario_tercera_forma = dict(
    [
        ('Nombre', 'Sara')
        , ('Edad', 37)
        , ('Documento', 123654)
    ]
)

print(diccionario_tercera_forma)


