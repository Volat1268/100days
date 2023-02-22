import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the my PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

rand_letters_ind = []
for ind in range(nr_letters):
  rand_letters_ind.append(random.randint(0, len(letters)))

rand_numbers_ind = []
for number in range(nr_numbers):
  rand_numbers_ind.append(random.randint(0, len(numbers)))

rand_symbols_ind = []
for symbol in range(nr_symbols):
  rand_symbols_ind.append(random.randint(0, len(symbols)))

# your_password = ''
# for ind in rand_letters_ind:
#   your_password += letters[ind]
# for ind in rand_symbols_ind:
#   your_password += symbols[ind]
# for ind in rand_numbers_ind:
#   your_password += numbers[ind]

your_password = []
for ind in rand_letters_ind:
  your_password.append(letters[ind])
for ind in rand_symbols_ind:
  your_password.append(symbols[ind])
for ind in rand_numbers_ind:
  your_password.append(numbers[ind])

random.shuffle(your_password)
for i in your_password:
    print(i,end='')

# print(your_hard_password)
