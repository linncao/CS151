"""Linn Cao Nguyen Phuong
   Nov 10th, 2020
   Section A
   Lab 9: Classes
   CS151
"""
#version 2

import turtle
import random
import sys

class TurtleInterpreter:
    def __init__(self, dx = 800, dy = 800):
        """Sets up the screen
        """
        turtle.setup(dx, dy)
        turtle.tracer(False)


    def drawString(self, dstring, distance, angle):
        """Interpret the characters in string dstring as a series of turtle commands.
           Distance specifies the distance to travel for each forward command.
           Angle specifies the angle (in degrees) for each right or left command.
           The list of turtle supported turtle commands is:
           F : forward
           L : draw a leaf
           H : draw a flower
           T : draw a triangle
           < : push a color on the color stack
           > : pop a color off the color stack
           g : set color to green
           y : set color to yellow
           r : set color to red
           - : turn right
           + : turn left
           [ : save the turtle's heading and position
           ] : restore the turtle's heading and position
        """
        stack = []
        colorstack = []
        for c in dstring:
            if c == 'F':
                turtle.forward(distance)
            elif c == 'L':
                turtle.begin_fill()
                turtle.circle(distance/2,70)
                turtle.left(110)
                turtle.circle(distance/2,70)
                turtle.end_fill()
            elif c == 'H':
                turtle.width(distance/10)
                turtle.begin_fill()
                for i in range(10):
                    turtle.circle(distance/2, 60)
                    turtle.left(120)
                    turtle.circle(distance/2, 60)
                    turtle.left(60)
                turtle.end_fill()
                turtle.width(2)
            elif c == 'T':
                turtle.begin_fill()
                for i in range(3):
                    turtle.forward(distance/2)
                    turtle.left(120)
                turtle.end_fill()
            elif c == '<':
                colorstack.append(turtle.color()[0])
            elif c == '>':
                save = colorstack.pop()
                turtle.color(save)
            elif c == 'g':
                turtle.color(0.15, 0.5, 0.2)
            elif c == 'y':
                turtle.color(0.8, 0.8, 0.3)
            elif c == 'r':
                turtle.color(0.7, 0.2, 0.3)
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


    def hold(self):
        """Holds the screen open until user clicks or presses 'q' key
        """
        turtle.hideturtle()
        turtle.update()
        turtle.onkey(turtle.bye, 'q')
        turtle.listen()
        turtle.exitonclick()


    def place(self, xpos, ypos, angle = None):
        """Moves turtle to desired location
           Sets angle of turtle
        """
        turtle.up()
        turtle.goto(xpos, ypos)
        if angle != None:
            turtle.setheading(angle)
        turtle.down()

    
    def orient(self, angle):
        """Sets angle of turtle
        """
        turtle.setheading(angle)


    def goto(self, xpos, ypos):
        """Moves turtle to desired location
        """
        turtle.up()
        turtle.goto(xpos, ypos)
        turtle.down()

    
    def setColor(self, c):
        """Sets pen color to desired color
        """
        turtle.color(c)

    
    def fill(self,c):
        """Sets fill color to desired color
           Begins fill
        """
        turtle.fillcolor(c)
        turtle.begin_fill()


    def end(self):
        """Ends fill
        """
        turtle.end_fill()

    
    def setWidth(self, w):
        """Sets pen width
        """
        turtle.width(w)