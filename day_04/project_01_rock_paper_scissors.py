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

player_choice = int(input('What do you choose?\n 0 for Rock\n1 for Paper\n2 for Scissors\n'))

# Looping until user enter invalid input
while player_choice > 2 or player_choice < 0:
    player_choice = int(input("enter valid input: "))

computer_choices = [rock, paper, scissors]
computer_choice = random.choice(computer_choices)

# Assign label to player_choice value and conduct comparison check for rock
if player_choice == 0:
    player_choice = rock
    if player_choice == computer_choice:
        print(f'Draw! Both players selected {player_choice} ')
    elif player_choice == rock:
        if computer_choice == paper:
            print(f'Sorry! But {computer_choice} beats {player_choice}')
        else:
            print(f'Boom! {player_choice} smashes {computer_choice}')

# Assign label to player_choice value and conduct comparison check for paper
if player_choice == 1:
    player_choice = paper
    if player_choice == computer_choice:
        print(f'Draw! Both players selected {player_choice} ')
    elif player_choice == paper:
        if computer_choice == scissors:
            print(f'Sorry! But {computer_choice} beats {player_choice}')
        else:
            print(f'Boom! {player_choice} smashes {computer_choice}')

# Assign label to player_choice value and conduct comparison check for scissors
if player_choice == 2:
    player_choice = scissors
    if player_choice == computer_choice:
        print(f'Draw! Both players selected {player_choice} ')
    elif player_choice == scissors:
        if computer_choice == rock:
            print(f'Sorry! But {computer_choice} beats {player_choice}')
        else:
            print(f'Boom! {player_choice} smashes {computer_choice}')
