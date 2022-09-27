'''PLAYFAIR CIPHER EMULATOR'''
import string
key=input("Enter the key")
fact_check = 1
if(key.isalpha):
    for i in range(len(key)):
        if(key.count(key[i])!=1):
            print("Invalid key entered as the letter "+key[i]+" occurs more than once in the key that you have inputted.")
            fact_check = 0
            break
if(fact_check==1):
    text = input("Enter the text you want to encrypt : ")
    plaintext = list(text)
    encrypted_cipher = ""
    matrix = []
    if(text.isalpha):
        for i  in range(len(plaintext)):
            if(((i+1)<len(plaintext))and(plaintext[i]==plaintext[i+1])):
                plaintext.insert(i+1,'x')
        if(len(plaintext)%2!=0):
            plaintext.extend("x")
        l=0
        for j in range(5):
            for k in range(5):
                if(l<len(key)):
                    matrix[j][k] = key[l]
                    l = l+1 
                else:
                    reference = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                    
    
    
    else:
        print("Invalid text entered .")
        
else:
    print("Invalid key entered.")               