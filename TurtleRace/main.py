from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput("Make a bet", "which turtle will win the race.Enter a color: ")
colors = ["red", "orange", "yellow", "blue", "purple", "green"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_race_on = False

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    new_turtle.color(colors[turtle_index])
    new_turtle.speed("fastest")
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"you won. The {winning_turtle}  color turtle won ")
            else:
                print(f"you lost. The {winning_turtle}  color turtle won ")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()


# def move_forward():
#     tim.forward(10)
#
#
# def move_backward():
#     tim.back(10)
#
#
# def move_left():
#     #tim.circle(-100,50,100)
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
#
# def move_right():
#     #tim.circle(100,50,100)
#     new_heading = tim.heading()-10
#     tim.setheading(new_heading)
#
#
# def clear_drawing():
#     #tim.reset()
#     tim.clear()
#     tim.penup()
#     tim.home()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="d", fun=move_right)
# screen.onkey(key="c", fun=clear_drawing)


