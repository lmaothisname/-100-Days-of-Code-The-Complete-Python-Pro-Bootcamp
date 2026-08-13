from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, position):
    super().__init__()
    self.shape("square")
    self.color("cyan")
    self.shapesize(stretch_wid=1.5, stretch_len=10) 
    self.penup()
    self.goto(position)
    self.move_speed = 60
    
  def move_left(self):
    new_x = self.xcor() - self.move_speed
    if new_x > -1160:
      self.goto(new_x,self.ycor()) # Stay within window boundaries
      
  def move_right(self):
    new_x = self.xcor() + self.move_speed
    if new_x < 1160:
      self.goto(new_x,self.ycor())