"""Linn Cao Nguyen Phuong
   Dec 1st, 2020
   Section A
   Final Project
   CS151
"""
#version 4

import turtle
import random
import sys

class TurtleInterpreter:
    initialized = False


    def __init__(self, dx = 800, dy = 800):
        """Sets up the screen
        """
        if TurtleInterpreter.initialized:
            return
        TurtleInterpreter.initialized = True
        turtle.setup(dx, dy)
        turtle.tracer(False)


    def title(self, title):
        turtle.title(title)

    
    def bgcolor(self, color):
        turtle.bgcolor(color)


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
           b : set color to blue
           - : turn right
           + : turn left
           [ : save the turtle's heading and position
           ] : restore the turtle's heading and position
           { : begin fill
           } : end fill
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
            elif c == 'b':
                turtle.color(0.005, 0.206, 0.25)
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
            elif c == '{':
                turtle.begin_fill()
            elif c == '}':
                turtle.end_fill()
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

    
    def setWidth(self, w):
        """Sets pen width
        """
        turtle.width(w)

    
    def fill(self):
        turtle.begin_fill()

    
    def end(self):
        turtle.end_fill()

    
    def write(self, text, size):
        """Replaces the turtle with a desired text
           in Arial, size, style bold
        """
        # turtle.clear()
        turtle.write(text, font=('Arial', size, 'bold'))
        turtle.hideturtle()