# Por ejemplo supongamos que debemos hacer un programa donde se almacenen los nombres de lo estudiantes de un grupo, se debe pedir estos nombres y cuando se ingrese la palabra salir debe parar el ingreso, finalmente se deben mostrar los nombres organizados en orden alfabético.

# students=[]
# while True:
#     name=input("nombre del estudiante ")
    
#     if name=='salir':        
#         print('salir')
#         break
    
#     students.append(name)  
# students.sort()      
# print(students)

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.


Asignaturas=["Matematicas","Fisica","Quimica","Historia","lengua"]
Notas=[]


for name in Asignaturas:
    nota=input('coloque su nota de ' + name)
    Notas.append(nota)
    
for  i in range(0,5):
    print("En ",Asignaturas[i],"has sacado",Notas[i])
    
    