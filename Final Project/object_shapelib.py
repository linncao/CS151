"""Linn Cao Nguyen Phuong
   Sep 17, 2020
   Section A
   Lab 4: Unique turtles
   CS151
"""

import random
import turtle

s = turtle.Screen()

def make_screen(width, height, title, color = 'black'):
    """Makes a 'Screen' object: the window in each turtles can draw shapes
    """
    s.setup(height = height, width = width)
    s.bgcolor(color)
    s.title(title)
    return s


def goto(turt, x, y, heading = 0):
    """Moves the turtle to (x, y) 
       with no connecting lines to the previous position
    """
    print('goto(): going to', x, y)
    print('goto(): before move, turtle at', turtle.position())
    turt.setheading(0)
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    print('goto(): after move, turtle now at', turtle.position())


def oval(turt, x, y, radius, penWidth = 3, fill = True, edgeColor = 'alice blue', fillColor = 'light blue', backgroundColor = 'salmon'):
    """Draws an oval race track at (x, y)
       anh chooses whether to fill it with which colors
    """
    goto(turt, x, y)
    turt.setheading(0)
    turt.right(45)
    turt.pensize(penWidth)
    if fill == True:
        turt.color(edgeColor, fillColor)
        turt.begin_fill()
        for i in range(2):
            turt.circle(radius, 90)
            turt.circle(radius/2, 90)
        turt.end_fill()
        goto(turt, x + 5*radius/14, y + radius/6)
        turt.color(edgeColor, backgroundColor)
        turt.begin_fill()
        turt.setheading(0)
        turt.right(45)
        for i in range(2):
            turt.circle(radius/2, 90)
            turt.circle(radius/4, 90)
        turt.end_fill()
        goto(turt, x + 17*radius/60, y + 7*radius/60)
        turt.right(44)
        for i in range(2):
            turt.circle(0.6*radius, 90)
            turt.circle(0.6*radius/2, 90)
        goto(turt, x + 2*radius/15, y + radius/30)
        turt.right(44)
        for i in range(2):
            turt.circle(5*radius/6, 90)
            turt.circle(5*radius/12, 90)
    else:
        for i in range(2):
            turt.circle(radius, 90)
            turt.circle(radius/2, 90)
        goto(turt, x + 4*radius/11, y + radius/5)
        turt.setheading(0)
        turt.right(45)
        for i in range(2):
            turt.circle(radius/2, 90)
            turt.circle(radius/4, 90)
    turt.hideturtle()


def star(turt, x, y, sideLength, fill = True, edgeColor = 'alice blue', fillColor = 'light slate gray'):
    """Draws a 5-point star and chooses its sidelength
       and whether to fill it with which colors
    """
    goto(turt, x, y)
    turt.speed(0)
    turt.pensize(1.5)
    if fill == True:
        turt.color(edgeColor, fillColor)
        turt.begin_fill()
        for i in range(5):
            turt.forward(sideLength)
            turt.right(144)
        turt.end_fill()
    else:
        turt.color(fillColor, edgeColor)
        turt.begin_fill()
        for i in range(5):
            turt.forward(sideLength)
            turt.right(144)
        turt.end_fill()
    turt.pensize(1)


def stars_random(turt, numStars = 40):
    """Randomly draws 40 stars around the whole screen
       and switches the edge and fill colors for half of them
    """
    for i in range(numStars):
        posx = random.randint(-500, 500)
        posy = random.randint(-350, 350)
        numStarsFill = random.random()
        if numStarsFill <= 0.5:
            star(turt, posx, posy, 20, True)
        else:
            star(turt, posx, posy, 20, False)


def cloud(turt, x, y, s, fill = True, edgeColor = 'lavender', fillColor = 'ghost white'):
    """Draws a cloud at (x, y), chooses the scale
       and whether to fill them with which colors
    """
    goto(turt, x, y)
    turt.speed(0)
    turt.setheading(90)
    turt.pensize(3)
    if fill == True:
        turt.color(edgeColor, fillColor)
        turt.begin_fill()
        turt.circle(s*50, 120)
        turt.right(60)
        turt.circle(s*80, 100)
        turt.right(80)
        turt.circle(s*50, 70)
        turt.circle(s*20, 30)
        turt.circle(s*50, 90)
        turt.right(50)
        turt.circle(s*120, 90)
        turt.right(60)
        turt.circle(s*50, 190)
        turt.end_fill()
    else:
        turt.color(fillColor, edgeColor)
        turt.begin_fill()
        turt.circle(s*50, 120)
        turt.right(60)
        turt.circle(s*80, 100)
        turt.right(80)
        turt.circle(s*50, 70)
        turt.circle(s*20, 30)
        turt.circle(s*50, 90)
        turt.right(50)
        turt.circle(s*120, 90)
        turt.right(60)
        turt.circle(s*50, 190)
        turt.end_fill()
    turt.pensize(1)


def draw_race_scene():
    """Puts several calls to the functions above
       to create the background and the race track
    """
    d1 = turtle.Turtle()
    cloud(d1, 550, 0, 1, False) 
    cloud(d1, -200, -230, 1.5, True)   
    cloud(d1, -390, 350, 1.8, True)
    stars_random(d1)
    oval(d1, -210, -100, 300)
    cloud(d1, 240, 210, 0.7, False)


# if __name__ == '__main__':
#     make_screen(1000, 700, 'linnxinhhihi', 'salmon')
#     draw_race_scene()

# s.exitonclick()