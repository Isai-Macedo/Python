primera_forma = {
    "Andrea"
    , "Luis"
    , "Raul"
    , "Sandra"
}

print(primera_forma)

segunda_forma = set(
    [
        "Php"
        , "JavaScript"
        , "Html"
        , "Python"
    ]
)

segunda_forma.add("C#")
segunda_forma.clear()
segunda_forma.pop()
segunda_forma.remove("JavaScript")

print(segunda_forma)

todos = primera_forma.union(segunda_forma)
print(todos)