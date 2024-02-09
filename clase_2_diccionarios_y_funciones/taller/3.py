# Fruta	Precio
# Plátano	1.35
# Manzana	0.80
# Pera	0.85
# Naranja	0.70

pricePerKilo={
    'Plátano' : 1.35,
    'Manzana' : 0.80,
    'Pera' : 0.85,
    'Naranja' : 0.70
}

fruit=input('Ingresa el nombre de una fruta: ')

if fruit not in pricePerKilo:
    print(f'La fruta: {fruit} no está en inventario')
    exit()

kilos=input('Ingresa una cantidad de kilos: ')

print(f'Para la fruta: {fruit} con {kilos} kilos el precio es {float(kilos) * pricePerKilo.get(fruit)}')