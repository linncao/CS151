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


def goto(x, y):
    """Moves the turtle to desired location
    """
    turtle.up()
    turtle.goto(x, y)
    turtle.down()


def makeTree1(x, y, scale):
    """Creates an L-system from the file tree.txt.
       Builds a string from the L-system with 4 iterations.
       Draws the string with desired location, scale and angle at 22.5.
    """
    goto(x, y)
    turtle.setheading(90)
    lsys = ls.createLsystemFromFile('tree.txt')
    lstr = ls.buildString(lsys, 5)
    turtle.width(1)
    turtle.pencolor('dark olive green')
    ti.drawString(lstr, scale, 22.5)


def makeTree2(x, y, scale):
    """Creates an L-system from the file tree.txt.
       Builds a string from the L-system with 4 iterations.
       Draws the string with desired location, scale and angle at -22.5.
    """
    goto(x, y)
    turtle.setheading(90)
    lsys = ls.createLsystemFromFile('tree.txt')
    lstr = ls.buildString(lsys, 5)
    turtle.width(1)
    turtle.pencolor('dark olive green')
    ti.drawString(lstr, scale, -22.5)


def makeTree_test(x, y, scale):
    """Sets the width and height of the window.
       Puts several calls to makeTree1 and makeTree2 functions to test the function.
    """
    turtle.setup(800, 600)
    turtle.tracer(False)
    # makeTree1(x - 230*scale, y - 250*scale, 7*scale)
    # makeTree1(x - 370*scale, y - 250*scale, 7*scale)
    # makeTree2(x + 150*scale, y - 100*scale, 5*scale)
    # makeTree2(x + 290*scale, y - 100*scale, 5*scale)
    makeTree2(x - 10*scale, y - 100*scale, 5*scale)
    ti.hold()


def makeMountains(x, y, scale):
    """Creates an L-system from the file mountain.txt.
       Builds a string from the L-system with 2 iterations.
       Draws the string with desired location, scale and angle at 120.
    """
    goto(x, y)
    turtle.setheading(0)
    lsys = ls.createLsystemFromFile('mountain.txt')
    lstr = ls.buildString(lsys, 2)
    turtle.color('peru', 'saddle brown')
    turtle.begin_fill()
    turtle.width(scale/80)
    ti.drawString(lstr, scale, 120)
    turtle.end_fill()


def makeMountains_test(x, y, scale):
    """Sets the width and height of the window.
       Puts several calls to makeMountains function to test the function.
    """
    turtle.setup(800, 600)
    turtle.tracer(False)
    makeMountains(x - 450*scale, y, 250*scale)
    makeMountains(x - 400*scale, y - 15*scale, 300*scale)
    makeMountains(x - 350*scale, y - 100*scale, 200*scale)
    ti.hold()


def ground(x, y, scale):
    """Draws the string created in the function's body
       with desired location, scale and angle at 30.
    """
    goto(x, y)
    turtle.setheading(90)
    s = 'FF---FF[----FF]F[--FF]FF---FF---FFFFF'
    turtle.begin_fill()
    turtle.color('olive drab', 'yellow green')
    turtle.width(scale/48)
    ti.drawString(s, scale, 30)
    turtle.end_fill()


def ground_test(x, y, scale):
    """Sets the width and height of the window.
       Puts several calls to ground function to test the function.
    """
    turtle.setup(800, 600)
    turtle.tracer(False)
    ground(x - 400*scale, y - 335*scale, 160*scale)
    ground(x, y, 80*scale)
    ground(x - 200*scale, y + 10*scale, 50*scale)
    ti.hold()


def main():
    """Sets the width and height of the window.
       Puts several calls to above functions to create the scene.
    """
    turtle.setup(800, 600)
    turtle.bgcolor('sky blue')
    turtle.tracer(False)
    makeMountains(-450, -15, 250)
    makeMountains(-400, -15, 300)
    makeMountains(-350, -15, 200)
    ground(-400, -335, 160)
    makeTree1(-150, -100, 5)
    makeTree1(-290, -100, 5)
    makeTree1(-230, -250, 7)
    makeTree1(-370, -250, 7)
    makeTree2(150, -100, 5)
    makeTree2(290, -100, 5)
    makeTree2(230, -250, 7)
    makeTree2(370, -250, 7)
    ti.hold()


if __name__ == '__main__':
    main()