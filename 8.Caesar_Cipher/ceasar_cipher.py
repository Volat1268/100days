alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in
# the alphabet by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able
# to test the code and encrypt a message.


def encrypt(encr_text, encr_shift):
    encoded_text = ''
    for letter in encr_text:
        index = alphabet.index(letter)
        new_index = index + encr_shift
        encoded_text += alphabet[new_index % len(alphabet)]
    print(f'The encoded text is: {encoded_text}.')


def decrypt(decr_text, decr_shift):
    decoded_text = ''
    alphabet.reverse()
    for letter in decr_text:
        position = alphabet.index(letter)
        new_position = (position + decr_shift) % len(alphabet)
        decoded_text += alphabet[new_position]
    print(f'The decoded text is: {decoded_text}')


#TODO-1: Create a different function called 'decrypt' that takes the
# 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the
# 'text' *backwards* in the alphabet by the shift amount and print
# the decrypted text.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"

#TODO-3: Check if the user wanted to encrypt or decrypt the message
# by checking the 'direction' variable. Then call the correct function
# based on that 'drection' variable. You should be able to test the code
# to encrypt *AND* decrypt a message.

if direction == 'encrypt':
    encrypt(encr_text=text, encr_shift=shift)
elif direction == 'decrypt':
    decrypt(decr_text=text, decr_shift=shift)
else:
    print('Check your answer.')
