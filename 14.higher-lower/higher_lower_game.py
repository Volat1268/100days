import random
from art import logo, vs
from game_data import data


def choice_option():
    random_choice = random.randint(0, data_qnt-1)
    name = data[random_choice]['name']
    description = data[random_choice]['description']
    country = data[random_choice]['country']
    follower_count = data[random_choice]['follower_count']
    option = [name, description, country, follower_count]
    return option


data_qnt = len(data)
option_a = choice_option()
option_b = choice_option()
score = 0
print(logo)
is_stop = False
while not is_stop:
    if score > 0:
        print(f"You're right! Current score: {score}")
    print(f"\nCompare A: {option_a[0]}, a {option_a[1]}, from {option_a[2]}")
    print(vs)
    print(f"Against B: {option_b[0]}, a {option_b[1]}, from {option_b[2]}")
    print(f"pssst. A: {option_a[3]} , B: {option_b[3]}")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if option_a[3] > option_b[3] and answer == "a" or option_a[3] < option_b[3] and answer == "b":
        score += 1
        option_a = option_b
        option_b = choice_option()
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        is_stop = True



