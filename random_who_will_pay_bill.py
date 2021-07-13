import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#print(names)
length = len(names)
#print(length)
randomIndex = random.randint(0, length - 1)
print(f"{names[randomIndex]} is going to buy the meal today!")
