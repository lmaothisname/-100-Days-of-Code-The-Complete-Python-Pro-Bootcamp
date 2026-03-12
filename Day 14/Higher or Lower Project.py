# import the file and library
import random
from game_data import data
from art import logo,vs
from os import system
# define function get_data and compare_data
def get_data():
  return random.choice(data)


def compare_data(data1,data2):
  if data1["follower_count"] > data2["follower_count"]:
    return True
  else:
    return False

# initialize variable data1, score, game_status
data1 = get_data()
score = 0
game_status = True
compare_guess = None
# print logo game
print(logo)

# Make game repeatable
while game_status:
  data2 = get_data() # initialize against data
  if data1 == data2: # if the data1 and data2 get the same information
    data2 = random.choice(data)
  print(f"Compare A: {data1["name"]}, a {data1["description"]}, from {data1["country"]}") # print the information compare A
  print(vs) # print logo vs
  print(f"Against B: {data2["name"]}, a {data2["description"]}, from {data2["country"]}") # print the information against B
  user_guess = input("Who has more followers? Type 'A' or 'B': ").upper() # initialize the variable user guess to get piece data compare
  if user_guess == "A": # assign data to user_guess and compare_guess
    user_guess = data1
    compare_guess = data2
  else:
    user_guess = data2
    compare_guess = data1
  if compare_data(user_guess,compare_guess): # compare the data
    score += 1
    data1 = data2
    system("clear")
    print(logo)
    print(f"You're right! Current score: {score}.")
  else:
    system("clear")
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    game_status = False
  

