names=[]
ages=[]

while True:
    name=input('Ingrese el nombre del usuario: ')

    if name.lower() == 'salir':
        break
    
    age=int(input('Ingrese la edad de usuario: '))
    
    names.append(name)
    ages.append(age)
    
for i in range(0,len(names)):
    message='no es mayor de edad'
    if ages[i] >= 18:
        message='es mayor de edad'
    
    singplur='año'
    if ages[i] > 1:
        singplur='años'
    
    print(f'El usuario {names[i]} tiene {ages[i]} {singplur} y {message}')