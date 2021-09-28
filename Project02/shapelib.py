"""Linn Cao Nguyen Phuong
   Sep 8, 2020
   Section A
   Linn's Project 2: Making A Museum Scene
   CS151
"""


import turtle
turtle.speed(0)


def goto(x, y):
    """Moves the turtle to (x, y) 
       with no connecting lines to the previous position
    """
    print('goto(): going to', x, y)
    print('goto(): before move, turtle at', turtle.position())
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    print('goto(): after move, turtle now at', turtle.position())


def block(x, y, width, height):
    """Draws a block at (x, y) 
       of the given width and height
    """
    goto(x, y)

    print('block(): drawing block of size', width, height)
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)


def bunchOfBlocks(x, y, scale):
    """Draws blocks stacking over one another
       at a given location (x, y)
    """
    print('bunchOfBlocks(): drawing blocks at location', x, y)

    #put several calls to the block function here
    block(x, y, 60*scale, 60*scale)
    block(x + 15*scale, y+60*scale, 30*scale, 30*scale)
    block(x + 25*scale, y+90*scale, 10*scale, 15*scale)


# import random

# for i in range(10):
#     bunchOfBlocks(random.random()*600 - 300,
#                   random.random()*600 - 300,
#                   random.random()*2 + 0.5)


# #main code
# bunchOfBlocks(-10, 0, 1)
# bunchOfBlocks(100, -200, 3)
# bunchOfBlocks(-300, -100, 2)


# turtle.hideturtle()
# turtle.exitonclick()