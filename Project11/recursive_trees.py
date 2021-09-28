"""Linn Cao Nguyen Phuong
   Nov 16th, 2020
   Section A
   Lab 11: Design with Recursion A
   CS151
"""

import turtle
from random import randint

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def goto(x, y):
    myTurtle.up()
    myTurtle.goto(x, y)
    myTurtle.down()
    myTurtle.setheading(90)


def tree(myTurtle, branchLen):
    if branchLen > 10:
        myTurtle.forward(branchLen)
        myTurtle.right(40)
        tree(myTurtle, branchLen - 30)
        myTurtle.left(80)
        tree(myTurtle, branchLen - 30)
        myTurtle.right(40)
        myTurtle.backward(branchLen)


def drawTree1(myTurtle, level, size, angle, ratio):
    if level >= 0:
        myTurtle.forward(size)
        drawTree1(myTurtle, level - 1, size/ratio, angle, ratio)
        myTurtle.left(angle)
        drawTree1(myTurtle, level - 1, size/ratio, angle, ratio)
        myTurtle.right(2*angle)
        drawTree1(myTurtle, level - 1, size/ratio, angle, ratio)
        myTurtle.left(angle)
        myTurtle.forward(-size)
    else:
        return


def drawTree2(myTurtle, level, size, angle, ratio):
    if level >= 0:
        myTurtle.forward(size)
        myTurtle.left(angle)
        drawTree2(myTurtle, level - 1, size/ratio, angle, ratio)
        myTurtle.right(2*angle)
        drawTree2(myTurtle, level - 1, size/ratio, angle, ratio)
        myTurtle.left(angle)
        myTurtle.forward(-size + size/10)
    else:
        return


def drawTree3(myTurtle, level, size, angle, ratio):
    if level >= 0:
        myTurtle.forward(size)
        drawTree3(myTurtle, level - 1, size/ratio, angle, ratio)
        myTurtle.right(angle)
        drawTree3(myTurtle, level - 1, size/ratio, angle, ratio)
        myTurtle.left(2*angle)
        drawTree3(myTurtle, level - 1, size/ratio, angle, ratio)
        myTurtle.right(angle)
        myTurtle.forward(-size + size/10)
    else:
        return


def main():
    myWin.setup(1000, 600)
    myWin.tracer(False)
    goto(-300, -180)
    drawTree3(myTurtle, randint(4, 6), randint(70, 100), randint(20, 40), randint(14, 18)/10)
    goto(0, -180)
    drawTree1(myTurtle, randint(4, 6), randint(80, 120), randint(20, 40), randint(14, 18)/10)
    goto(300, -180)
    drawTree2(myTurtle, randint(4, 6), randint(80, 120), randint(20, 40), randint(14, 18)/10)
    myTurtle.hideturtle()
    myWin.exitonclick()


main()