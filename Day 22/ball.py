from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        # self.shapesize(stretch_len=20,stretch_wid=20)
        self.color("purple")
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    def bounce(self):
        self.y_move *= -1
        self.move_speed *= 0.9
    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    def refresh(self):
        self.goto(0,0)
        self.bounce_paddle()
        self.move_speed = 0.1
