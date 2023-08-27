from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.new_x = x_pos
        self.new_y = y_pos
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(self.new_x, self.new_y)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


