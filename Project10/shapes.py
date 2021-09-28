"""Linn Cao Nguyen Phuong
   Nov 12th, 2020
   Section A
   Lab 10: Inheritance
   CS151
"""

import turtle_interpreter as ti

class Shape:
    def __init__(self, distance = 100, angle = 90, color = (0, 0, 0), istring = ''):
        """Sets attributes of Shape
        """
        self.distance = distance
        self.angle = angle
        self.color = color
        self.string = istring

    
    def setColor(self, c):
        """Sets color
        """
        self.color = c

    
    def setDistance(self, d):
        """Sets distance
        """
        self.distance = d

    
    def setAngle(self, a):
        """Sets angle
        """
        self.angle = a

    
    def setString(self, s):
        """Sets string
        """
        self.string = s

    
    def draw(self, xpos, ypos, scale = 1.0, orientation = 0):
        """Draws the string at desired location with desired color
        """
        o = ti.TurtleInterpreter(800, 600)
        o.place(xpos, ypos, orientation)
        o.setColor(self.color)
        o.drawString(self.string, self.distance*scale, self.angle)


class Square(Shape):
    def __init__(self, distance = 100, color = (0, 0, 0)):
        """Sets attributes of Square
        """
        Shape.__init__(self, distance, 90, color, 'F-F-F-F-')


class Triangle(Shape):
    def __init__(self, distance = 100, color = (0, 0, 0)):
        """Sets attributes of Triangle
        """
        Shape.__init__(self, distance, 120, color, 'F-F-F-')