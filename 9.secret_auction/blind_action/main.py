from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

name = input('What is your name?: ')
bid = int(input('What is your bid?: $'))
auction = {}

is_finish = False
while not is_finish:
    other_bidders = input('Are there any others bidders? Type \'yes\' or \'no\' ')
    if other_bidders == 'yes':
        print('\n' * 50)
        name = input('What is your name?: ')
        bid = int(input('What is your bid?: $'))
        auction[name] = bid
    if other_bidders == 'no':
        is_finish = True
        winner = ''
        max_bid = 0
        for bidder in auction:
            if auction[bidder] > max_bid:
                winner = bidder
                max_bid = auction[bidder]
        print('\n' * 50)
        print(f'The winner is {winner} with a bid of ${auction[winner]}')


