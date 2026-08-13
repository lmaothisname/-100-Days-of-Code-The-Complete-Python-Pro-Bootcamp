from turtle import Turtle

COLORS = ["#E74C3C", "#E67E22", "#F1C40F", "#2ECC71", "#3498DB", "#9B59B6"]

class Brick(Turtle):
    def __init__(self, position, color, points):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1.5, stretch_len=5)  # 30px high, 100px wide (fits 2560x1600)
        self.color(color)
        self.penup()
        self.goto(position)
        self.points = points

class BrickManager:
  def __init__(self):
    self.bricks = []
    self.create_wall()

  def create_wall(self):
    start_y = 650
    # 6 rows of colored bricks
    for row, color in enumerate(COLORS):
      points = (len(COLORS) - row) * 10
      y = start_y - (row * 42)  # 30px brick + 12px vertical gap
      # 19 columns spanning from x = -1035 to x = +1035
      for col in range(-9, 10):
        x = col * 115         # 100px brick + 15px horizontal gap
        brick = Brick(position=(x, y), color=color, points=points)
        self.bricks.append(brick)

  def remove_brick(self, brick):
    brick.goto(3000, 3000)
    brick.hideturtle()
    self.bricks.remove(brick)