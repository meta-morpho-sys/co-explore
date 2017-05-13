#this program will design a changing pattern of circles by using Turtles
        
import turtle
cuteTurtle = turtle.Turtle()
cuteTurtle.setpos(0, 160) # positions the turtle at coordinates x, y
cuteTurtle.speed(0)
turtle.bgcolor("black")


# This function will draw a full circle of cirles and
# will let the user choose colour, angle and diameter of the circle. 

def drawCircles(col, turnAngle, circleDiam): 
        cuteTurtle.color(col)
        numCircles = int(360 / turnAngle) #calculates number of sircles to complete the round of circles if angle is changed
        for i in range(numCircles):
                cuteTurtle.pensize(1) #sets the drawing line thickness to 1
                cuteTurtle.circle(circleDiam)
                cuteTurtle.right(turnAngle)

for i in range(9):
        cuteTurtle.penup()
        cuteTurtle.forward(100) # cuteTurtle is an object "." is the access to the function "forward" 
        cuteTurtle.pendown()

        drawCircles("white", 16, 80)

        cuteTurtle.penup()
        cuteTurtle.backward(100) # cuteTurtle is an object "." is the access to the function "forward" 
        cuteTurtle.right(45)

        cuteTurtle.penup()
        cuteTurtle.forward(100) # cuteTurtle is an object "." is the access to the function "forward" 
        cuteTurtle.pendown()

        drawCircles("yellow", 16, 50)

        
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
        
        
