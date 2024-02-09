name=input('Cual es su nombre: ')
age=input('Cual es su edad: ')
address=input('Cual es su dirección: ')
phone=input('Cual es su teléfono: ')

person={
    'name' : name,
    'age' : age,
    'address' : address,
    'phone' : phone
}

print(f'{person.get('name')} tiene {person.get('age')} años, vive en {person.get('address')} y su número de teléfono es {person.get('phone')}.')