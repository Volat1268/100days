from art import logo

# TODO-1: Import and print the logo from art.py when the program starts.
# TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26.
# Hint: Think about how you can use the modulus (%).
# TODO-3: What happens if the user enters a number/symbol/space?
# Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.


print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]


def caesar(cod_direction, user_text, shift_amount):
    response = 'encoded'
    if cod_direction == 'decrypt':
        alphabet.reverse()
        response = 'decoded'
    finish_text = ''
    for char in user_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % len(alphabet)
            finish_text += alphabet[new_position]
        else:
            finish_text += char
    print(f'The {response} text is: {finish_text}')


is_finish = False
while not is_finish:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(cod_direction=direction, user_text=text, shift_amount=shift)
    response_about_finish = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if response_about_finish == 'no':
        is_finish = True
