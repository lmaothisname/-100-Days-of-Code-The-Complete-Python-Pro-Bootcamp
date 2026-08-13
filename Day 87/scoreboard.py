from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.score = 0
    self.lives = 3
    self.update_scoreboard()
    
  def update_scoreboard(self):
    self.clear()
    # Top-Left corner for Score
    self.goto(-1150, 720)
    self.write(f"Score: {self.score}", font=("Courier", 28, "bold"))
    
    # Top-Right corner for Lives
    self.goto(900,720)
    self.write(f"Lives: {self.lives}", font=("Courier", 28, "bold"))
    
  def add_score(self,points):
    self.score += points
    self.update_scoreboard()
    
  def lose_life(self):
    self.lives -= 1
    self.update_scoreboard()
    
  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER", align="center", font=("Courier", 56, "bold"))
    
  def victory(self):
    self.goto(0,0)
    self.write("YOU WIN!", align="center", font=("Courier", 56, "bold"))