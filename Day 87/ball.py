from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.penup()
    self.dx = 10
    self.dy = 10
    self.move_speed = 0.04
  
  def move(self):
    self.goto(self.xcor() + self.dx, self.ycor() + self.dy)
    
  def bounce_y(self):
    self.dy *= -1
    
  def bounce_x(self):
    self.dx *= -1
    
  def reset_position(self):
    self.goto(0,-400)
    self.dy = 10
    self.bounce_x()