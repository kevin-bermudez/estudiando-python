numbers2=[]
numbers=[]

while True:
    number=input("Ingresa un número: ")
    
    if number.lower() == 'salir':
        break
    
    numberInt=int(number)
    numbers.append(numberInt)
    numbers2.append(numberInt*numberInt)
    
    
for i in range(0,len(numbers)):
    print(f"El cuadrado del número: {numbers[i]} es {numbers2[i]}")