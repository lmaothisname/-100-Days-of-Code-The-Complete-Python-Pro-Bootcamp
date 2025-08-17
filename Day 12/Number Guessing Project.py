#ToDo 1: print a logo and the welcome word
import random
logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
computer_number = 36
choose_game_mode = input("Choose a difficulty.Type 'easy' or 'hard': ")
attempts = 0
if choose_game_mode == "easy":
    attempts = 10
else:
    attempts = 5
def compare(p1,p2):
    if p2 > p1:
        return "Too high.\nGuess again."
    elif p2 < p1:
        return "Too low.\nGuess again."
    else:
        return False
status = True
while status:
    print(f"You have {attempts} attempts remaining to guess the number.")
    player_number = int(input("Make a guess: "))
    guess = compare(computer_number,player_number)
    if guess == False:
        print(f"You got it! The answer was {computer_number}.")
        break
    elif guess != False and attempts == 1:
        print("You've run out of guesses.")
        break
    else:
        print(guess)
        status = True
    attempts -= 1




