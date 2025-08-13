from turtle import Turtle
BALL_STARTING_SPEED = 2


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = BALL_STARTING_SPEED
        self.y_move = BALL_STARTING_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # self.y_move *= -1
        self.goto(self.xcor(), self.ycor() * -1)  # portal mode

    def bounce_x(self):
        self.x_move *= -1

    def refresh(self):
        self.goto(0, 0)
        self.x_move = BALL_STARTING_SPEED
        self.y_move = BALL_STARTING_SPEED

    def increase_speed(self):
        self.x_move *= 1.1
        self.y_move *= 1.1
