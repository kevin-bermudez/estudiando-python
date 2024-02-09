names=[]
temperatures=[]

while True:    
    temperature=input('Ingrese la temperatura: ')
    
    if temperature.lower() == 'salir':
        break
    
    temperatureF=float(temperature)
    temperatures.append(temperatureF)

sum=0
for temperature in temperatures:
    sum += temperature
    
print(f'La temperatura promedio es: {sum/(len(temperatures))}')