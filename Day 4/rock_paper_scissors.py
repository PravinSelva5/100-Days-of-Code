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

import random

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n")
computer_choice = random.randint(0,2)

if player_choice == '0':
  print(rock)
elif player_choice == '1':
  print(paper)
else:
  print(scissors)

# Computer decision
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
else:
  print(scissors)

# Winning Logic
if player_choice >= '3' or player_choice < '0':
  print("You typed an invalid number, you lose!")
elif player_choice == '0' and computer_choice == 2:
  print("You win")
elif player_choice == '1' and computer_choice == 0:
  print("You win")
elif player_choice == '2' and computer_choice == 1:
  print("You win")
else:
  print("You lose")

