def printhello(name):
    print('hello' + name)


    
def drawCircles(col, turnAngle, circleDiam):
        import turtle
        cuteTurtle = turtle.Turtle()
        cuteTurtle.setpos(0, 50) # positions the turtle at coordinates x, y
        cuteTurtle.penup()
        cuteTurtle.right(75)
        cuteTurtle.pendown()
        cuteTurtle.speed(0)
        turtle.bgcolor("black")
        cuteTurtle.color(col)
        numCircles = int(210 / turnAngle) #calculates number of sircles to complete the round of circles if angle is changed
        for i in range(numCircles):
                cuteTurtle.pensize(1) #sets the drawing line thickness to 1
                cuteTurtle.circle(circleDiam)
                cuteTurtle.right(turnAngle)
 
        turtle.done()
