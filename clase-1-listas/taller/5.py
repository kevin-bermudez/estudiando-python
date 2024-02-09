abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
mult3=[]
index=0

for i in abc:
    if index % 3 == 0 and index != 0:
        mult3.append(i)
    
    index += 1
        
print(mult3)