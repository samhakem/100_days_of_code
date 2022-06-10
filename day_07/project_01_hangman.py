# Hangman V2

# Start
# Execute code start

# Imports
import random

# Welcome message
print('Welcome to Hangman!')

# Word list
word_list = ['aardvark', 'baboon', 'camel']

# Randomly choose a word
chosen_word = random.choice(word_list)

# Testing
print(f'For testing purposes, the chosen word is: {chosen_word}')

# Create and empty list called display
display = []

for i in range(len(chosen_word)):
    display.append('_')

print(display, sep='', end='\n')

# Ask the user to guess a letter
guess = input('So then, what\'s your first letter?\n').lower()

# Is the guessed letter in the word
for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display[i] = guess
    else:
        display[i] = '_'

print(display, sep='', end='\n')
