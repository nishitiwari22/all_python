#  Fractal - A curve or geometric figure, each part of which has the same similar patterns recur at progressively smaller scales.

#  Turtle model walk through

# https://www.youtube.com/watch?v=_ABdBoW4DV8

from turtle import *  #  2D graphic model in Python allows to make art (I guess?)'

shape("turtle")
speed(0)
# forward(100)  #  Moving the cursor forward from the middle of the canvas
# left(90)
# forward(100)
# right(45)
# forward(100)
# left(45)
# forward(100)

#  Fractal Tree
def tree(size, levels, angle):

    #  This 'if' statement is a base case.

    if levels == 0:
        color("green")
        dot(size)
        color("black")
        return

    forward(size)
    right(angle)  # Creating right branch angle.

    tree(size * 0.8, levels - 1, angle)

    left(
        angle * 2
    )  # Multiplying it with the value of right angle so that we can go to the left.
    tree(size * 0.8, levels - 1, angle)

    right(angle)
    backward(size)


#  Fractal Snowflake


def snowflake_side(length, levels):
    if levels == 0:
        forward(length)
        return

    length /= 3.0
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)
    right(120)
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)


def create_snowflake(sides, length):
    colors = ["orange", "dark green", "purple"]
    # for _ in range(sides):
    for i in range(sides):
        color(colors[i])
        snowflake_side(length, sides)
        right(360 / sides)
    # pass


left(90)
tree(70, 7, 30)

mainloop()  # It's a must to write so that the turtle screen doesn't close immediately as we run the program.
