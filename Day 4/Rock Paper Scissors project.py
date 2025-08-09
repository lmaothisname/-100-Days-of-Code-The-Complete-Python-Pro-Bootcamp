# You are going to build a Rock, Paper, Scissors game. You will need to use what you have learnt about randomisation and Lists to achieve this.
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
game_images = [rock, paper, scissors]
player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if 0 <= player_choose <= 2:
    print(game_images[player_choose])
computer_choose = random.randint(0,2)
print("computer choose: ")
print(game_images[computer_choose])

if player_choose > 2 or player_choose < 0:
    print("You type an invalid number. You lose!")
elif player_choose == 0 and computer_choose == 2:
    print("You win!")
elif computer_choose == 0 and player_choose == 2:
    print("You lose!")
elif computer_choose > player_choose:
    print("You lose!")
elif player_choose > computer_choose:
    print("You win!")
elif computer_choose == player_choose:
    print("It's a draw.")