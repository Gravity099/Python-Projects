
#NOTE :  This can be more enhaced by using the string module 
import art

alpha = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p',
          'q','r','s','t','u','v','w','x','y','z','a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p',
          'q','r','s','t','u','v','w','x','y','z']

def encrypt(plain_text , shift_amount):
    """ The function to encrpyt the text as input bu the user"""
    cipher_text = ""
    for letter in plain_text:
        
        if letter in alpha:
            position = alpha.index(letter)
            new_position = position + shift_amount
            new_letter = alpha[new_position]
            cipher_text += new_letter
        
        else:
            cipher_text += letter
    print(f"The encoded text is {cipher_text}")


def decrypt(plain_text , shift_amount):
    """ The function to decrpyt the text based on the paramenters"""
    cipher_text = ""
    for letter in plain_text:
        
        if letter in alpha:
            position = alpha.index(letter)
            new_position = position - shift_amount
            new_letter = alpha[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f"The decoded text is {cipher_text}")


while True:
    print(art.text2art(" Caesar Cipher"))
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt :")
    text = input("Type your message :").lower()
    shift = int(input("Typethe shift number :"))
    
    if direction == "encode":
        encrypt(text,shift)
    else:
        decrypt(text,shift)
        break
  

