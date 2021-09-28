"""Linn Cao Nguyen Phuong
   Oct 27, 2020
   Section A
   Project 8: L-system Scene
   CS151
"""

import turtle


def drawString(dstring, distance, angle):
    """Interpret the characters in string dstring as a series of turtle commands.
       Distance specifies the distance to travel for each forward command.
       Angle specifies the angle (in degrees) for each right or left command.
       The list of turtle supported turtle commands is:
       F : forward
       L : leaf
       B : berry
       - : turn right
       + : turn left
       [ : save the turtle's heading and position
       ] : restore the turtle's heading and position
    """
    stack = []
    for c in dstring:
        if c == 'F':
            turtle.forward(distance)
        elif c == 'L':
            turtle.left(60)
            turtle.color('dark olive green', 'forest green')
            turtle.begin_fill()
            for i in range(2):
                turtle.circle(distance/3, 120)
                turtle.right(90)
            turtle.end_fill()
        elif c == 'B':
            turtle.right(90)
            turtle.color('dark olive green', 'red')
            turtle.begin_fill()
            turtle.circle(distance/3, 360)
            turtle.end_fill()
        elif c == '-':
            turtle.right(angle)
        elif c == '+':
            turtle.left(angle)
        elif c == '[':
            stack.append(turtle.pos())
            stack.append(turtle.heading())
        elif c == ']':
            turtle.up()
            turtle.setheading(stack.pop())
            turtle.goto(stack.pop())
            turtle.down()
    turtle.update()


def hold():
    """Holds the screen open until user clicks or presses 'q' key
    """
    turtle.hideturtle()
    turtle.update()
    turtle.onkey(turtle.bye, 'q')
    turtle.listen()
    turtle.exitonclick()