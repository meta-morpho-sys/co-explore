# This program wil represent graphically the output of the file modes.py

# figure out background photo (for staves)
# figure out forward x distance x steps

import turtle
from modes import scale


##def stavesDrawer():
##    turtle.goto(-300, 0)
##    
##    
##    for i in range(5):
##        turtle.pendown()
##        turtle.fd(300)
##        turtle.penup()
##        turtle.setpos(-300, 20)
##        
##        
##stavesDrawer()
   

def initialize_turtle():
    turtle.mode("logo")
    turtle.penup()
    start_from = turtle.goto(-200, 0)
    #screen.register_shape("turtle.gif")
    turtle.shape("circle")
    turtle.shapesize(0.5, 1)
    turtle.tilt(40)
    turtle.color("blue")

initialize_turtle()   

def modes_drawer(mode):
    
    for step in mode:
        turtle.stamp();
        turtle.penup();
        turtle.right(80)
        turtle.fd(10 * step);
        turtle.pendown();
        turtle.setheading(0)
        
# mode = [0, 3, 6, 9, 12] # this is only example

mode = scale()

modes_drawer(mode)

