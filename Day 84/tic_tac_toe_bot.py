import time
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
  print(f" {board[3]} | {board[4]} | {board[5]} ")
  print("---+---+---")
  print(f" {board[6]} | {board[7]} | {board[8]} \n")
  
# step 2: Handle player move & validation
def get_human_move(board, player):
  while True:
    choice = input(f"Player {player}, enter your move (1-9): ").strip()
    if choice.isdigit() and 1 <= int(choice) <= 9:
      position = int(choice) - 1 # convert to 0-based index
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

# implement Minimax algorithm for AI
def minimax(board, depth, is_maximizing):
  if check_win(board, "O"):
    return 10 - depth
  if check_win(board, "X"):
    return -10 + depth
  if check_draw(board):
    return 0
  
  if is_maximizing:
    best_score = -float('inf')
    for i in range(9):
      if board[i] == " ":
        board[i] = "O"
        score = minimax(board, depth + 1, False)
        board[i] = " "
        best_score = max(score, best_score)
    return best_score
  else:
    best_score = float('inf')
    for i in range(9):
      if board[i] == " ":
        board[i] = "X"
        score = minimax(board, depth + 1, True)
        board[i] = " "
        best_score = min(score, best_score)
    return best_score
  
def get_ai_move(board):
  print("🤖 Computer is thinking...")
  time.sleep(0.5)
  best_score = -float('inf')
  best_move = 0
  for i in range(9):
    if board[i] == ' ':
      board[i] = "O"
      score = minimax(board, 0, False)
      board[i] = " "  # Reset board spot after checking
      if score > best_score:
        best_score = score
        best_move = i
  return best_move

# step 4: the main game loop
def play_game():
  board = [' '] * 9
  current_player = 'X'
  
  print(logo)
  print_board([str(i+1) for i in range(9)])
  while True:
    if current_player == "O":
      move = get_ai_move(board)
    else:
      move = get_human_move(board,current_player)
    board[move] = current_player
    print_board(board)
    if check_win(board,current_player):
      if current_player == "O":
        print("🤖 Computer wins! Better luck next time.\n")
      else:
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