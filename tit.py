from turtle import Turtle, Screen
import time


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("SNAKEGAME")
screen.tracer(0)


body = (0, -20, -40)
snake_bodies = []
for part_of_body in range(0, 3):
    snake = Turtle("square")
    snake.color("white")
    snake.penup()
    snake.setpos(body[part_of_body], 0)
    snake_bodies.append(snake)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    for snake_num in range(len(snake_bodies) - 1, 0, -1):

        new_x = snake_bodies[snake_num - 1].xcor()
        new_y = snake_bodies[snake_num - 1].ycor()
        snake_bodies[snake_num].goto(new_x, new_y)
    snake_bodies[0].fd(20)
    snake_bodies[0].rt(20)

screen.exitonclick()
