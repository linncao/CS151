"""Linn Cao Nguyen Phuong
   Nov 16th, 2020
   Section A
   Lab 11: Design with Recursion A
   CS151
"""

import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def goto(x, y):
    myTurtle.up()
    myTurtle.goto(x, y)
    myTurtle.down()


def zigzag(myTurtle, num, length):
    """Draws the specified number of zigzags 
       with the specified number of zigzags and the length.
    """
    if num > 0:
        myTurtle.left(45)
        myTurtle.forward(length)
        myTurtle.right(90)
        myTurtle.forward(2*length)
        myTurtle.left(90)
        myTurtle.forward(length)
        myTurtle.right(45)
        zigzag(num - 1, length)


def recursive1(myTurtle, sideLen, angle, scaleFactor, minLen):
    if sideLen >= minLen:
        myTurtle.forward(sideLen)
        myTurtle.right(angle)
        recursive1(myTurtle, sideLen*scaleFactor, angle, scaleFactor, minLen)


def recursive2(myTurtle, sideLen, minLen):
    myTurtle.setheading(0)
    if sideLen >= minLen:
        for i in range(3):
            myTurtle.right(60)
            myTurtle.forward(sideLen)
            myTurtle.right(50)
        recursive2(myTurtle, sideLen*0.8, minLen)


def recursive3(myTurtle, sideLen, scaleFactor, minLen):
    if sideLen >= minLen:
        for i in range(10):
            turtle.circle(sideLen/2, 60)
            turtle.left(120)
            turtle.circle(sideLen/2, 60)
            turtle.left(60)
        recursive3(myTurtle, sideLen*scaleFactor, scaleFactor, minLen)


def main():
    myWin.tracer(False)
    goto(-200, 200)
    recursive1(myTurtle, 100, 60, 0.95, 10)
    goto(150, -150)
    recursive2(myTurtle, 100, 10)
    goto(0, 0)
    recursive3(myTurtle, 150, 0.9, 10)
    myWin.exitonclick()


main()