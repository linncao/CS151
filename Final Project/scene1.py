"""Linn Cao Nguyen Phuong
   Dec 1, 2020
   Section A
   Final Project
   CS151
"""

import turtle

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


def step(turt, distance, angle, orientation, scale):
    """Draws a step of staircase
    """
    turt.setheading(orientation)
    turt.forward(distance*scale)
    turt.right(angle)
    turt.forward(distance*scale)
    turt.left(angle)


def stairsright(turt, numSteps, distance, scale):
    """Draws staircase extending to right side
    """
    if numSteps == 0:
        return
    step(turt, distance, 90, 0, scale)
    stairsright(turt, numSteps - 1, distance, scale)


def stairsleft(turt, numSteps, distance, scale):
    """Draws staircase extending to left side
    """
    if numSteps == 0:
        return
    step(turt, distance, -90, 180, scale)
    stairsleft(turt, numSteps - 1, distance, scale)


def stairs(turt, x, y, distance, scale):
    """Draws the whole staircase
    """
    goto(turt, x, y)
    turt.color('light grey')
    turt.begin_fill()
    stairsleft(turt, 9, distance*scale, scale)
    goto(turt, x, y)
    turt.setheading(0)
    turt.forward(200*scale)
    stairsright(turt, 9, distance*scale, scale)
    turt.setheading(180)
    turt.forward(560*scale)
    turt.end_fill()


def walls(turt, x, y, distance, scale, color):
    """Draws the walls
    """
    goto(turt, x, y)
    turt.setheading(0)
    turt.color(color)
    turt.begin_fill()
    for i in range(2):
        turt.forward(distance*scale)
        turt.right(90)
        turt.forward(scale*distance/8)
        turt.right(90)
    turt.end_fill()


def door(turt, x, y, distance, scale, color):
    """Draws the door
    """
    goto(turt, x, y)
    turt.setheading(90)
    turt.color(color)
    turt.begin_fill()
    turt.forward(distance*scale)
    turt.circle(scale*distance/2, 180)
    turt.forward(scale*distance)
    turt.left(90)
    turt.forward(scale*distance)
    turt.end_fill()


def building(turt, x, y, distance, scale):
    """Draws the building
    """
    goto(turt, x, y)
    turt.setheading(0)
    turt.width(3)
    turt.color('dark salmon', 'bisque')
    turt.begin_fill()
    for i in range(2):
        turt.forward(distance*scale)
        turt.left(90)
        turt.forward(scale*distance/2)
        turt.left(90)
    turt.end_fill()
    door(turt, x + 100*scale, y, scale*distance/7, 1, 'dark salmon')
    door(turt, x + 300*scale, y, scale*distance/4.5, 1, 'dark salmon')
    door(turt, x + 470*scale, y, scale*distance/7, 1, 'dark salmon')


def dome(turt, x, y, distance, scale):
    """Draws the dome
    """
    goto(turt, x, y)
    turt.setheading(0)
    turt.width(4)
    turt.color('cadet blue', 'powder blue')
    turt.begin_fill()
    turt.forward(distance*scale)
    turt.setheading(90)
    turt.circle(scale*distance/2, 180)
    turt.end_fill()
    turt.color('cadet blue')
    goto(turt, x + scale*distance/2, y + scale*distance/2)
    turt.setheading(198)
    turt.circle(scale*distance/2, 80)
    goto(turt, x + scale*distance/2, y + scale*distance/2)
    turt.setheading(232)
    turt.circle(scale*distance/1.5, 80)
    goto(turt, x + scale*distance/2, y + scale*distance/2)
    turt.setheading(161)
    turt.circle(scale*distance/2, -80)
    goto(turt, x + scale*distance/2, y + scale*distance/2)
    turt.setheading(125)
    turt.circle(scale*distance/1.5, -80)


def exterior(turt, x, y, distance, scale):
    """Draws the museum exterior by combining small functions
    """
    goto(turt, x, y)
    dome(turt, x - 100*scale, y + 210*scale, 400*scale, scale)
    building(turt, x - 150*scale, y, 500*scale, scale)
    building(turt, x - 500*scale, y, 500*scale, scale*0.7)
    building(turt, x + 350*scale, y, 500*scale, scale*0.7)
    walls(turt, x - 400*scale, y, 1000*scale, scale, 'silver')
    walls(turt, x - 400*scale, y - 125*scale, 1000*scale, scale, 'floral white')
    stairs(turt, x, y, 20*scale, scale)


def writeNameEntrance(turt, text):
	"""Replaces the turtle with a desired text
	   in Arial, size 40, style bold
	"""
	turt.clear()
	turt.write(text, font=('Arial', 40, 'bold italic'))
	turt.hideturtle()


def main(state = True):
    """Draws the museum exterior
    """
    s.tracer(False)
    turt.hideturtle()
    make_window('Museum Exterior', 'alice blue', 1000, 700)
    exterior(turt, -110, -140, 100, 1)
    if state == True:
        welcome = make_turtle('circle', 'cadet blue', 0.1, 0.1, -150, 30)
        writeNameEntrance(welcome, 'WELCOME')
    else:
        goodbye = make_turtle('circle', 'cadet blue', 0.1, 0.1, -150, 30)
        writeNameEntrance(goodbye, 'GOODBYE')
    # s.exitonclick()


# if __name__ == '__main__':
#     main(True)
#     s.exitonclick()