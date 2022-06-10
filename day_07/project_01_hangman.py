# Hangman

import random

# Open the words text file in read-only mode
with open('hangman_words/words.txt', 'r') as file:
    all_text = file.read()
    words = all_text.split(' ')

    hangman_words = []

print(words)
