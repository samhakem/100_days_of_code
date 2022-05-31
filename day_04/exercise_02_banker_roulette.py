import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Get total number of names in list
num_items = len(names)

# Using randint select index value minus 1: generate a number between 0 and last item  ie 5 items means 1 less
random_choice = random.randint(0, num_items - 1)
person = names[random_choice]
print(person + ' is going to buy the meal today!')
