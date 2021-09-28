"""Linn Cao Nguyen Phuong
   Sep 8, 2020
   Section A
   Linn's Project 2: Making A Museum Scene
   CS151
"""


import turtle
import shapelib


def arch(x, y, width, height):
    """Draws an arch at (x, y) 
       of the given width and height
    """
    print('arch(): drawing arch of size', width, height)
    shapelib.goto(x, y)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.circle(width/2, 180)
    turtle.forward(height)


def arches(x, y, scale):
    """Draws three arches with varying scales
       at a given location
    """
    print('arches(): drawing three arches at location', x, y)

    #put several calls to the arch function
    arch(x, y, 20*scale, 35*scale)
    turtle.setheading(0)
    arch(x + 22*scale, y, 10*scale, 22*scale)
    turtle.setheading(0)
    arch(x - 12*scale, y, 10*scale, 22*scale)


def rectangle(x, y, width, height):
    """Draws a rectangle at (x, y) 
       of the given width and height
    """
    shapelib.goto(x, y)

    print('rectangle(): drawing rectangle of size', width, height)
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)


def stairs(x, y, scale):
    """Draws a flight of stairs
       with varying scales at a given location
    """
    print('stairs(): drawing staircase at location', x, y)

    #put several calls to the rectangle function
    rectangle(x, y, 200*scale, 10*scale)
    rectangle(x + 5*scale, y + 10*scale, 190*scale, 9*scale)
    rectangle(x + 10*scale, y + 19*scale, 180*scale, 8*scale)
    rectangle(x + 15*scale, y + 27*scale, 170*scale, 7*scale)
    rectangle(x + 20*scale, y + 34*scale, 160*scale, 6*scale)


def dome(x, y, diameter):
    """Draws the a dome at (x, y) of a given diameter
    """
    shapelib.goto(x, y)

    print('dome(): drawing dome of diameter', diameter)
    turtle.setheading(90)
    turtle.forward(300)
    turtle.circle(diameter, 180)
    turtle.setheading(270)
    turtle.forward(300)


def domed_roof(x, y, scale):
    """Draws a domed roof 
       with varying scales at a given location
    """
    print('domed_roof(): drawing domed roof at location', x, y)

    #put several calls to the dome function
    dome(x, y, 150*scale)
    dome(x + 20*scale, y, 170*scale)
    dome(x + 50*scale, y, 200*scale)
    dome(x + 100*scale, y, 250*scale)
    dome(x + 170*scale, y, 320*scale)
    dome(x + 270*scale, y, 420*scale)
    shapelib.goto(150, -10)
    turtle.goto(420, -10)
    shapelib.goto(139, 39)
    turtle.goto(420, 55)
    shapelib.goto(-150, -10)
    turtle.goto(-420, -10)
    shapelib.goto(-139, 39)
    turtle.goto(-420, 55)
    shapelib.goto(75, 109.9)
    turtle.goto(420, 500)
    shapelib.goto(-75, 109.9)
    turtle.goto(-420, 500)


def staircase():
    """Draws the stairs system
    """
    print('staircase(): drawing the stairs system')

    #call the stairs function and draw 2 other flights of stairs and a floor at suitable locations
    turtle.setheading(0)
    stairs(-100, -285, 1)
    shapelib.goto(-150, -170)
    turtle.goto(150, -170)
    shapelib.goto(-150, -170)
    turtle.setheading(0)
    for i in range(5):
        turtle.forward(15)
        turtle.right(90)
        turtle.forward(15)
        turtle.left(90)
    shapelib.goto(150, -170)
    turtle.setheading(180)
    for i in range(5):
        turtle.forward(15)
        turtle.left(90)
        turtle.forward(15)
        turtle.right(90)


def windows_doors():
    """Uses arches() and arch() 
       to make the museum's windows and doors
    """
    print('windows_doors(): drawing windows and doors')

    #call several arch and arches function at suitable locations
    arches(-60, -170, 6)
    turtle.setheading(0)
    turtle.setheading(0)
    arches(-23.5, -95, 2.4)
    turtle.setheading(0)
    shapelib.goto(-131, -100)
    turtle.forward(60)
    shapelib.goto(-59, -100)
    turtle.forward(120)
    shapelib.goto(72, -100)
    turtle.forward(60)
    shapelib.goto(0, 85)
    turtle.setheading(285)
    turtle.forward(30)
    turtle.right(30)
    turtle.forward(30)
    turtle.right(150)
    turtle.forward(30)
    turtle.right(30)
    turtle.forward(30)
    turtle.setheading(0)
    arch(-123, -95, 17, 54)
    turtle.setheading(0)
    arch(-97, -95, 17, 54)
    turtle.setheading(0)
    arch(106, -95, 17, 54)
    turtle.setheading(0)
    arch(80, -95, 17, 54)
    turtle.setheading(0)
    arch(-130, -170, 27, 54)
    turtle.setheading(0)
    arch(-101, -170, 27, 54)
    turtle.setheading(0)
    arch(-57, -170, 27, 54)
    turtle.setheading(0)
    arch(-28, -170, 27, 54)
    turtle.setheading(0)
    arch(1, -170, 27, 54)
    turtle.setheading(0)
    arch(30, -170, 27, 54)
    turtle.setheading(0)
    arch(74, -170, 27, 54)
    turtle.setheading(0)
    arch(103, -170, 27, 54)


def museum1():
    """Combines all above functions 
       at suitable locations to make a museum scene
    """
    print('museum_scene1(): drawing the museum with above functions')
    
    #call functions above at suitable locations
    domed_roof(150, -320, 1)
    staircase()
    turtle.setheading(0)
    shapelib.bunchOfBlocks(-15, -245, 0.6)
    windows_doors()


#main code
museum1()


turtle.hideturtle()
turtle.exitonclick()