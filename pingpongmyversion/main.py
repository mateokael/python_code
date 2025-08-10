from turtle import Screen
import time
from paddle import Paddle
from score import Scoreboard
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

r_score = Scoreboard((-50, 0))
l_score = Scoreboard((50, 0))


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_on = True
while game_on:
    time.sleep(0.01)
    screen.update()

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 335 or ball.distance(l_paddle) < 50 and ball.xcor() < -335:
        ball.bounce_x()
        ball.increase_speed()
    if ball.xcor() > 380:
        ball.refresh()
        r_score.increase_score()

    if ball.xcor() < -380:
        ball.refresh()
        l_score.increase_score()

screen.exitonclick()
