"""Linn Cao Nguyen Phuong
   Sep 17, 2020
   Section A
   Project 3: Scenes within scenes
   CS151
"""

import turtle
import random
import sys
import math

turtle.tracer(0)

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


def rectangle(x, y, width, height, fill = False, edgeColor = 'black', fillColor = 'red'):
    """Draws a rectangle at (x, y) of the given width and height 
       and controls whether to fill the rectangle
    """
    goto(x, y)
    print("rectangle(): draws a ", width, "x ", height, "rectangle and chooses whether to fill it.")
    if fill == True:
        turtle.width(2)
        turtle.color(edgeColor, fillColor)
        turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    if fill == True:
        turtle.end_fill()
        turtle.color(edgeColor, fillColor)
        turtle.width(1)


def mondrian(x, y, s, numRectangles = 100):
    """Creates a Mondrian scene with randomly placed
       rectangles and fills 40% of the number of them
    """
    goto(x, y)
    turtle.setheading(0)
    for i in range(numRectangles):
        if x < s*200:
            posx = random.randint(x, s*200)
        else:
            posx = random.randint(s*200, x)
        if y < s*200:
            posy = random.randint(y, s*200)
        else:
            posy = random.randint(s*200, y)
        widthLength = random.randint(s*20, s*50)
        heightLength = random.randint(s*20, s*50)
        fillColorR = random.random()
        fillColorG = random.random()
        fillColorB = random.random()
        turtle.width(2)
        numberOfFill = random.random()
        if numberOfFill <= 0.4:
            rectangle(posx, posy, widthLength, heightLength, True, fillColor = (fillColorR, fillColorG, fillColorB))
        else:
            rectangle(posx, posy, widthLength, heightLength, False)


def parallelogram(x, y, width, height, fill = False, left = False, edgeColor = 'black', fillColor = 'red'):
    """Draws a parallelogram at (x, y) of the given width and height 
       and controls whether to fill the parallelogram and what side it faces
    """
    goto(x, y)
    print("parallelogram(): draws a ", width, "x ", height, "parallelogram, chooses whether to fill it and what side it faces.")
    turtle.setheading(0)
    if fill == True:
        turtle.width(2)
        turtle.color(edgeColor, fillColor)
        turtle.begin_fill()
        if left == True:
            turtle.left(30)
            for i in range(2):
                turtle.forward(width)
                turtle.left(60)
                turtle.forward(height)
                turtle.left(120)
        else:
            turtle.left(150)
            for i in range(2):
                turtle.forward(width)
                turtle.right(60)
                turtle.forward(height)
                turtle.right(120)
        turtle.color(edgeColor, fillColor)
        turtle.width(1)
        turtle.end_fill()
    else:
        if left == True:
            turtle.left(30)
            for i in range(2):
                turtle.forward(width)
                turtle.left(60)
                turtle.forward(height)
                turtle.left(120)
        else:
            turtle.left(150)
            for i in range(2):
                turtle.forward(width)
                turtle.right(60)
                turtle.forward(height)
                turtle.right(120)


def parallelogram_mondrian(x, y, s, left = False, numParallelograms = 10):
    """Creates a Mondrian scene with randomly placed parallelograms, 
       controls which side they face and fills 40% of the number of them
    """
    goto(x, y)
    turtle.setheading(0)
    for i in range(numParallelograms):
        if x < s*200 + x:
            posx = random.randint(x, x + s*200)
        else:
            posx = random.randint(s*200 + x, x)
        if y < s*200:
            posy = random.randint(y, s*200)
        else:
            posy = random.randint(s*200, y)
        widthLength = random.randint(s*20, s*50)
        heightLength = random.randint(s*20, s*50)
        fillColorR = random.random()
        fillColorG = random.random()
        fillColorB = random.random()
        turtle.width(2)
        numberOfFill = random.random()
        if left == True:
            if numberOfFill <= 0.4:
                parallelogram(posx, posy, widthLength, heightLength, True, True, fillColor = (fillColorR, fillColorG, fillColorB))
            else:
                parallelogram(posx, posy, widthLength, heightLength, False, True)
        else:
            if numberOfFill <= 0.4:
                parallelogram(posx, posy, widthLength, heightLength, True, False, fillColor = (fillColorR, fillColorG, fillColorB))
            else:
                parallelogram(posx, posy, widthLength, heightLength, False, False)

# New scene
def circular_mondrian(x, y, s, numRectangles = 200):
    """Create a circular Mondrian scene that chooses 
       the number of rectangles and fill 40% of them
    """
    goto(x, y)
    posa = random.randint(x + s*3, x + s*20)
    posb = random.randint(y + s*3, y + s*20)
    for i in range(numRectangles):
        radius = abs(s*100 - x)
        posx = random.randint(posa - radius, posa + radius)
        ymultiply = [-1, 1]
        multiply = random.randint(0, 1)
        posy = ymultiply[multiply]*random.randint(0, int(math.sqrt(radius**2 - (posx - posa)**2))) + posb
        widthLength = random.randint(s*10, s*20)
        heightLength = random.randint(s*10, s*20)
        fillColorR = random.random()
        fillColorG = random.random()
        fillColorB = random.random()
        turtle.width(2)
        numberOfFill = random.random()
        if numberOfFill <= 0.4:
            rectangle(posx, posy, widthLength, heightLength, True, fillColor = (fillColorR, fillColorG, fillColorB))
        else:
            rectangle(posx, posy, widthLength, heightLength, False)

# 1st simple shape from Project 2
def arch(x, y, width, height, fill = False, edgeColor = 'black', fillColor = 'white'):
    """Draws an arch at (x, y) of the given width and height
       and controls whether to fill it
    """
    print('arch(): draws arch of size', width, height, ', controls whether to fill it')
    goto(x, y)
    turtle.setheading(0)
    if fill == True:
        turtle.begin_fill()
        turtle.color(edgeColor, fillColor)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.circle(width/2, 180)
    turtle.forward(height)
    if fill == True:
        turtle.end_fill()
        turtle.color(edgeColor, 'white')

# 1st compound shape from Project 2
def arches(x, y, s, fill = False, edgeColor = 'black', fillColor = 'white'):
    """Draws three arches with varying scales at a given location
       and controls whether to fill them
    """
    # put several calls to the arch function
    colorlist = [fillColor, 'light blue']
    index = random.randint(0, 1)
    arch(x, y, 20*s, 35*s, fill, edgeColor, fillColor)
    arch(x + 22*s, y, 10*s, 22*s, fill, edgeColor, fillColor)
    arch(x - 12*s, y, 10*s, 22*s, fill, edgeColor, fillColor)

# 2nd simple shape from Project 2
def stair(x, y, width, height, fill = False, edgeColor = 'black', fillColor = 'white'):
    """Draws a stair at (x, y) of the given width and height
       and controls whether to fill it
    """
    goto(x, y)
    print('rectangle(): draws rectangle of size', width, height, ', controls whether to fill it.')
    if fill == True:
        turtle.begin_fill()
        turtle.color(edgeColor, fillColor)
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    if fill == True:
        turtle.end_fill()
        turtle.color(edgeColor, 'white')
    
# 2nd compound shape from Project 2
def staircase(x, y, s, fill = False, edgeColor = 'black', fillColor = 'white'):
    """Draws a flight of stairs with varying scales at a given location
       and controls whether to fill them
    """
    # put several calls to the stair function
    colorlist = [fillColor, 'indigo']
    index = random.randint(0, 1)
    rectangle(x, y, 200*s, 10*s, fill, edgeColor, fillColor)
    rectangle(x + 5*s, y + 10*s, 190*s, 9*s, fill, edgeColor, fillColor)
    rectangle(x + 10*s, y + 19*s, 180*s, 8*s, fill, edgeColor, fillColor)


def circleShape(x, y, radius):
    """Draws a circle with given radius 
       at a given location and fills it
    """
    turtle.width(2)
    turtle.color('rosy brown','antique white')
    turtle.begin_fill()
    turtle.setheading(0)
    goto(x, y)
    print('circleShape(): draws a circle at location', x, y, ', fills it.')
    turtle.circle(radius, 360)
    turtle.end_fill()


def circleStatue(x, y, s):
    """Draws a bunch of circles with different scales
       to create a statue-like figure
    """
    # put several calls to the circleShape function
    circleShape(x, y, 110*s)
    circleShape(x + 140*s, y + 137*s, 50*s)
    circleShape(x + 187*s, y + 217*s, 20*s)
    circleShape(x + 220*s, y + 222*s, 13*s)
    circleShape(x + 230*s, y + 246*s, 8*s)
    circleShape(x - 20*s, y + 219*s, 65*s)
    circleShape(x - 105*s, y + 297*s, 30*s)
    circleShape(x + 30*s, y + 332*s, 20*s)
    circleShape(x + 30*s, y + 373*s, 10*s)
    circleShape(x + 42*s, y + 387*s, 5*s)

# New scene
def statue(x, y, s, edgeColor = 'dim gray', fillColor = 'gray'):
    """Draws a statue-like figure 
       by combining circleStatue and staircase function
    """
    circleStatue(x, y, 0.5*s)
    staircase(x - 60*s, y - 16*s, 0.6*s, True, edgeColor = edgeColor, fillColor = fillColor)

# New scene
def myScene(x, y, s):
    """Draws the background for the museum scene
    """
    # Background wall
    turtle.setheading(0)
    rectangle(x - 216*s, y - 125*s, 583*s, 500*s, True, edgeColor = 'alice blue', fillColor = 'alice blue') 
    # Door  
    turtle.setheading(0)
    turtle.width(2.5*s)
    arch(x, y, 150*s, 150*s, True, fillColor = 'slate gray')                                 
    goto(x + 75*s, y)
    # Decoration above the door
    turtle.setheading(90)
    turtle.forward(225*s)
    turtle.width(2*s)
    arches(x + 65*s, y + 235*s, s, True, fillColor = 'light blue')
    # Floor
    goto(x,y)
    turtle.color('steel blue','light blue')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.right(150)
    turtle.forward(250*s)
    turtle.left(150)
    turtle.forward(583*s)
    turtle.left(150)
    turtle.forward(250*s)
    turtle.end_fill()
    turtle.color('black','white')
    # Pictures
    turtle.width(15*s)
    goto(x - 40*s, y + 50*s)
    turtle.setheading(0)
    turtle.color('slate gray', 'misty rose')
    turtle.begin_fill()
    turtle.right(150)
    for i in range(2):
        turtle.forward(120*s)
        turtle.right(120)
        turtle.forward(160*s)
        turtle.right(60)
    goto(x + 190*s, y + 50*s)
    turtle.setheading(0)
    turtle.right(30)
    for i in range(2):
        turtle.forward(120*s)
        turtle.left(120)
        turtle.forward(160*s)
        turtle.left(60)
    turtle.end_fill()
    turtle.color('black', 'white')

# # main code
# if __name__=='__main__':
#     myScene(100, 100, 1)
#     myScene(-200, 200, 0.5)
#     myScene(-10, -200, 0.8)

# turtle.hideturtle()
# turtle.exitonclick()