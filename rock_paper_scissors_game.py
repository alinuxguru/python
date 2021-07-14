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

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors" ))
#print(type(choose))
list = ["rock", "paper", "scissors"]
if choose == 0:
  #human_chose = "rock"
  human_chose = list[choose]
  print(rock)
elif choose == 1:
  human_chose = list[choose]
  #human_chose = "paper"
  print(paper)
else:
  human_chose = list[len(list) - 1]
  print(scissors)
  #print(scissors) 
  #human_chose = "scissors"   
  
# print(map[0])
print("Computer Chose:")

#print(list)
randomIndex = random.randint(0, len(list) - 1)
computer_chose = list[randomIndex]
#print(computer_chose)
if computer_chose == "rock":
  print(rock)
elif computer_chose == "paper":
  print(paper)
else:
  print(scissors)    
#print(human_chose)
#print(type(computer_chose))
#print(list[randomIndex])
#print(rock)
#print(type(human_chose))

if human_chose == computer_chose:
  print("It's Tie")
elif (human_chose == "rock") and (computer_chose == "scissors"):
  print("You Won!")
elif (human_chose == "scissors") and (computer_chose == "paper"):
  print("You Won!")
elif (human_chose == "paper") and (computer_chose == "rock"):
  print("You Won!")

elif (computer_chose == "rock") and (human_chose == "scissors"):
  print("You lose!")
elif (computer_chose == "scissors") and (human_chose == "paper"):
  print("You lose!")  
elif (computer_chose == "paper") and (human_chose == "rock"):
  print("You lose!")  
else:
  print("Try again")
