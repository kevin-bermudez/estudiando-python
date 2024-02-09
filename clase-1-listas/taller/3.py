names=[]

while True:
    name=input('Ingresa el nombre de una persona: ')
    
    if name == 'me voy':
        break
    
    names.append(name)

names.sort(reverse=True)
print(names)