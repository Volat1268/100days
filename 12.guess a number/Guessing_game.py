import random
from art import logo
# print(logo)


def check_difficulty():
    """в зависимости от ответа пользователя
    определяет количество попыток у игрока"""
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if diff == 'hard':
        return 5
    else:
        return 10


def check_answer(corr_nmb, user_nmb, turns):
    if user_nmb < corr_nmb:
        print("Too low")
        return turns - 1
    elif user_nmb > corr_nmb:
        print("Too high")
        return turns - 1
    else:
        print(f"You got it! The answer was {corr_nmb}")


print("Welcome to the Number guessing Game!")
print("I'm thinking of a number between 1 and 100.")
correct_answer = random.randint(1, 100)
print(f"Psssst, the correct answer is {correct_answer}.")
level = check_difficulty()
while correct_answer != correct_answer:
    guess = int(input("Make a guess: "))
    level = check_answer(correct_answer, guess, level)



