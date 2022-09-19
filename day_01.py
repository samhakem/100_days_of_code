# Day 01
# Print statements

# Prints a string into the console. print("Hello World")

print('Im a string')  # Print something in the parentheses using quotation marks to delineate a string

# Error handling

# print('Im an error!)  # Syntax highlighting error using an underline

# print('Im an error)  # Example of a missing quotation mark and its relevant syntax error
#           ^
# SyntaxError: unterminated string literal (detected at line 10)

# Exercise 01
# These are the notes from the previous lesson.
print('Day 1 - Python Print Function')
print('The function is declared like this:')
print("print('what to print')")

# Print to a new line \n
print('This is how\n')
print('You print to a new line')

# Multi print lines with one statement, no spaces between the \n is important
print('A line\nand another line\nand yet another.')

# String concatenation
print('4' + '2')

string_1 = '4'
string_2 = '2'

print(string_1 + string_2)

# With added spaces
print('An example of a' + ' ' + 'space.')

# Indentation error

# print('Im an indentation error')
# print('Im an indentation error')
# IndentationError: unexpected indent

# Fix the code below 👇

# print(Day 1 - String Manipulation")
# print("String Concatenation is done with the "+" sign.")
#   print('e.g. print("Hello " + "world")')
# print(("New lines can be created with a backslash and n.")

# Fixed code

print('Day 1 - String Manipulation')
print('String Concatenation is done with the' + 'sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# Python input function
# Input is a built-in function with the prompt in the quotes within the parentheses
# Once run, a sold/flashing cursor will appear awaiting human input
input('What is your name?')

print('Hello user' + input('What is your name?\n'))  # \n tidies up the response line to a new line

# Write a program that prints the number of characters in a user's name.
# You might need to Google for a function that
# calculates the length of a string.

name_length = input('What is your name?')
print(len(name_length))

# Variables

# Variable assignment
# A variable is a placeholder with
# a certain name, type and value.

# Examples
#
# ■ Convention: Variable names should be short,
# descriptive and in lower letters. Multiple words
# should be separated by an _ underscore.
#
# > name0 = 'Franz'
# > age = 20
# > shoe_size = 3.5
# > is_clever = True
# > diff = age - 18

# Please remember for now:
# ■ Variable names are only allowed
# to contain alphanumeric
# characters and underscores.
# ■ The first character must not
# be a number!
# ■ There are some reserved
# keywords that can’t be used
# (e.g. if, for, while, return, ...)

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
c = a
a = b
b = c

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)