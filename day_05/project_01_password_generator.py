# Password Generator Project
# import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# selected_letters = random.sample(letters, nr_letters)
# print(selected_letters)

def pick_random_letter(array: object) -> object:
    """

    :rtype: object
    :param array:
    :return:
    """
    for x in letters:
        return list(set(letters))[0: nr_letters]


def pick_random_symbols(array: object) -> object:
    """

    :rtype: object
    :param array:
    :return:
    """

    for s in symbols:
        return list(set(symbols))[0: nr_symbols]


def pick_random_numbers(array: object) -> object:
    """

    :rtype: object
    :param array:
    :return:
    """

    for n in numbers:
        return list(set(numbers))[0: nr_numbers]


password_letters = ''.join(pick_random_letter(letters))
password_symbols = ''.join(pick_random_symbols(symbols))
password_numbers = ''.join(pick_random_numbers(numbers))

print(password_letters, password_symbols, password_numbers, sep='')

# print(str(password_letters), str(password_symbols), str(password_numbers))

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
