def calcTime(hours):
    return {
        'minutes' : hours * 60,
        'seconds' : hours * 60 * 60
    }
    
print(calcTime(1))