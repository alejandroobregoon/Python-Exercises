# Crear un Sets -
# Crear un Sets con diferentes tipos de elementos -
# Añadir un elemento -
# Añadir varios elementos -
# Remover un elemento de las 2 maneras - // remove si no encuentra un elemento lanza el error y el otro no lo omite ni mostrar error
# Limpiar todos los elementos de un Sets -

set1 = {1,2,3,"Hello",0}
print(set1)

set2 = {"Javier", "Prado", 23123, 460.214, True}
print(set2)

set1.add(4)
print(set1)

set1.update([3,6,7,8,9,9,9,9,9,9])
print(set1)

set1.update([5,10,11,12,12,12,12,12])
print(set1)

set1.remove(10)
print(set1)

set1.discard(9)
print(set1)

set1.discard(10)
print(set1)


set2.clear()
print(set2)

set2.update(["Hello", 234, 2345.5])
print(set2)

