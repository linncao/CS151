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


def makeTree(argv, x, y, n, scale, angle):
    """Creates an L-system from the file tree.txt.
       Builds a string from the L-system with n iterations.
       Draws the string with desired location, scale and angle.
    """
    goto(x, y)
    lsys = ls.createLsystemFromFile('systemB.txt')
    lstr = ls.buildString(lsys, n)
    turtle.width(scale/5)
    ti.drawString(lstr, scale, angle)


def makeTree_test(argv, x, y, scale):
    """Sets the width and height of the window.
       Puts several calls to ground function to test the function.
    """
    turtle.setup(600, 600)
    turtle.tracer(False)
    turtle.setheading(90)
    makeTree(argv[1], x, y, 3, scale, 22)
    makeTree(argv[1], x + 10*scale, y - 20*scale, 2, 1.5*scale, 46)
    makeTree(argv[1], x - 20*scale, y + 5*scale, 1, 2*scale, 60)
    ti.hold()


def makeGrid(argv, x, y, scale):
    """Places the trees with different angles and iterations into a 3x3 grid.
       The colors of the trees changes from left to right,
       indicating summer - fall - winter.
    """
    angles = [60, 46, 22]
    initx = x
    turtle.setheading(90)
    for i in range(3):
        for ii in [1, 2, 3]:
            if ii == 1:
                turtle.pencolor('saddle brown')
            elif ii == 2:
                turtle.pencolor('gold')
            elif ii == 3:
                turtle.pencolor('light cyan')
            makeTree(argv[1], x, y, ii, scale, angles[i])
            x = x + scale*20
        y = y + scale*20
        x = initx


def main(argv):
    """Sets the width and height of the window.
       Puts several calls to above functions to create the scene.
       Usage: python grid.py systemB.txt
    """
    if len(argv) < 2:
        print('Usage: python grid.py systemB.txt')
        exit()
    turtle.setup(600, 600)
    turtle.tracer(False)
    makeGrid(argv, -230, 170, 2)
    makeGrid(argv, -240, -290, 9)
    makeGrid(argv, 0, 0, 5)
    ti.hold()


if __name__ == '__main__':
    main(sys.argv)