from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide
}


def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    is_continue = True
    while is_continue:
        operation_symbol = input("Pick an operation: ")
        next_num = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, next_num)
        print(f'{num1} {operation_symbol} {next_num} = {answer}')
        if input(f'Type "y" to continue calculating with {answer} or type "n" to exit: ').lower() == 'y':
            num1 = answer
        else:
            is_continue = False
            calculator()


calculator()

