from turtle import Turtle

BODY = ([0, 0], [-20, 0], [-40, 0])
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):

        self.snake_bodies = []
        for part_of_body in BODY:
            self.add_body(part_of_body)

    def add_body(self, part_of_body):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(part_of_body)
        self.snake_bodies.append(snake)

    def extend(self):
        self.add_body(self.snake_bodies[-1].position())

    def move(self):
        for snake_num in range(len(self.snake_bodies) - 1, 0, -1):
            new_x = self.snake_bodies[snake_num - 1].xcor()
            new_y = self.snake_bodies[snake_num - 1].ycor()
            self.snake_bodies[snake_num].goto(new_x, new_y)
        self.snake_bodies[0].fd(MOVE_DISTANCE)

    upmove = True

    def up(self):
        if self.snake_bodies[0].heading() != DOWN:
            self.snake_bodies[0].setheading(UP)

    def right(self):
        if self.snake_bodies[0].heading() != LEFT:
            self.snake_bodies[0].setheading(RIGHT)

    def left(self):
        if self.snake_bodies[0].heading() != RIGHT:
            self.snake_bodies[0].setheading(LEFT)

    def down(self):
        if self.snake_bodies[0].heading() != UP:
            self.snake_bodies[0].setheading(DOWN)
