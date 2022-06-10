# Hangman V2

# Start
# Execute code start

# Imports
import random

# Welcome message
print('Welcome to Hangman!')

# Word list
with open('hangman_words/words.txt', 'r') as f:
    word_list = f.readlines()


# Randomly choose a word
chosen_word = random.choice(word_list).lower().replace('\n', '')

# Testing
print(f'For testing purposes, the chosen word is: {chosen_word}')

# Create and empty list called display
display = []

for i in range(len(chosen_word)):
    display.append('_')

win_counter = len(display)
lose_counter = len(display)

# Is the guessed letter in the word
while win_counter > 0:
    print(display, sep='', end='\n')

    # Ask the user to guess a letter
    guess = input('So then, what\'s your letter?\n').lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i].replace('_', guess)
            display[i] = guess
            win_counter -= 1
            print(f'Counting down no. of tries at: {win_counter}')


print(f'Congrats! You finished your word: {display}')
