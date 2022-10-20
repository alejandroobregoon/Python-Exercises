# Hacer una Lista y búsqueda por índice -
# Acceder por índice, por negativo y por [a:b] -
# Anidarla a una lista padre -
# Mutabilidad o Modificar un elemento de una lista y una sublista -
# Agregar elementos a una lista con una función -
# Agregar una lista dentro de otra con las dos funciones -
# Voltea la lista -
# obtener el tamaño de una lista y sublista con una funcion -

language = ["Python", "Java", "PHP"]
print(language[2])
print(language[-3])
print(language[1:3])

programacion = ["Dedicación", "Disciplina", language]
print(programacion)

programacion[1] = "Respeto"
print(programacion)

programacion[2][1] = "GO"
print(programacion)

Others_languages = ["Java", "C++", "C#"]
language.append(Others_languages)
print(language)

language.append("Flutter")
print(language)

language.extend(Others_languages)
print(language)

print(programacion)
print(language)

print(len(language))
print(len(Others_languages))

