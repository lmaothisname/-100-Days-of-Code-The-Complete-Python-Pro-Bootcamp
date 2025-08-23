# import turtle
# import another_module
# print(another_module.another_variable)
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("maroon1")
# timmy.forward(100)
# from turtle import Screen
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"
print(table)