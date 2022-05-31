# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#print(int(float(weight,)) / int(float(height) ** 2))

bmi = float(weight) / float(height)**2

bmi_int = int(bmi)

print(round(bmi))