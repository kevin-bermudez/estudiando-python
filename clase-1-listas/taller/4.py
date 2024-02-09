subjects=['Matematicas','Fisica','Quimica','Historia','Lengua']
grades=[]


for name in subjects:
    grade=float(input('coloque su nota de ' + name + ' '))
    
    if grade < 3.5:
        grades.append(None)
        continue
        
    grades.append(grade)
    
for  i in range(0,len(subjects)):
    if grades[i] is not None:
        print('En ',subjects[i],'has sacado',grades[i])
    
    