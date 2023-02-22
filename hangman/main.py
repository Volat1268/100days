import random
from hangman_words import words
from hangman_art import stages, logo

print(logo)
print('You have to guess the word. You have 6 lives. If you letter is not in the word, you lose one life.')
chosen_word = random.choice(words)
print(f'Pssss. randomly chosen word is "{chosen_word}"')
word_length = len(chosen_word)

encrypt_list = []
for _ in range(word_length):
    encrypt_list.append('_')
encrypted = ''.join(encrypt_list)
print(encrypted)
guess = input('Guess the letter: ').lower()
end_of_game = False
while not end_of_game:
    for i in range(word_length):

        letter = chosen_word[i]
        if guess == letter:
            encrypt_list[i] = guess
print(encrypt_list)


