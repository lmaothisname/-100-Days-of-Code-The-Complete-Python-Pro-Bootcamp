from turtle import Turtle,Screen
tim = Turtle()
screen = Screen()
def move_forward():
    tim.forward(36)
def move_backward():
    tim.backward(36)
def clockwise():
    tim.left(10)
def anti_clockwise():
    tim.right(10)
def remove():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(clockwise,"a")
screen.onkey(anti_clockwise,"d")
screen.onkey(remove,"c")
screen.exitonclick()