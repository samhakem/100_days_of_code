# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))


# Eazy Level - Order not randomised: Randomised anyway
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password_easy = ''  # Declare an empty string

# Non-inclusive end of slice, hence plus 1 to reach input no.
# Iterate over range starting at 1, up to input no.
# Take empty string, increment random choice of string, integer, symbol into it with +=
for char in range(1, nr_letters + 1):
    password_easy += random.choice(letters)

for num in range(1, nr_numbers + 1):
    password_easy += random.choice(numbers)

for sym in range(1, nr_symbols + 1):
    password_easy += random.choice(symbols)

# Join, shuffle and print using length of now filled string
print(''.join(random.sample(password_easy, len(password_easy))))

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_hard = []

for char in range(1, nr_letters + 1):
    password_hard.append(random.choice(letters))

for num in range(1, nr_numbers + 1):
    password_hard.append(random.choice(numbers))

for sym in range(1, nr_symbols + 1):
    password_hard.append(random.choice(symbols))

random.shuffle(password_hard)

password = ''

for char in password_hard:
    password += char

print(f'Your password is: {password}')

# Function based solution using doc strings and parameter tagging

def pick_random_letter(array: object) -> object:
    """

    :rtype: object
    :param array:
    :return: list:
    """
    for x in letters:
        return list(set(letters))[0: nr_letters]


def pick_random_symbols(array: object) -> object:
    """

    :rtype: object
    :param array:
    :return: list:
    """

    for s in symbols:
        return list(set(symbols))[0: nr_symbols]


def pick_random_numbers(array: object) -> object:
    """

    :rtype: object
    :param array:
    :return: list:
    """

    for n in numbers:
        return list(set(numbers))[0: nr_numbers]


password_letters = ''.join(pick_random_letter(letters))
password_symbols = ''.join(pick_random_symbols(symbols))
password_numbers = ''.join(pick_random_numbers(numbers))

final_password = password_letters + password_symbols + password_numbers

print(''.join(random.sample(final_password, len(final_password))))
