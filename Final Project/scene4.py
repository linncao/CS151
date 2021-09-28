"""Linn Cao Nguyen Phuong
   Dec 1, 2020
   Section A
   Final Project
   CS151
"""

import turtle
import random
import math

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


def goto(x, y):
    """Moves the turtle to (x, y) 
       with no connecting lines to the previous position
    """
    turt.penup()
    turt.goto(x, y)
    turt.pendown()


class Shape():
    def __init__(self, distance, edgeColor, fillColor, numSides):
        """General attributes of the class
        """
        self.distance = distance
        self.edgeColor = edgeColor
        self.fillColor = fillColor
        self.numSides = numSides

    
    def intro(self):
        """Introduces basic information of the shape
        """
        print('This is a', self.numSides,'- side shape with lenth', self.distance, '.')

    
    def perimeter(self):
        """Calculates the shape's perimeter
        """
        return self.distance*self.numSides
        
    
    def drawShape(self, x, y, distance, edgeColor, fillColor):
        """Draws the shape
        """
        goto(x, y)
        self.edgeColor = edgeColor
        self.fillColor = fillColor
        self.distance = distance
        angle = 360/self.numSides
        turt.color(edgeColor, fillColor)
        turt.begin_fill()
        for i in range(self.numSides):
            turt.forward(distance)
            turt.right(angle)
        turt.end_fill()


class Square(Shape):
    def __init__(self, distance, edgeColor, fillColor, numSides = 4):
        """Takes general attributes of Shape class 
           Changes number of sides into 4
        """
        self.numSides = numSides
        super().__init__(distance, edgeColor, fillColor, numSides)


    def intro(self):
        """Introduces the shape
        """
        print('This is a square with perimeter', self.perimeter)


class Rectangle(Shape):
    def __init__(self):
        """Takes general attributes of Shape class
        """
        return


    def drawShape(self, x, y, distance, edgeColor, fillColor, fill = False):
        """Draws the rectangle
        """
        goto(x, y)
        if fill == True:
            self.edgeColor = edgeColor
            self.fillColor = fillColor
            self.distance = distance
            turt.color(edgeColor, fillColor)
            turt.begin_fill()
        for i in range(2):
            turt.forward(random.randint(distance, distance*random.randint(2, 3)))
            turt.right(90)
            turt.forward(random.randint(distance, distance*random.randint(2, 3)))
            turt.right(90)
        if fill == True:
            turt.end_fill()


    def intro(self):
        """Introduces the shape
        """
        print('This is a rectangle')

    
class Triangle(Shape):
    def __init__(self, distance, edgeColor, fillColor, numSides = 3):
        """Takes general attributes of Shape class 
           Changes number of sides into 3
        """
        self.numSides = numSides
        super().__init__(distance, edgeColor, fillColor, numSides)


    def intro(self):
        """Introduces the shape
        """
        print('This is a triangle with perimeter', self.perimeter)


    def drawShape(self, x, y, distance, edgeColor, fillColor):
        """Draws the shape
        """
        turt.setheading(60)
        super().drawShape(x, y, distance, edgeColor, fillColor)


class Circle(Shape):
    def __init__(self, distance, edgeColor, fillColor, numSides = 360):
        """Takes general attributes of Shape class 
           Changes number of sides into 360
        """
        self.numSides = numSides
        super().__init__(distance, edgeColor, fillColor, numSides)


    def intro(self):
        """Introduces the shape
        """
        print('This is a square with perimeter', self.perimeter)


obj_square = Square(10, 'blue', 'blue', 4)
obj_rectangle = Rectangle()
obj_triangle = Triangle(10, 'blue', 'blue', 3)
obj_circle = Circle(10, 'blue', 'blue', 360)


def circular_mondrian(x, y, s, numRectangles = 200):
    """Create a circular Mondrian scene that chooses 
       the number of rectangles and fill 40% of them
    """
    goto(x, y)
    posa = random.randint(x + s*3, x + s*20)
    posb = random.randint(y + s*3, y + s*20)
    colorDict = {1: 'black', 2: 'blue', 3: 'red'}
    for i in range(numRectangles):
        radius = abs(s*100 - x)
        posx = random.randint(posa - radius, posa + radius)
        ymultiply = [-1, 1]
        multiply = random.randint(0, 1)
        posy = ymultiply[multiply]*random.randint(0, int(math.sqrt(radius**2 - (posx - posa)**2))) + posb
        fillColorR = random.random()
        fillColorG = random.random()
        fillColorB = random.random()
        turt.width(2)
        numberOfFill = random.random()
        if numberOfFill <= 0.4:
            obj_rectangle.drawShape(posx, posy, 10, edgeColor = colorDict[random.randint(1, 3)], fillColor = (fillColorR, fillColorG, fillColorB), fill = True)
        else:
            obj_rectangle.drawShape(posx, posy, 10, edgeColor = 'black', fillColor = 'white', fill = False)


def triangleStatue(x, y, scale):
    """Draws a statue made up of triangles
    """
    setsColor = {'indian red', 'crimson', 'firebrick'}
    turt.width(4)
    obj_triangle.drawShape(x, y, 10*scale, setsColor.pop(), 'indian red')
    obj_triangle.drawShape(x - 0.9*scale, y - 5*scale, 12*scale, setsColor.pop(), 'crimson')
    obj_triangle.drawShape(x - 1.7*scale, y - 10*scale, 14*scale, setsColor.pop(), 'firebrick')


def anotherStatue(x, y, scale):
    """Draws a statue made up of a square and a circle
    """
    setsColor = {'dark slate blue', 'light slate blue'}
    turt.setheading(270)
    obj_square.drawShape(x, y, 100*scale, setsColor.pop(), 'dark slate blue')
    obj_circle.drawShape(x - 20*scale, y + 10*scale, 0.5*scale, setsColor.pop(), 'light slate blue')


def string(x, y, distance):
    """Draws a string/line
    """
    goto(x, y)
    turt.color('black')
    turt.width(3)
    turt.setheading(270)
    turt.forward(distance)


def main():
    """Draws the Sculpture Gallery
    """
    s.tracer(False)
    turt.hideturtle()
    make_window('Sculpture Gallery', 'alice blue', 1000, 700)
    obj_square.drawShape(-500, -100, 1000, 'cadet blue', 'cadet blue')
    string(0, 350, 100)
    circular_mondrian(0, 160, 1, numRectangles = 200)
    triangleStatue(-350, 0, 18)
    anotherStatue(380, -50, 2.2)
#     s.exitonclick()


# if __name__ == '__main__':
#     main()