# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
leap = int(year)
if leap % 4 == 0:
    print('Leap year.')
elif leap % 100 == 0:
    print('Not leap year')
elif leap % 400 == 0:
    print('Not leap yer.')
else:
    print('Not leap year.')