word=input('Ingrese una palabra: ')
wordSplited=list(word)
reversedWord=wordSplited[::-1]

if wordSplited == reversedWord:
    print(f'La palabra {word} es un palíndromo')
    exit()
    
print(f'La palabra {word} no es un palíndromo')