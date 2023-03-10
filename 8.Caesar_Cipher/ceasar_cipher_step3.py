alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.


def caesar(dir, txt, shft):
    response = 'encoded'
    if dir == 'decrypt':
        alphabet.reverse()
        response = 'decoded'
    cod_text = ''
    for letter in txt:
        position = alphabet.index(letter)
        new_position = (position + shft) % len(alphabet)
        cod_text += alphabet[new_position]
    print(f'The {response} text is: {cod_text}')


caesar(dir=direction, txt=text, shft=shift)
