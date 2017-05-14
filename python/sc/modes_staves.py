# This program will represent graphically scales produced using module modes.py

"""
TODO:
 - figure out background photo (for staves)
 - figure out forward x distance x steps

"""

import turtle
from modes import scale, steps


# def draw_staff():
#    turtle.goto(-300, 0)
#
#    for i in range(5):
#        turtle.pendown()
#        turtle.fd(300)
#        turtle.penup()
#        turtle.setpos(-300, 20)
#
#
# draw_staff()
   

def initialize_turtle():
    SHAPE_SIZE_WIDTH = 0.5

    turtle.mode("logo")
    turtle.penup()

    # tilted oval, for stamping out notes
    turtle.shape("circle")
    turtle.shapesize(SHAPE_SIZE_WIDTH, 2 * SHAPE_SIZE_WIDTH)
    turtle.tilt(60)

    turtle.color("blue")

    reset_turtle_position()


def draw_intervals(intervals, step_size=30):
    """ Draw a line of notes spaced according to the list of intervals.

    :param intervals: A list of positive integers, representing the intervals in numbers of semitones.
    :param step_size: A positive integer multiplier for how long (in pixels) the turtle will move for a single semitone.

    """
    for step in intervals:
        turtle.stamp()
        turtle.fd(step_size * step)


def reset_turtle_position():
    turtle.goto(-200, -200)


def horizontal_skip(distance=20):
    turtle.right(90)
    turtle.fd(distance)
    turtle.left(90)


def position_to_column(x):
    """ Position turtle ready to draw another scale, but at horizontal position x."""
    reset_turtle_position()
    horizontal_skip(distance=x*30)

if __name__ == '__main__':

    initialize_turtle()

    # mode = [0, 3, 6, 9, 12] # this is only example
    mode = scale()
    intervals = steps(mode)

    print('     mode:', mode)
    print('intervals:', intervals)

    draw_intervals(intervals)

    # draw some more

    position_to_column(1)
    draw_intervals(steps(scale(1)))

    position_to_column(2)
    draw_intervals(steps(scale(2)))

    position_to_column(3)
    draw_intervals(steps(scale(3)))

    position_to_column(4)
    draw_intervals(steps(scale(4)))

    position_to_column(5)
    draw_intervals(steps(scale(scale_steps=[2, 2, 2, 2, 2, 2])))

    turtle.done()

