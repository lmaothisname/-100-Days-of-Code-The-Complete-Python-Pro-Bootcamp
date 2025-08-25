from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
for step in range(10):
    timmy.forward(10)
    timmy.up()
    timmy.forward(10)
    timmy.down()
screen = Screen()
screen.exitonclick()