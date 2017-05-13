#this program will design two sets of circles to reproduce Moire' patterns
#by using Turtles
        
import turtle
cuteTurtle = turtle.Turtle()
cuteTurtle.speed(0)
turtle.bgcolor("blue")


# This function will draw a full circle of cirles and
# will let the user chose the colour. 

def drawCircles(col, turnAngle):
        cuteTurtle.color(col)
        numCircles = int(360 / turnAngle)
        for i in range(numCircles):
                cuteTurtle.pensize(1) #sets the drawing line thickness to 1
                cuteTurtle.circle(180)
                cuteTurtle.right(turnAngle)
              
for i in range(2):
        drawCircles("white", 10)
        cuteTurtle.penup()
        cuteTurtle.forward(20) # cuteTurtle is an object "." is the access to the function "forward" 
        cuteTurtle.pendown()

        drawCircles("white", 10)
        cuteTurtle.penup()
        cuteTurtle.forward(150) # cuteTurtle is an object "." is the access to the function "forward" 
        cuteTurtle.pendown()


turtle.done()





# reflections on how the function drawCircles was created.
# numCircles = 
# turnAngle = 5 #rotate angle in degrees clockwise
# x = numCircles * turnAngle # after x turnes for numCircles * turnAngle
                             # it returns to the same direction
# 360 = numCircles * turnAngle ~ replace "x" with 360 degrees
# NA = 360
# NA/A = 360/A
# N = 360/A

# test ?
        
        
