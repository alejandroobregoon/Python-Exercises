# Las tuplas son INMUTABLES
# Crear una tupla -
# Acceder a la tupla mediante índice, índices negativos y expresión [a:b] -
# Anidar a una tupla padre
# Obtener la longitud de una tupla y una subtupla

Transporte = ("Avion", "Auto", "Canoa", "Crucero")
print(Transporte)
print(type(Transporte))


print(Transporte[1])
print(Transporte[-1])
print(Transporte[1:3])

Others_Transportes = ("Bicicleta", Transporte, "Camión", "Kayak")
print(Others_Transportes)

print(Others_Transportes[1][2])

print(len(Others_Transportes))
print(len(Transporte))

