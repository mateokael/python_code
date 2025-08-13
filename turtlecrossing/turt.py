from turtle import Turtle
START_POSITION = (-380, 0)
FINISH_LINE_X = 380
TURTLE_SPEED = 40


class turtle(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.penup()
        self.goto_start()

    def goto_start(self):
        self.goto(START_POSITION)

    def turtle_forward(self):
        self.setheading(0)
        self.fd(TURTLE_SPEED)

    def turtle_up(self):
        if self.ycor() + TURTLE_SPEED <= 280:  # top boundary
            self.setheading(90)
            self.forward(TURTLE_SPEED)

    def turtle_down(self):
        if self.ycor() - TURTLE_SPEED >= -280:
            self.setheading(270)
            # bottom boundary
            self.fd(TURTLE_SPEED)

    def is_at_finish_line(self):
        return self.xcor() > FINISH_LINE_X
