from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import BrickManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("#111111")
screen.setup(width=2560, height=1600)
screen.title("Breakout Game")
screen.tracer(0)

# Instantiate objects
paddle = Paddle((0,-600))
ball = Ball()
brick_manager = BrickManager()
scoreboard = Scoreboard()
# Controls
screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "a")
screen.onkeypress(paddle.move_right, "d")
    
# Game loop
game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(ball.move_speed)
  ball.move()
  
  # 1. Wall Collisions (Left/Right)
  if ball.xcor() > 1250 or ball.xcor() < -1250:
    ball.bounce_x()
    
  # 2. Wall Collisions (Top)
  if ball.ycor() > 780:
    ball.bounce_y()
    
  # 3. Paddle Collisions
  if (ball.ycor() < -575
      and ball.ycor() > -600
      and abs(ball.ycor() - paddle.xcor())
      and ball.dy < 0):
    ball.bounce_y()
  
  # 4. Brick Collisions
  for brick in brick_manager.bricks:
    if(abs(ball.xcor() - brick.xcor()) < 60 and abs(ball.ycor() - brick.ycor()) < 25):
      ball.bounce_y() 
      scoreboard.add_score(brick.points)
      brick_manager.remove_brick(brick)
      break
    
  # 5. Missed Paddle (Bottom Edge)
  if ball.ycor() < - 750:
    scoreboard.lose_life()
    if scoreboard.lives <= 0:
      game_is_on = False
      scoreboard.game_over()
    else:
      ball.reset_position()
    
  # 6. Win condition (All bricks cleared)
  if (len(brick_manager.bricks) == 0):
    game_is_on = False
    scoreboard.victory()
screen.mainloop()