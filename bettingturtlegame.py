from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Your bet", prompt="which turtle?: ")
colors = ["red", "orange", "yellow", "green", "blue"]
start_pos = [-100, -70, -40, -10, 20]
all_turtles = []

for turtle_index in range(0, 5):
    turtles = Turtle(shape="turtle")
    turtles.color(colors[turtle_index])
    turtles.penup()
    turtles.goto(x=-230, y=start_pos[turtle_index])
    all_turtles.append(turtles)

if user_bet:
    race_on = True


moves = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 10, 5,
         0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 10, 5,
         0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 10, 5,
         0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 10, 5,
         0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 10, 5,
         0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 10, 5,
         0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 10, 5,
         0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 10, 5,
         200]
while race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            print(f"{winning_color} WON")

        move = random.choice(moves)
        turtle.fd(move)


# def fd():
#     tim.fd(20)


# def bk():
#     tim.bk(20)


# def rt():
#     tim.rt(20)


# def lt():
#     tim.lt(20)


# def circ():
#     tim.circle(100)


# def home():
#     tim.home()


# # def move_f():
# #     tim.fd(10)
# screen.listen()
# screen.onkey(key="w", fun=fd)
# screen.onkey(key="s", fun=bk)
# screen.onkey(key="d", fun=rt)
# screen.onkey(key="a", fun=lt)
# screen.onkey(key="q", fun=circ)
# screen.onkey(key="e", fun=home)


screen.exitonclick()
