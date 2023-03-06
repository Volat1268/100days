import random
cards = [11, 2, 3, 4, 5, 6, 11, 8, 11, 11, 11, 11, 10]
user_cards = []
computer_cards = []

while sum(computer_cards) <= 16:
    computer_cards.append(random.choice(cards))
    print(computer_cards)
    if sum(computer_cards) > 21 and 11 in computer_cards:
        index_of_11 = computer_cards.index(11)
        computer_cards[index_of_11] = 1
    print(computer_cards)
print(f"summa = {sum(computer_cards)}")

