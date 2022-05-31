# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
character1 = ['t', 'r', 'u', 'e']
character2 = ['l', 'o', 'v', 'e']

counter1 = [] # r u u e e
counter2 = [] # u e r

score1 = 0
score2 = 0

for char in name1.lower():
    if char in character1:
        counter1.append(char)
        score1 += 1

for char in name1.lower():
    if char in character2:
        counter2.append(char)
        score2 += 1

for char in name2.lower():
    if char in character1:
        counter1.append(char)
        score1 += 1

for char in name2.lower():
    if char in character2:
        counter2.append(char)
        score2 += 1

total = int(str(score1) + str(score2))

if total <= 10 or total >= 90:
    print(f'Your score is {total}, you go together like coke and mentos.')

elif total > 40 and total < 50:
    print(f'Your score is {total}, you are alright together.')

else:
    print(f'Your score is {total}.')