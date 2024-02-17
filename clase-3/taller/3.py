def ConvertirEspaciado(text):
    newText=''
    for char in text:
        newText += char + ' '
    
    return newText
        
print(ConvertirEspaciado('hola'))