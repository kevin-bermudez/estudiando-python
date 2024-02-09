subjects = {
    'Matemáticas': 6, 
    'Física': 4, 
    'Química': 5
}

totalCredits=0
for subject in subjects:
    print(f'{subject} tiene {subjects.get(subject)} créditos')
    totalCredits += subjects.get(subject)

print(f'Total de créditos es: ',totalCredits)