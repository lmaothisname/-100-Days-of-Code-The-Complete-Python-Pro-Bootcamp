logo = r"""

        88                                                              
  ,d    ""              ,d                            ,d                
  88                    88                            88                
MM88MMM 88  ,adPPYba, MM88MMM ,adPPYYba,  ,adPPYba, MM88MMM ,adPPYba,   ,adPPYba,
  88    88 a8"     ""   88    ""     `Y8 a8"     ""   88   a8"     "8a a8P_____88
  88    88 8b           88    ,adPPPPP88 8b           88   8b       d8 8PP"""""""
  88,   88 "8a,   ,aa   88,   88,    ,88 "8a,   ,aa   88,  "8a,   ,a8" "8b,   ,aa 
  "Y888 88  `"Ybbd8"'   "Y888 `"8bbdP"Y8  `"Ybbd8"'   "Y888 `"YbbdP"'   `"Ybbd8"'                                                                       
            
"""

WINING_COMBOS = [
  (0,1,2), (3,4,5), (6,7,8),
  (0,3,6), (1,4,7), (2,5,8),
  (0,4,8), (2,4,6)
]

# step 1: Initialize the Board & Display it
def print_board(board):
  print(f"\n {board[0]} | {board[1]} | {board[2]} ")
  print("---+---+---")
  print(f"\n {board[3]} | {board[4]} | {board[5]} ")
  print("---+---+---")
  print(f"\n {board[6]} | {board[7]} | {board[8]} ")
  
# step 2: Handle player move & validation
def get_player_move(board, player):
  choice = input(f"Player {player}, enter your move (1-9): ").strip()
  if choice.isdigit() and 1 <= int(choice) <= 9:
    position = int(choice) - 1 # conver to 0-based index
    if board[position] == " ":
      return position
    else:
      print("That spot is already taken! Choose another.")
  else:
    print("Invalid input. Please enter a number from 1 to 9.")  
    
# step 3: check win and draw conditions

def check_win(board, player):
  for combo in WINING_COMBOS:
    if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
      return True
  return False

def check_draw(board):
  return " " not in board

# step 4: the main game loop
def play_game():
  board = [' '] * 9
  current_player = 'X'
  
  print(logo)
  print_board([str(i+1) for i in range(9)])
  while True:
    move = get_player_move(board,current_player)
    board[move] = current_player
    print_board(board)
    if check_win(board,current_player):
      print(f"🎉 Congratulations! Player {current_player} wins! 🎉\n")
      break
    
    if check_draw(board):
      print("🤝 It's a draw!\n")
      break
    
    current_player = 'O' if current_player == 'X' else 'X'
    
def main():
  while True:
    play_game()
    replay =  input("Play again? (y/n): ").strip().lower()
    if replay != 'y':
      print("Thanks for playing!")
      break

if __name__ == "__main__":
  main()