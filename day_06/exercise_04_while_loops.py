# While loop

while something_is_true:
    # Do something repeatedly

# https://reeborg.ca/

def jump_1():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_hurdles = 4
while number_of_hurdles > 0:
    jump_1()
    number_of_hurdles -= 1
    print(number_of_hurdles)

