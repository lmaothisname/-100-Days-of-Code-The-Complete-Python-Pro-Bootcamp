# import colorgram
# colors = colorgram.extract("Day 18/hirst.jpg",80)
# rgb_color =[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     total = (r,g,b)
#     rgb_color.append(total)

# print(rgb_color)
color_list = [(208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70), (187, 93, 105), (187, 139, 170), (84, 123, 181), (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72), (45, 74, 78), (161, 202, 220), (80, 73, 44), (57, 131, 121), (218, 176, 188), (220, 183, 166), (166, 207, 165), (179, 188, 211), (149, 37, 35), (46, 73, 71), (45, 65, 62)]
import turtle as t
from turtle import Screen
import random
timmy = t.Turtle()
t.colormode(255)
timmy.pensize(20)
number_of_dots = 100
timmy.speed(0)
timmy.hideturtle()
for dot_count in range(1,number_of_dots+1):
    timmy.dot(20,random.choice(color_list))
    timmy.up()
    timmy.forward(50)
    timmy.down()
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.up()
        timmy.forward(50)
        timmy.down()
        timmy.setheading(180)
        timmy.up()
        timmy.forward(500)
        timmy.down()
        timmy.setheading(0)
screen = Screen()
screen.exitonclick()