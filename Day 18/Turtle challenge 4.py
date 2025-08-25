directions = [0,90,190,270]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
from turtle import Turtle, Screen
import random 
timmy = Turtle()
timmy.shape("turtle")
timmy.speed(0)
timmy.pensize(15)
for i in range(200):
    timmy.color(random.choice(colours))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))
screen = Screen()
screen.exitonclick()