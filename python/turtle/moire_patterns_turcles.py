#this program will design two sizes of circles by using Turtles
        
import turtle
cuteTurtle = turtle.Turtle()
cuteTurtle.speed(0)
turtle.bgcolor("blue")


# function drawCircles(col)     #col =color
# This function will draw a full circle of cirles and
# will let the user chose the colour. 

def drawCircles(col, turnAngle):
        numCircles = int(360 / turnAngle)
        for i in range(numCircles):
                cuteTurtle.pensize(3) #sets the drawing line thickness to 1
                cuteTurtle.circle(80)
                cuteTurtle.right(turnAngle)
                cuteTurtle.color(col)


cuteTurtle.forward(70)

for i in range(9):
        cuteTurtle.penup()
        cuteTurtle.forward(100) # cuteTurtle is an object "." is the access to the function "forward" 
        cuteTurtle.pendown()

        drawCircles("white", 10)

        cuteTurtle.penup()
        cuteTurtle.backward(100) # cuteTurtle is an object "." is the access to the function "forward" 
        cuteTurtle.right(45)

        cuteTurtle.penup()
        cuteTurtle.forward(100) # cuteTurtle is an object "." is the access to the function "forward" 
        cuteTurtle.pendown()

        drawCircles("red", 5)

##for i in range(numCircles):
##        cuteTurtle.color("white")
##        cuteTurtle.pensize(1) #sets the drawing line thickness to 1
##        cuteTurtle.circle(150)
##        cuteTurtle.right(turnAngle)
        
turtle.done()







# numCircles = 
# turnAngle = 5 #rotate angle in degrees clockwise
# x = numCircles * turnAngle # after x turnes for numCircles * turnAngle
                             # it returns to the same direction
# 360 = numCircles * turnAngle ~ replace "x" with 360 degrees
# NA = 360
# NA/A = 360/A
# N = 360/A

# test ?
        
        
