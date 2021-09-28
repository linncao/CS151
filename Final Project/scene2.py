"""Linn Cao Nguyen Phuong
   Dec 1, 2020
   Section A
   Final Project
   CS151
"""

import turtle
import random

s = turtle.Screen()
turt = turtle.Turtle()

def make_window(window_title, bgcolor, width, height):
	"""This function creates a screen object and returns it
	"""
	s.setup(height=height, width=width)
	s.bgcolor(bgcolor)
	s.title(window_title)
	return s


def make_turtle(shape, color, stretch_width, stretch_length, x_pos, y_pos):
	"""Creates a turtle and sets inital position
	"""
	turt = turtle.Turtle()
	turt.shape(shape)
	turt.shapesize(stretch_width, stretch_length)
	turt.color(color)
	turt.penup()
	turt.goto(x_pos, y_pos)
	return turt


def goto(turt, x, y):
    """Goes to desired location
    """
    turt.penup()
    turt.goto(x, y)
    turt.pendown()


def stair(turt, x, y, width, height, edgeColor, fillColor):
    """Draws a stair at (x, y) of the given width and height
       and controls whether to fill it
    """
    goto(turt, x, y)
    turt.begin_fill()
    turt.color(edgeColor, fillColor)
    for i in range(2):
        turt.forward(width)
        turt.left(90)
        turt.forward(height)
        turt.left(90)
    turt.end_fill()
    

def staircase(turt, x, y, s, edgeColor = 'black', fillColor = 'white'):
    """Draws a flight of stairs with varying scales at a given location
       and controls whether to fill them
    """
    stair(turt, x, y, 200*s, 10*s, edgeColor, fillColor)
    stair(turt, x + 5*s, y + 10*s, 190*s, 9*s, edgeColor, fillColor)
    stair(turt, x + 10*s, y + 19*s, 180*s, 8*s, edgeColor, fillColor)


def circleShape(turt, x, y, radius):
    """Draws a circle with given radius 
       at a given location and fills it
    """
    turt.width(2)
    turt.color('silver', 'rosy brown')
    turt.begin_fill()
    turt.setheading(0)
    goto(turt, x, y)
    turt.circle(radius, 360)
    turt.end_fill()


def circleStatue(turt, x, y, s):
    """Draws a bunch of circles with different scales
       to create a statue-like figure
    """
    circleShape(turt, x, y, 110*s)
    circleShape(turt, x + 140*s, y + 137*s, 50*s)
    circleShape(turt, x + 187*s, y + 217*s, 20*s)
    circleShape(turt, x + 220*s, y + 222*s, 13*s)
    circleShape(turt, x + 230*s, y + 246*s, 8*s)
    circleShape(turt, x - 20*s, y + 219*s, 65*s)
    circleShape(turt, x - 105*s, y + 297*s, 30*s)
    circleShape(turt, x + 30*s, y + 332*s, 20*s)
    circleShape(turt, x + 30*s, y + 373*s, 10*s)
    circleShape(turt, x + 42*s, y + 387*s, 5*s)


def statue(turt, x, y, s, edgeColor = 'dim gray', fillColor = 'gray'):
    """Draws a statue-like figure 
       by combining circleStatue and staircase function
    """
    circleStatue(turt, x, y, 0.5*s)
    staircase(turt, x - 60*s, y - 16*s, 0.6*s, edgeColor = edgeColor, fillColor = fillColor)


def drawTree(turt, level, size, angle, scale):
    """Draws tree
    """
    if level >= 0:
        turt.forward(size)
        drawTree(turt,  level - 1, size/scale, angle, scale)
        turt.left(angle)
        drawTree(turt, level - 1, size/scale, angle, scale)
        turt.right(2*angle)
        drawTree(turt, level - 1, size/scale, angle, scale)
        turt.left(angle)
        turt.forward(-size)
    else:
        return


def star(turt, x, y, distance):
    """Draws star
    """
    goto(turt, x, y)
    turt.color('gold')
    turt.begin_fill()
    for i in range(5):
        turt.forward(distance)
        turt.right(144)
    turt.end_fill()


def painting(turt, x, y, distance):
    """Draws painting
    """
    goto(turt, x, y)
    turt.setheading(0)
    turt.width(8)
    turt.color('saddle brown', 'crimson')
    turt.begin_fill()
    for i in range(2):
        turt.forward(distance)
        turt.left(90)
        turt.forward(distance*1.5)
        turt.left(90)
    turt.end_fill()


def room_outline(turt, distance):
    """Draws the outline of the room
    """
    turt.setheading(0)
    turt.width(2)
    turt.color('indian red', 'light coral')
    turt.begin_fill()
    for i in range(2):
        turt.forward(distance)
        turt.left(90)
        turt.forward(3*distance/4)
        turt.left(90)
    turt.end_fill()


def room1(turt, x, y, distance, scale):
    """Draws room 1
    """ 
    goto(turt, x, y)
    room_outline(turt, distance)
    statue(turt, x + 90*scale, y + 25*scale, 0.5, 'dim gray', 'gray')


def room2(turt, x, y, distance, scale):
    """Draws room 2
    """
    goto(turt, x, y)
    room_outline(turt, distance)
    goto(turt, x + 100*scale, y + 20*scale)
    turt.seth(90)
    turt.color('dark olive green')
    drawTree(turt, 4, 30, 20, 1.4)


def room3(turt, x, y, distance, scale):
    """Draws room 3
    """
    goto(turt, x, y)
    room_outline(turt, distance)
    painting(turt, x + 77*scale, y + 30*scale, 50*scale)


def room4(turt, x, y, distance, scale):
    """Draws room 4
    """
    goto(turt,x, y)
    room_outline(turt, distance)
    for i in range(30):
        star(turt, random.randint(x + 30*scale, x + 150*scale), random.randint(y + 30*scale, y + 130*scale), random.randint(10*scale, 20*scale))


def writeName(turt, text):
	"""Replaces the turtle with a desired text
	   in Arial, size 20, style normal
	"""
	turt.clear()
	turt.write(text, font=('Arial', 20, 'normal'))
	turt.hideturtle()


def writeNameMap(turt, text):
	"""Replaces the turtle with a desired text
	   in Arial, size 40, style bold
	"""
	turt.clear()
	turt.write(text, font=('Arial', 40, 'bold'))
	turt.hideturtle()


def writeNameEntrance(turt, text):
	"""Replaces the turtle with a desired text
	   in Arial, size 25, style underline
	"""
	turt.clear()
	turt.write(text, font=('Arial', 25, 'underline'))
	turt.hideturtle()


def main():
    """Draws the map
    """
    s.tracer(False)
    turt.hideturtle()
    make_window('Museum Map', 'bisque', 1000, 700)
    room1(turt, 110, 20, 200, 1)
    room2(turt, -310, 20, 200, 1)
    room3(turt, 110, -200, 200, 1)
    room4(turt, -310, -200, 200, 1)
    name1 = make_turtle('circle', 'indian red', 0.1, 0.1, -300, -20)
    writeName(name1, '1. Greenhouse')
    name2 = make_turtle('circle', 'indian red', 0.1, 0.1, 87, -20)
    writeName(name2, '2. Sculpture Gallery')
    name3 = make_turtle('circle', 'indian red', 0.1, 0.1, -325, -250)
    writeName(name3, '3. Futuristic Gallery')
    name4 = make_turtle('circle', 'indian red', 0.1, 0.1, 97, -250)
    writeName(name4, '4. Painting Gallery')
    name5 = make_turtle('circle', 'indian red', 0.1, 0.1, -60, -335)
    writeNameEntrance(name5, 'Entrance')
    mapname = make_turtle('circle', 'brown', 0.1, 0.1, -180, 220)
    writeNameMap(mapname, 'MUSEUM MAP')
    # s.exitonclick()


# if __name__ == '__main__':
#     main()
#     s.exitonclick()