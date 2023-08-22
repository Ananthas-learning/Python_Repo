# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)
# print(timmy)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable
my_table = PrettyTable()
my_table.add_column("Pokemon Name", ["Pikachu", "squirtle", "charmander"])
my_table.add_column("Type", ["Electric", "water", "Fire"])
print(my_table)

my_table.align = "l"
print(my_table)

