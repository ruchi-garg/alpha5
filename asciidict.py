char=input("enter a character ")
d ={}

if char in 'aeiouAEIOU':
    d[char]= ord(char)
    print(d)
else:
    print("its not a vowel")
    
    
