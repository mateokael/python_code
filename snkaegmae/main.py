from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("SNAKEGAME")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.08)

    snake.move()

    # collision w food
    if snake.snake_bodies[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # collision w wall
    if snake.snake_bodies[0].xcor() > 280 or snake.snake_bodies[0].xcor() < -280 or snake.snake_bodies[0].ycor() > 280 or snake.snake_bodies[0].ycor() < -280:
        game_on = False
        score.game_over()

    # collision w tailq
    for segment in snake.snake_bodies[1:]:
        if snake.snake_bodies[0].distance(segment) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()
