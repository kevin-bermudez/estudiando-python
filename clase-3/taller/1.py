def potencia(base,potencia):
    acum=base*base
    
    for i in range(1,potencia-1):
        acum *= base
    
    return acum

print(potencia(2,4))