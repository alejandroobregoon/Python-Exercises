# En otros lenguajes se conocen como Json o HashMap
# Crear un Diccionario -
# Agregar un elemento al Diccionario -
# Agregar una Lista -
# Agregar una Tupla -
# Funciones para mostar la data del Diccionario values, keys, item
# Acceder a un valor

Books = {
    "Robert Kiyosaki": "Padre Rico, Padre Pobre",
    "Dante Alighrei": "La Divina Comedia",
    "Juan Salvador": "Juan Salvador Gaviota"
}

print(Books)

Books["Libros"] = ["The Ego is ENEMY", 1561, "Hello", "Hello", "Robert Kiyosaki" "Padre Rico, Padre Pobre"]
Books["Location"] = "Mand"
Books["Location"] = "Mand"
print(Books)

Books["Juguetes"] = ("Bozz", "Goku", "Vegeta", "Cell")
print(Books)

print(Books.items())
print(Books.keys())
print(Books.values())

Colores = {
    "Diccionario de Libros":Books,
    "Colores Primarios" : ["Verde, Rojo, Azuel"]
}

print(Colores)

print(Colores["Colores Primarios"])

print(Colores["Diccionario de Libros"])

print(Books["Robert Kiyosaki"])
