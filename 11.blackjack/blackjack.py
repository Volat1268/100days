import random
from art import logo


# -------------------------------my functions-----------------------------------------
def first_two_cards(deck, player):
    """из колоды (deck) игроку (player) выдается 2 карты"""
    for card in range(2):
        player.append(random.choice(cards))
    if player.count(11) > 1:
        player[1] = 1
    return player


# ----------------------------------------------------------------------------------------
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

should_start = input("Do you wont to play game of Blackjack? Type 'y' or 'n': ").lower()
if should_start == 'n':
    print("I'm sorry you gave up on the game. I'm waiting for you again.")
else:
    # print(logo)
    two_cards_player = first_two_cards(cards, user_cards)
    two_cards_computer = first_two_cards(cards, computer_cards)
    if sum(two_cards_computer) == 21:
        print(
            f"Your cards: {two_cards_player}, current score: {sum(two_cards_player)}\n"
            f"Computer's cards: {two_cards_computer}, current score: 21.\n Computer has blackjack. You lose!"
              )
    else:
        user_cards = two_cards_player
        computer_cards = two_cards_computer
        print(
            f"Your cards: {user_cards}, current score: {sum(user_cards)}\n"
            f"Computer's first card: {computer_cards[0]}")
        cards_more = True
        while cards_more:
            one_card_more = input("Type 'y' to get another card or type 'n' to pass: ").lower()
            if one_card_more == "y":
                user_cards.append(random.choice(cards))
                print(
                    f"Your cards: {user_cards}, current score: {sum(user_cards)}\n"
                    f"Computer's first card: {computer_cards[0]}"
                )
            else:
                print("To be continue... ")
                cards_more = False


