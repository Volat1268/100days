import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

player_choice = int(input('What do your choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
comp_choice = random.randint(0, 2)


if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
else:
    print(scissors)
print('Computer chose:')
if comp_choice == 0:
    print(rock)
elif comp_choice == 1:
    print(paper)
else:
    print(scissors)

if (player_choice == 0 and comp_choice == 1) or (player_choice == 1 and comp_choice == 2) or (
        player_choice == 2 and comp_choice == 0):
    result = 'You lose'
elif player_choice == comp_choice:
    result = 'Draw'
else:
    result = 'You win!'

print(result)