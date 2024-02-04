lista=[]

# agregar elemento
lista.append(1)
print('Append',lista)

# vacear lista
# print()
# lista.clear()
# print('Clear',lista)

# concatenar listas
print()
lista.append(1)
lista.extend([2,3])
print('Extend',lista)

# contar ocurrencias de un elemento en una lista
print()
print('Count',lista.count(1))

# devuelve el índice de la primera ocurrencia de un elemento
print()
print('Index',lista.index(2))

# insertar elemento en una posición concreta de la lista (indice,elemento)
print()
lista.insert(0,0)
print('Insert',lista)

# extraer y eliminar elemento de la lista en la posición dada
print()
eliminado=lista.pop(1)
print('pop',lista,'eliminado',eliminado)

# eliminar un elemento de la lista, recibe como parametro el elemento a borrar, borra la primera ocurrencia
print()
lista.append(0)
lista.remove(0)
print('Remove',lista)

# cambiar el orden de la lista, ponerla al reves
print()
lista.reverse()
print('Reverse',lista)

#ordenar lista de menor a mayor, sorted devuelve la lista
print()
lista.reverse()
lista.sort()
print('Sort',lista)

# Si la lista está previamente ordenada, entonces la consola retornará "None".

# El método sort() puede tomar dos argumentos opcionales llamados key y reverse.
print()
lista.sort(reverse=True)
print('Sort reverse',lista)