from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-150, 200)
        self.write(f"score:{self.l_score}", align="center", font=("courier", 30, "normal"))
        self.goto(150, 200)
        self.write(f"score:{self.r_score}", align="center", font=("courier", 30, "normal"))

    def update_lscore(self):
        self.l_score += 1
        self.update_scoreboard()

    def update_rscore(self):
        self.r_score += 1
        self.update_scoreboard()


