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

game_attr = [rock, paper, scissors]
user_choice = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(game_attr[user_choice])
computer_choice = random.randint(0,2)
print("computer_chose:")
print(game_attr[computer_choice])
if user_choice >= 3 or user_choice <0:
  print("Please enter valid number, 0, 1, or 2")
else:
  if user_choice == computer_choice:
    print("It's a draw")
  elif user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose!")  
  elif user_choice < computer_choice:
    print("You lose!")
  elif user_choice > computer_choice:
    print("You win!")  
