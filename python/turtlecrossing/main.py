from turtle import Screen
import time

from turt import turtle
from cars import Car

screen = Screen()
screen.tracer(0)

character = turtle()
cars = Car()
cars.spawn_car()
screen.listen()

screen.onkey(character.turtle_forward, "d")
screen.onkey(character.turtle_up, "w")
screen.onkey(character.turtle_down, "s")

game_on = True
while game_on:
    time.sleep(0.01)
    screen.update()

    cars.move()

    for car in cars.cars:
        if car.distance(character) < 20:
            # game_on = False
            print("GAME OVER!")
    if character.is_at_finish_line():
        character.goto_start()
        cars.level_up()


screen.exitonclick()
