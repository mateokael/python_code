
# REEBORG HURDLE 4 WITHOUT USING CHECK IF RIGHT CLEAR/WALL COMMAND
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def crw():
    # to check if right is clear/wall
    turn_left()
    move()
    turn_right()
# def jump():
#    while wall_in_front() == True:
#       crw()
 #      if not wall_in_front():
#           move()
 #          turn_right()
 #          while not wall_in_front():
#               move()
 #          if wall_in_front() == True:
 #              turn_left()
 #
 #
 # or you dont need to use if because


def jump():
    while wall_in_front() == True:
        crw()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()


while not at_goal():
    if wall_in_front() == True:
        jump()
    else:
        move()


# MAZE
# This code makes Reeborg solve a maze using the right-hand rule. First, Reeborg moves straight ahead until he hits a wall, then turns left to begin following the wall. In the main loop, Reeborg checks if the right side is clear; if it is, he turns right and moves forward. If the right is blocked but the front is clear, he moves forward. If both are blocked, he turns left to look for a new direction. This process repeats until Reeborg reaches the goal, effectively making him hug the right-hand wall through the maze.
def tr():
    tl()
    tl()
    tl()


def tl():
    turn_left()


def wif():
    return wall_in_front()


def rig():
    return right_is_clear()


while not wif():
    move()
tl()


while not at_goal():
    if rig():
        tr()
        move()
    elif not wif():
        move()
    else:
        tl()
