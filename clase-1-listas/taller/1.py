subjects=['Matematicas','Fisica','Quimica','Historia','Lengua']
grades=[]


for name in subjects:
    grade=input('coloque su nota de ' + name + ' ')
    grades.append(grade)
    
for  i in range(0,len(subjects)):
    print('En ',subjects[i],'has sacado',grades[i])
    
    