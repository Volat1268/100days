import random


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
    elif sum(two_cards_player) == 21 and sum(two_cards_computer) != 21:
        print(
            f"Your cards: {two_cards_player}, current score: {sum(two_cards_player)}\n"
            f"Computer's cards: {two_cards_computer}, current score: {sum(two_cards_computer)}.\n"
            f" You have blackjack. You win!"
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
                # 1 вариант: если у игрока перебор, сообщаем ему, что он проиграл.
                if sum(user_cards) > 21:
                    print(
                        f"Your cards: {user_cards}, current score: {sum(user_cards)}\n"
                        f"Computer's first card: {computer_cards[0]}"
                          )
                    print(
                        f"Your final hand: {user_cards}, final score: {sum(user_cards)}\n"
                        f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}\n"
                        f"You went over. You lose!"
                    )
                    cards_more = False
                # 2 вариант: если у игрока ровно 21, компьютер набирает дополнительные карты, и здесь свои варианты:
                elif sum(user_cards) == 21:
                    while sum(computer_cards) <= 16:
                        computer_cards.append(random.choice(cards))
                    #  2.1. у компьютера тоже ровно 21: (сообщаем, что компьютер выиграл)
                    if sum(computer_cards) == 21:
                        print(
                            f"Your cards: {user_cards}, final score: {sum(user_cards)}\n"
                            f"Computer's cards: {computer_cards}, final score: {sum(computer_cards)}.\n "
                            f"Computer has blackjack. You lose!"
                        )
                    # 2.2. у компьютера перебор: (сообщаем, что у компьютера перебор, и игрок выиграл)
                    elif sum(computer_cards) > 21:
                        print(
                            f"Your cards: {user_cards}, final score: {sum(user_cards)}\n"
                            f"Computer's cards: {computer_cards}, final score: {sum(computer_cards)}.\n "
                            f"Opponent went over. You win!"
                        )
                    # 2.3. у компьютера меньше 21: (сообщаем, что игрок выиграл)
                    else:
                        print(
                            f"Your final hand: {user_cards}, final score: {sum(user_cards)}\n"
                            f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}\n"
                            f"You have blackjack. You win!"
                        )
                    cards_more = False
                # 3 вариант: если у игрока меньше 21, предлагаем ему выбрать, будет ли брать еще одну карту.
                else:
                    print(
                        f"Your cards: {user_cards}, current score: {sum(user_cards)}\n"
                        f"Computer's first card: {computer_cards[0]}"
                    )
            else:
                # если игрок отказывается брать еще одну карту:
                # компьютер добирает карты, пока у него сумма меньше 16:
                while sum(computer_cards) <= 16:
                    computer_cards.append(random.choice(cards))
                # подвариант 1: компьютер набрал 21:
                if sum(computer_cards) == 21:
                    print(
                        f"Your cards: {user_cards}, final score: {sum(user_cards)}\n"
                        f"Computer's cards: {computer_cards}, final score: {sum(computer_cards)}.\n "
                        f"Computer has blackjack. You lose!"
                    )
                # подвариант 2: у компьютера перебор: (сообщаем, что у компьютера перебор, и игрок выиграл)
                elif sum(computer_cards) > 21:
                    print(
                        f"Your cards: {user_cards}, final score: {sum(user_cards)}\n"
                        f"Computer's cards: {computer_cards}, final score: {sum(computer_cards)}.\n "
                        f"Opponent went over. You win!"
                    )
                # подвариант 3: у компьютера меньше 21:
                else:
                    # 3.1. у игрока сумма больше:
                    if sum(user_cards) > sum(computer_cards):
                        print(
                            f"Your final hand: {user_cards}, final score: {sum(user_cards)}\n"
                            f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}\n"
                            f" You win!"
                        )
                    # 3.2. у компьютера сумма больше:
                    elif sum(user_cards) < sum(computer_cards):
                        print(
                            f"Your final hand: {user_cards}, final score: {sum(user_cards)}\n"
                            f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}\n"
                            f" Opponent wins!"
                        )
                    else:
                       print(
                            f"Your final hand: {user_cards}, final score: {sum(user_cards)}\n"
                            f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}\n"
                            f" It's draw!"
                        )



 print(logo)
    two_cards_player = first_two_cards(cards, user_cards)
    two_cards_computer = first_two_cards(cards, computer_cards)
    if sum(two_cards_computer) == 21:
        print(
            f"Your cards: {two_cards_player}, current score: {sum(two_cards_player)}\n"
            f"Computer's cards: {two_cards_computer}, current score: 21.\n Computer has blackjack. You lose!"
        )
    elif sum(two_cards_player) == 21 and sum(two_cards_computer) != 21:
        print(
            f"Your cards: {two_cards_player}, current score: {sum(two_cards_player)}\n"
            f"Computer's cards: {two_cards_computer}, current score: {sum(two_cards_computer)}.\n"
            f" You have blackjack. You win!"
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
            if one_card_more == "n":
                # если игрок отказывается брать еще одну карту:
                # компьютер добирает карты, пока у него сумма меньше 16:
                while sum(computer_cards) <= 16:
                    computer_cards.append(random.choice(cards))
                    # решаем вопрос туза: если сумма с тузом становится больше 21, то туз = 1
                    if sum(computer_cards) > 21 and 11 in computer_cards:
                        index_of_11 = computer_cards.index(11)
                        computer_cards[index_of_11] = 1
                # подвариант 1: компьютер набрал 21:
                if sum(computer_cards) == 21:
                    print(
                        f"Your cards: {user_cards}, final score: {sum(user_cards)}\n"
                        f"Computer's cards: {computer_cards}, final score: {sum(computer_cards)}.\n"
                        f"Computer has blackjack. You lose!"
                    )
                # подвариант 2: у компьютера перебор: (сообщаем, что у компьютера перебор, и игрок выиграл)
                elif sum(computer_cards) > 21:
                    print(
                        f"Your cards: {user_cards}, final score: {sum(user_cards)}\n"
                        f"Computer's cards: {computer_cards}, final score: {sum(computer_cards)}.\n"
                        f"Opponent went over. You win!"
                    )
                # подвариант 3: у компьютера меньше 21:
                else:
                    # 3.1. у игрока сумма больше:
                    if sum(user_cards) > sum(computer_cards):
                        print(
                            f"Your final hand: {user_cards}, final score: {sum(user_cards)}\n"
                            f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}\n"
                            f"You win!"
                        )
                    # 3.2. у компьютера сумма больше:
                    elif sum(user_cards) < sum(computer_cards):
                        print(
                            f"Your final hand: {user_cards}, final score: {sum(user_cards)}\n"
                            f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}\n"
                            f"Opponent wins!"
                        )
                    else:
                        print(
                            f"Your final hand: {user_cards}, final score: {sum(user_cards)}\n"
                            f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}\n"
                            f"It's draw!"
                        )
                cards_more = False
            elif one_card_more == "y":
                user_cards.append(random.choice(cards))
                # решаем вопрос туза: если сумма с тузом становится больше 21, то туз = 1
                if sum(user_cards) > 21 and 11 in user_cards:
                    index_of_11 = user_cards.index(11)
                    user_cards[index_of_11] = 1
                # 1 вариант: если у игрока перебор, сообщаем ему, что он проиграл.
                if sum(user_cards) > 21:
                    print(
                        f"Your cards: {user_cards}, current score: {sum(user_cards)}\n"
                        f"Computer's first card: {computer_cards[0]}"
                    )
                    print(
                        f"Your final hand: {user_cards}, final score: {sum(user_cards)}\n"
                        f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}\n"
                        f"You went over. You lose!"
                    )
                    cards_more = False
                # 2 вариант: если у игрока ровно 21, компьютер набирает дополнительные карты, и здесь свои варианты:
                elif sum(user_cards) == 21:
                    while sum(computer_cards) <= 16:
                        computer_cards.append(random.choice(cards))
                    #  2.1. у компьютера тоже ровно 21: (сообщаем, что компьютер выиграл)
                    if sum(computer_cards) == 21:
                        print(
                            f"Your cards: {user_cards}, final score: {sum(user_cards)}\n"
                            f"Computer's cards: {computer_cards}, final score: {sum(computer_cards)}.\n "
                            f"Computer has blackjack. You lose!"
                        )
                    # 2.2. у компьютера перебор: (сообщаем, что у компьютера перебор, и игрок выиграл)
                    elif sum(computer_cards) > 21:
                        print(
                            f"Your cards: {user_cards}, final score: {sum(user_cards)}\n"
                            f"Computer's cards: {computer_cards}, final score: {sum(computer_cards)}.\n"
                            f"Opponent went over. You win!"
                        )
                    # 2.3. у компьютера меньше 21: (сообщаем, что игрок выиграл)
                    else:
                        print(
                            f"Your final hand: {user_cards}, final score: {sum(user_cards)}\n"
                            f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}\n"
                            f"You have blackjack. You win!"
                        )
                    cards_more = False
                # 3 вариант: если у игрока меньше 21, предлагаем ему выбрать, будет ли брать еще одну карту.
                else:
                    print(
                        f"Your cards: {user_cards}, current score: {sum(user_cards)}\n"
                        f"Computer's first card: {computer_cards[0]}"
                    )
