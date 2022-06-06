# For Loop

# for item in list_of_items:
     # Do something to each item

# fruits = ['Apple', 'Peach', 'Pear']

# Code block loops 3 times due to number of strings in list, then outside block print(fruits) prints once
# for fruit in fruits:
#     print('has no ' + fruit + ' in it.')
#     print(fruit + ' pie')
# print(fruits)

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0
for heights in student_heights:
    total_height += heights

number = 0
for nums in student_heights:
    number += 1

print(round(total_height / number))
