logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def cipher():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    encoded_text = ''
    decrypted_text = ''
    if direction == 'encode':
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        for letter in text:
            # print(letter)
            if letter.lower() in alphabet:
                index = alphabet.index(letter.lower())
                shift_position = (index+shift)
                shift_position %= len(alphabet)
                code = alphabet[shift_position]
                # print(alphabet[index])
                if alphabet[index] == letter:
                    encoded_text += code
                else:
                    encoded_text += code.upper()
            elif not letter in alphabet:
                encoded_text += letter
        print(encoded_text)
    elif direction == 'decode':
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        if len(text) == 0:
            print("There's no message to decrypt yet. Type 'encode' to write a message")
        else:
            for letter in text:
                if letter.lower() in alphabet:
                    index = alphabet.index(letter.lower())
                    shift_position = (index - shift)
                    shift_position %= len(alphabet)
                    code = alphabet[shift_position]
                    if alphabet[index] == letter:
                        decrypted_text += code
                    else:
                        decrypted_text += code.upper()
                elif not letter in alphabet:
                    decrypted_text += letter
            print(decrypted_text)
    else:
        print("Your input is not valid!")

##########################################
#Try out Ceaser Cipher Game below!
##########################################
print(logo)
should_continue = True
while should_continue:
    cipher()
    continue_or_not = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n")
    if not continue_or_not == 'yes':
        should_continue = False
        print("Good Bye!")

