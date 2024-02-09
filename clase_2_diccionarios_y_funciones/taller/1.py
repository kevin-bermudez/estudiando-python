currencies={
    'Euro':'€', 
    'Dollar':'$', 
    'Yen':'¥'
}

divisa=input('Ingrese una divisa: ')

if divisa not in currencies:
    print('La divisa no está en el diccionario')
    exit()

print('La moneda correspondiente es: ',currencies[divisa])
