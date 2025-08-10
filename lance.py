import turtle as t
from turtle import Screen


import random
tim = t.Turtle()
# import colorgram

# rgb_colors = [

# ]
# colors = colorgram.extract('tite.jpg', 20)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
tim.speed(10)
color_list = [(187, 80, 16), (111, 188, 173), (7, 11, 53), (180, 189, 17), (191, 148, 116), (226, 44, 71), (134, 156, 182), (66,
                                                                                                                             101, 120), (170, 9, 104), (62, 172, 12), (187, 43, 73), (27, 20, 14), (23, 83, 62), (230, 85, 34), (212, 209, 124), (112, 89, 4)]
x = 250
y = -250
tim.teleport(x, y, fill_gap=True)
while x != -250:
    x -= 25
    tim.teleport(x, y)
    if x == -50:
        y += 20


# t.colormode(255)


# def ran_col():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color


# turtle.speed(0)
# gapsize = int(input())
# for tilt in range(int(360/gapsize)):
#     turtle.color(ran_col())
#     turtle.circle(100)
#     turtle.rt(gapsize)


# turn = [
#     0,
#     90,
#     180,
#     270

# ]
# turtle.speed(0)
# turtle.pensize(10)

# on = True
# while on:
#     turtle.color(ran_col())
#     turtle.fd(30)
#     turtle.rt(random.choice(turn))


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         turtle.fd(100)
#         turtle.rt(angle)


# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)


# for i in range(4):
#     turtle.backward(90)
#     turtle.lt(90)


# turtle.fd(30)
# turtle.lt(90)
# turtle.fd(200)
# turtle.rt(90)
# turtle.backward(60)
# turtle.rt(90)
# turtle.fd(200)


# # def fe():
# #     turtle.fd(100)
# #     turtle.rt(90)


# # for i in range(4):
# #     fe()


screen = Screen()
screen.exitonclick()
