import turtle as t
import random

timmy = t.Turtle()
screen = t.Screen()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

#colours = ["light steel blue", "cyan", "lime green", "red", "olive", "yellow", "crimson", "blue"]

#timmy.color("blue")
#timmy.shapesize(3, 3, 3)
# shapes = {"triangle": 3, "Square": 4, "Pentagon


def draw_polygon(no_of_sides):
    for _ in range(no_of_sides):
        angle = 360 / no_of_sides
        timmy.fd(100)
        timmy.rt(angle)


    #draw_polygon(_)
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading()+10)


draw_spirograph(5)

timmy.shape("turtle")
screen.exitonclick()
