import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600) 
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move,"space")
score_board = Scoreboard()
game_is_on = True
car = CarManager()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
    #Detect collision with car
    for i in car.all_car:
        if i.distance(player) < 20:
            game_is_on = False
            score_board.game_over()            
    if player.is_at_finish_line():
        player.go_to_start()
        score_board.increase_score()
        car.level_up()
screen.exitonclick()

