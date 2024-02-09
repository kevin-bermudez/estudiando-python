diccionario = {
    "a" : 1,
    "b" : 2
}

# contar elementos de un diccionario
print('Len',len(diccionario))

# verificar si un elemento tiene una clave
print()
print('In','a' in diccionario,1 in diccionario)

# borrar todos los item del diccionario
print()
diccionario.clear()
print('Clear',diccionario)

# devolver una copia del diccionario
print()
diccionarioRef = diccionario
diccionarioRef['a'] = 3
print('Copy refs',diccionario,diccionarioRef)
print()
diccionarioCopy = diccionario.copy()
diccionarioCopy['a'] = 4
print('Copy',diccionario,diccionarioCopy)

# fusionar diccionarios D1.update(D2) mete D2 en D1
print()
diccionario2={
    "c" : 3,
    "d" : 4
}
diccionario.update(diccionario2)
print('Update',diccionario,diccionario2)

# Obtener un elemento del diccionario
print()
print('Get',diccionario.get('a'),diccionario['d'])

# si no existe la key le asigna el valor por defecto
print()
diccionario.setdefault('e',3)
print('Setdefault',diccionario)

# devuelve y elimina último elemento
print()
print('Popitem acción',diccionario.popitem())
print('Popitem',diccionario)

# Borra el item con la key que se le pase
print()
print('Pop acción',diccionario.pop('a'))
print('Pop',diccionario)

# Crea un diccionario y lo devuelve, con las claves y les asigna el mismo valor fromkeys(claves,valor)
print(dict.fromkeys(['a','b'],0))