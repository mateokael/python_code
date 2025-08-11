from turtle import Turtle
START_POSITION = (-380, 0)
FINISH_LINE_X = 380


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
        self.fd(20)

    def turtle_up(self):
        self.setheading(90)
        self.fd(20)

    def turtle_down(self):
        self.setheading(270)
        self.fd(20)

    def is_at_finish_line(self):
        return self.xcor() > FINISH_LINE_X
