# OPERADORES DE ASIGNACIÓN
x = 5
print(x)
x += 2
print(x)
x -= 2
print(x)
x *= 2
print(x)
x /= 2
print(x)
##########
x = 5
x %= 2
print(x)

x = 5
x //= 2
print(x)

x = 5
x **= 2
print(x)

# OPERATES ARITMÉTICOS
suma = 5 + 5
res = 10 - 5
multi = 10 * 2
div = 5 / 2
residuodiv = 5 % 2
poten = 3 ** 3

text = "Python " * 3
text2 = "Hoy estoy " + "Aprendiendo " + text

# print(suma)
# print(res)
# print(multi)
# print(div)
# print(residuodiv)
# print(poten)
# print(text)
# print(text2)

# OPERADORES RELACIONALES
op1 = 5 > 5
op2 = 5 < 6
op3 = 5 >= 5
op4 = 5 <= 6
op5 = 5 == 5
op6 = 5 != 5
op7 = text == text
op8 = text == text2
op9 = text != text2

print(op1)
print(op2)
print(op3)
print(op4)
print(op5)
print(op6)
print(op7)
print(op8)
print(op9)

# OPERADORES LÓGICOS
# AND TRUE && TRUE = TRUE | SINO TOD0 ES FALSO
# OR FALSE || FALSE = FALSE | SINO TOD0 ES VERDADERO
# NOT REVIERTE ! LA VALOR LÓGICO

print("OPERADORES LÓGICOS")
cur1 = 1 == 1 and 2 == 2
cur2 = 1 == 2 and 2 == 2
cur3 = 1 > 2 or 2 < 2
cur4 = 1 > 2 or 2 == 2
cur5 = not(1 > 2 or 2 == 2)

print(cur1)
print(cur2)
print(cur3)
print(cur4)
print(cur5)
