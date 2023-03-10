import random
from art import logo


def guess_number():
<<<<<<< HEAD
    correct_number = random.randint(1, 100)
=======
    correct_number = random.choice(guess_numbers)
>>>>>>> bee19af0c2d9828e166a1d9375731f844bc47826
    print("I'm thinking of a number between 1 and 100.")
    print(f"Pssst, the correct number is {correct_number}")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'hard':
        attempts = 5
    else:
        attempts = 10
    guessing(attempts, correct_number)


def guessing(n, number):
    should_continue = True
    while n > 0 and should_continue:
        print(f"You have {n} attempts to guess the number.")
        response = int(input("Make a guess: "))
        if response > number:
            n -= 1
            print("Too high.")
            if n > 0:
                print("Guess again.")
            else:
                print("You've run out of guesses, you lose.")
        elif response < number:
            n -= 1
            print("Too low.")
            if n > 0:
                print("Guess again.")
            else:
                print("You've run out of guesses, you lose.")
        else:
            print(f"You got it! The answer was {number}. You win!")
            should_continue = False


should_play_continue = True
while should_play_continue:
    print(logo)
    print("Welcome to the Guessing Numbers game!")
<<<<<<< HEAD
=======
    guess_numbers = list(range(1, 101))
>>>>>>> bee19af0c2d9828e166a1d9375731f844bc47826
    guess_number()
    players_answer = input("\nDo you want to guess again? Type 'yes' or 'no' ")
    if players_answer == 'no':
        print("Ok. We will miss you.")
        should_play_continue = False




