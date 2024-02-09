numbers=[1,2,3,4,5,6,7,8,9,10]
print('Lista original: ',numbers)

toAdd=input('Elemento a agregar: ')
indexToAdd=int(input('Posición donde desea agregar el elemento: '))
numbers.insert(indexToAdd,toAdd)

print('Nueva lista: ',numbers)