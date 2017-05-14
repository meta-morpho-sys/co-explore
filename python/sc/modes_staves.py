# This program wil represent graphically the output of the file modes.py

# figure out background photo (for staves)
## set turtle coordinates  OK
## figure out turtle stamp() function  OK
# figure out forward x distance x steps

import turtle


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
##   
    
    

def modesDrawer():
    turtle.mode("logo")
    turtle.penup()
    turtle.goto(-100, 0)
    #screen.register_shape("turtle.gif")
    turtle.shape("circle")
    turtle.shapesize(1, 2)
    turtle.tilt(40)
    turtle.color("blue")

    ''' numSteps = steps ## will draw notes based on
        distance in pixels x steps in the scale. will be used in the turtle.fd()
        The "steps()" function is defined in modes.py
    '''
    mode = [0, 3, 6, 9, 12] # this is only example

    for i in mode:
        turtle.stamp();
        turtle.penup();
        turtle.right(65)
        turtle.fd(80);
        turtle.pendown();
        turtle.setheading(0)
        
modesDrawer()

