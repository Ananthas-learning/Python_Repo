from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        #scoreboard.update_rscore()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        #scoreboard.update_lscore()



    # detect R paddle missed
    if ball.xcor() > 380:
        ball.reposition()
        scoreboard.update_lscore()

    # detect l paddle missed
    if ball.xcor() < -360:
        ball.reposition()
        scoreboard.update_rscore()


screen.exitonclick()
