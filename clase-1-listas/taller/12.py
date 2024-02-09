numbers=[1,2,3,4,5,6,7,8,9,10]
print('Lista original: ',numbers)
toDelete=int(input('Ingresa el índice que deseas eliminar: '))
numbers.pop(toDelete)
print('Nueva lista: ',numbers)