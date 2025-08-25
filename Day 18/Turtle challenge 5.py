import turtle as t
from turtle import Screen
import random

timmy = t.Turtle()
timmy.pensize(2)
timmy.speed(0)
timmy.shape("turtle")
for step in range(6):
    for color in ("red","green","blue","magenta","cyan","white","yellow"):
        timmy.color(color)
        timmy.circle(100)
        timmy.left(10)
screen = Screen()
screen.exitonclick()