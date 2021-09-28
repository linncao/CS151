"""Linn Cao Nguyen Phuong
   Oct 27, 2020
   Section A
   Project 8: L-system Scene
   CS151
"""

import turtle
import sys 
import lsystem as ls
import turtle_interpreter as ti
import random


def goto(x, y):
    """Moves the turtle to desired location
    """
    turtle.up()
    turtle.goto(x, y)
    turtle.down()


def system1(argv, x, y, scale):
    """Creates an L-system from a text file (abstract1.txt).
       Builds a string from the L-system with 4 iterations.
       Draws the string with desired location, scale and angle at 120.
    """
    goto(x, y)
    turtle.setheading(-30)
    lsys = ls.createLsystemFromFile(argv[1])
    lstr = ls.buildString(lsys, 4)
    turtle.width(2)
    turtle.begin_fill()
    edgeColor = (random.random(), random.random(), random.random())
    fillColor = (random.random(), random.random(), random.random())
    turtle.color(edgeColor, fillColor)
    ti.drawString(lstr, 30*scale, 120)
    turtle.end_fill()


def system1_test(argv, x, y, scale):
    """Sets the width and height of the window.
       Puts several calls to system1 function to test the function.
       Usage: python abstract.py abstract1.txt
    """
    if len(argv) < 2:
        print('Usage: python abstract.py abstract1.txt')
        exit()
    turtle.setup(600, 800)
    turtle.tracer(False)
    system1(argv, x + 240*scale, y + 50*scale, scale)
    system1(argv, x + 100*scale, y - 50*scale, 0.5*scale)
    system1(argv, x - 100*scale, y - 200*scale, 1.5*scale)
    ti.hold()


def system2(argv, x, y, scale):
    """Creates an L-system from a text file (abstract2.txt).
       Builds a string from the L-system with 4 iterations.
       Draws the string with desired location, scale and angle at 90.
    """
    goto(x, y)
    turtle.setheading(0)
    lsys = ls.createLsystemFromFile(argv[2])
    lstr = ls.buildString(lsys, 4)
    turtle.color(random.random(), random.random(), random.random())
    turtle.begin_fill()
    ti.drawString(lstr, 10*scale, 90)
    turtle.end_fill()


def system2_test(argv, x, y, scale):
    """Sets the width and height of the window.
       Puts several calls to system2 function to test the function.
       Usage: python abstract.py 1 abstract2.txt
    """
    if len(argv) < 3:
        print('Usage: python abstract.py 1 abstract2.txt')
        exit()
    turtle.setup(600, 800)
    turtle.tracer(False)
    system2(argv, x - 300*scale, y - 400*scale, scale)
    system2(argv, x + 100*scale, y - 50*scale, 0.5*scale)
    system2(argv, x - 100*scale, y - 200*scale, 0.2*scale)
    ti.hold()


def system3(argv, x, y, scale):
    """Creates an L-system from a text file (abstract3.txt).
       Builds a string from the L-system with 3 iterations.
       Draws the string with desired location, scale and angle at 10.
    """
    goto(x, y)
    turtle.setheading(90)
    lsys = ls.createLsystemFromFile(argv[3])
    lstr = ls.buildString(lsys, 5)
    turtle.pencolor('gold')
    turtle.width(3*scale)
    ti.drawString(lstr, 50*scale, 120)


def system3_test(argv, x, y, scale):
    """Sets the width and height of the window.
       Puts several calls to system3 function to test the function.
       Usage: python abstract.py 1 2 abstract3.txt
    """
    if len(argv) < 4:
        print('Usage: python abstract.py 1 2 abstract3.txt')
        exit()
    turtle.setup(600, 800)
    turtle.tracer(False)
    system3(argv, x - 300*scale, y - 400*scale, scale)
    system3(argv, x + 100*scale, y - 50*scale, 0.5*scale)
    system3(argv, x - 100*scale, y - 200*scale, 0.2*scale)
    ti.hold()


def main(argv, x, y, scale):
    """Sets the width and height of the window.
       Puts several calls to above functions to create the scene.
       Usage: python abstract.py abstract1.txt abstract2.txt abstract3.txt
    """
    if len(argv) < 4:
        print('Usage: python abstract.py abstract1.txt abstract2.txt abstract3.txt')
        exit()
    turtle.setup(600, 800)
    turtle.tracer(False)
    system1(argv, x + 240*scale, y + 50*scale, scale)
    system2(argv, x - 300*scale, y - 400*scale, scale)
    system3(argv, x - 50*scale, y, 2*scale)
    ti.hold()


if __name__ == "__main__":
    main(sys.argv, 0, 0, 1)