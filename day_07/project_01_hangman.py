# Hangman V2

# Start
# Execute code start

# Imports
import random

# Welcome message
print('Welcome to Hangman!')

# Word list
word_list = ['aardvark','baboon', 'camel']

# Randomly choose a word
chosen_word = random.choice(word_list)

# Ask the user to guess a letter
guess = input('So, Sophie, what\'s your first letter?\n').lower()

# Is the guessed letter in the word
for letter in chosen_word:
    if letter == guess:
        print('Correct!')
    else:
        print('Wrong :\'(')
