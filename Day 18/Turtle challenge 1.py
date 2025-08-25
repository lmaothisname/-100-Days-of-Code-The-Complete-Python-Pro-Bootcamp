from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
for step in range(1,5):
    timmy.forward(100)
    timmy.right(90)
screen = Screen()
screen.exitonclick()