"""Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
 pregunte al usuario la nota que ha sacado en cada asignatura, y después las
 muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde
 <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de
 las correspondientes notas introducidas por el usuario."""

# Asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
#
#
# name=input("¿What's your name?")
# print(f"Hello {name}\n")
#
# for i in Asignaturas:
#     nota = input(f"¿Cuánto has sacado en {i}?")
#     print(f"En {i} has sacado {nota}\n")


##############################################

"""Escribir un programa que pregunte al usuario los números ganadores
de la lotería primitiva, los almacene en una lista y los muestre por
pantalla ordenados de menor a mayor."""

# numloteria = input('¿Cuál es el número de la Loteria?: ')
#
# numloteria = []
#
# ordenados=sorted(numloteria)
#
# print(ordenados)


##############################################

"""Escribir un programa que almacene en una lista los números 
 del 1 al 10 y los muestre por pantalla en orden inverso separados 
 por comas."""

# number = [1,2,3,4,5,6,7,8,9,10]
# number.sort(reverse= True)
# print(number)

##############################################

"""Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura y elimine 
de la lista las asignaturas aprobadas. Al final el programa debe mostrar 
por pantalla las asignaturas que el usuario tiene que repetir."""

name = input("¿What's your name?")
print(f"Hello {name}")

subjects = ["Matemáticas", "Química", "Física", "Historia", "Lengua"]
desaprobadas = []

for i in subjects:
    score = float(input(f'¿Cuanto has sacado en {i}?: '))

    if score <= 10:
        desaprobadas.append(i)
print(f"Has desaprobado y tienes que repetir: {desaprobadas}")

##############################################

"""Escribir un programa que almacene el abecedario en una lista, 
elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
y muestre por pantalla la lista resultante."""

# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T',
#               'u',
#               'V', 'W', 'Y', 'Z']
#
# for i in range(len(alphabet), 1, -1):
#     if i % 3 == 0:
#         alphabet.pop(i-1)
# print(alphabet)
