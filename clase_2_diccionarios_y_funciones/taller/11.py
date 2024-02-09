import math

def decToBin(dec):
    numbInt = dec
    digits = []
    
    while True:
        aux =  math.floor(numbInt / 2)
        resi = numbInt % 2
        numbInt = aux
        
        digits.append(str(resi))
        
        if(( numbInt == 0 or numbInt == 1 )):
            if dec != 0:
                digits.append(str(numbInt))
            break
    
    digits.reverse()
    return ''.join(digits)

print(decToBin(0))