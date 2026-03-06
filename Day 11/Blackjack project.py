import random
from os import system
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

def draw():
  """Drawn a card"""
  return random.choice(cards)

def hand_value(hand):
  score = 0
  ace_count = 0
  for c in hand:
    if c == "A":
      score += 11
      ace_count += 1
    elif c in ["J","Q","K"]:
      score += 10
    else:
      score += int(c)
  while score > 21 and ace_count > 0:
    score -= 10
    ace_count -= 1
  return score

def play_game():
  print(logo)
  player_cards = [draw(),draw()]
  dealer_cards = [draw(),draw()]

  game_over = False
  while not game_over:
    player_score =  hand_value(player_cards)
    dealer_score = hand_value(dealer_cards)
    print(f"\tYour cards: {player_cards}, current score: {player_score}")
    print(f"\tComputer's first card: {dealer_cards[0]}")
    
    if player_score == dealer_score == 21:
      print(f"\tYour final hand: {player_cards}, final score: {player_score}")
      print(f"\tComputer's final hand: {dealer_cards}, final_score: {dealer_score}")
      print("It's a draw.")
      return
    elif player_score == 21:
      print(f"\tYour final hand: {player_cards}, final score: {player_score}")
      print(f"\tComputer's final hand: {dealer_cards}, final_score: {dealer_score}")
      print("Win with a Blackjack 😎")
      return
    elif dealer_score == 21:
      print(f"\tYour final hand: {player_cards}, final score: {player_score}")
      print(f"\tComputer's final hand: {dealer_cards}, final_score: {dealer_score}")
      print("Lose, opponent has a Blackjack 😱")
      return
    else:
      hit = input("Type 'y' to get another card, type 'n' to pass:")
      if hit == "y":
        player_cards.append(draw())
      else:
        game_over = True
  
  while dealer_score != 0 and dealer_score < 16:
    dealer_cards.append(draw())
    dealer_score = hand_value(dealer_cards)
  
  print(f"\tYour final hand: {player_cards}, final score: {player_score}")
  print(f"\tComputer's final hand: {dealer_cards}, final_score: {dealer_score}")
  
  if player_score > 21:
    print("You went over. You lose 😭")
  elif dealer_score > 21:
    print("Opponent went over. You win 😁")
  elif player_score > dealer_score:
    print("You have higher score. You win! 😁")
  elif player_score < dealer_score:
    print("You have lower score. You lose! 😭")
  else:
    print("It's a draw! ")


while input("Do you want to play a game of Blackjack? type 'y' or 'n': ") == "y":
  play_game()
