import random
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
    """Take a card"""
    return random.choice(cards)

def hand_value(card):
    """sum of their score of card"""
    total = 0
    ace = 0
    for c in card:
        if c == "A":
            total += 11
            ace += 1
        elif c in ('J',"Q","K","A"):
            total += 10
        else:
            total += int(c)
    #Down value of ace from 11 to 1 if greater than 21:
    while total > 21 and ace:
        total -= 10
        ace -= 1
    return total

ask_player = input("Do you want to play a game of Blackjack? type 'y' or 'n': ")
while ask_player == "y":
    print(logo)
    player = [draw(),draw()]
    dealer = [draw()]

    #player turn
    while True:
        p_score = hand_value(player)
        print(f"\t  Your card: {player}, current score: {p_score}")
        print(f"\t  Computer's first card: {dealer}")
        if p_score == 21:
            break
        hit = input("Type 'y' to get another card, type 'n' to pass: ")
        if hit == "y":
            player.append(draw())
            if hand_value(player) > 21:
                break
        else:
            break
    
    #computer turn, draw a card when greater than 17
    while hand_value(dealer) < 17:
        dealer.append(draw())
    p_score = hand_value(player)
    d_score = hand_value(dealer)
    print(f"\tYour final hand: {player}, final score: {p_score}")
    print(f"\tComputer's final hand: {dealer} , final score: {d_score}")
    if p_score > 21:
        print("You went over. You lose (╥﹏╥)")
    elif d_score > 21:
        print("Opponent went over. You win (^_^)")
    elif p_score > d_score:
        print("Opponent went over. You win (^_^)")
    elif p_score < d_score:
        print("You went over. You lose (╥﹏╥)")
    else:
        print("Draw!")
    ask_player = input("Do you want to play a game of Blackjack? type 'y' or 'n': ")