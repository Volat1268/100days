import random
from hangman_words import words
from hangman_art import stages, logo, smile, death

print(logo)
print('You have to guess the word. You have 6 lives. If you letter is not in the word, you lose one life.')
chosen_word = random.choice(words)
print(f'Pssss. randomly chosen word is "{chosen_word}"')
word_length = len(chosen_word)

encrypt_list = []
for _ in range(word_length):
    encrypt_list.append('_')


lives = 6
end_of_game = False
while not end_of_game:
    encrypted = ''.join(encrypt_list)
    print(encrypted)
    guess = input('Guess the letter: ').lower()
    if guess in encrypt_list:
        print('You guessed this letter before.')
    for i in range(word_length):
        letter = chosen_word[i]
        if guess == letter:
            encrypt_list[i] = guess
    if guess not in chosen_word:
        print(f'You guess "{guess}" it is not in the word. You lose one life.')
        print(stages[lives])
        lives -= 1
    if lives == 0:
        end_of_game = True
        print('You lose. Gave over.')
        print(death)
    if '_' not in encrypt_list:
        print('\nYou win. Game over.')
        print(smile)
        end_of_game = True



