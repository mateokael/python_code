from turtle import Turtle
import random

STARTING_SPEED = 2
MOVE_INCREMENT = 0.5
LANE_X_POSITIONS = [-350, -320, -230, -
                    200, -110, -80, 10, 40, 130, 160, 250, 280,]
COLORS = ["red", "orange", "yellow", "green", "blue"]


class Car:

    def __init__(self):

        self.cars = []
        self.spawn_car()
        self.car_speed = STARTING_SPEED

    def spawn_car(self):
        for _ in range(10):
            car = Turtle()
            car.shape("square")
            car.shapesize(1, 1.5)
            car.penup()
            car.setheading(90)
            car.color(random.choice(COLORS))
            # random_x = random.randint(-340, 340)
            random_x = random.choice(LANE_X_POSITIONS)
            random_y = random.randint(-250, 250)
            car.goto(random_x, random_y)
            self.cars.append(car)

    def move(self):
        for allcar in self.cars:
            allcar.fd(self.car_speed)
            if allcar.ycor() > 320:
                offset = random.randint(-200, 0)
                allcar.goto(random.randint(-340, 340), -400 + offset)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
