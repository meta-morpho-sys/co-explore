import turtle


line_length = 800
interline_space = 20


def turtle_init():
    turtle.setheading(0) # turtle heading EAST
    turtle.setpos(-500, 0)
    turtle.speed(0)
    turtle.pensize(5)
    turtle.bgcolor("blue")
    turtle.pencolor("blue")

    
def draw_stave(num_lines):
    """ Draw a number horizonal lines and spaces in between, typical for the music notation

    :param num_lines: a positive integer, the number of lines to draw.
    
    """
    for line in range(num_lines):
        draw_line()
        vertical_skip()
        

def draw_line():
    turtle.pendown() 
    turtle.fd(line_length)
    turtle.penup()
    turtle.back(line_length)


def vertical_skip():
    """ leap upwards to draw next line"""
    turtle.left(90)
    turtle.fd(interline_space)
    turtle.right(90)
    
     
if __name__ == '__main__':
    turtle_init()
    draw_stave(10)

   

