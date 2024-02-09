def someFunction(list,callback):
    newList = []
    
    for i in range(0,len(list)):
        newList.append(callback(i))
        
    return newList

def cuadrado(num):
    return num * num

print(someFunction([0,1,2,3],cuadrado))