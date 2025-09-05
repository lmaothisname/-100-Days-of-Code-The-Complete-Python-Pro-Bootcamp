from turtle import  Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black") 
screen.title("Pong Game")
screen.tracer(0)
l_pad = Paddle((-350,0))
r_pad = Paddle((350,0))
ball = Ball()
screen.listen()
screen.onkey(r_pad.go_up, "Up")
screen.onkey(r_pad.go_down, "Down")
screen.onkey(l_pad.go_up, "w")
screen.onkey(l_pad.go_down, "s")
score = Scoreboard()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # Detect collision in the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # Detect collision in the paddle
    if ball.distance(l_pad) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    elif ball.distance(r_pad) < 50 and ball.xcor() > 320:
        ball.bounce_paddle()
    if ball.xcor() > 400:
        ball.refresh()
        score.l_point()
    if ball.xcor() < -400:
        ball.refresh()
        score.r_point()
screen.exitonclick()