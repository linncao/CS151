"""Linn Cao Nguyen Phuong
   Sep 17, 2020
   Section A
   Lab 4: Unique turtles
   CS151
"""

import random
import turtle

s = turtle.Screen()

def make_screen(width, height, title, color = 'black'):
    """Makes a 'Screen' object: the window in each turtles can draw shapes

    Parameters:
    -----------
    width: int.
        The width of the window/screen in pixels.
    height: int.
        The height of the window/screen in pixels.
    title: str.
        The name that you'd like to call the pop-up window. Appears at the center of top of the window.
    color: str.
        Color string name (e.g. 'black', 'white', etc). This is the background color of the screen.
    
    Returns:
    -----------
    The 'Screen' object that you create.
    """
    s.setup(height = height, width = width)
    s.bgcolor(color)
    s.title(title)
    return s


def make_turtle(shape = 'turtle', penColor = 'white', fillColor = 'black'):
    """Makes a 'Turtle' object

    Parameters:
    -----------
    shape: str.
        From the turtle documentation website, possible options are:
        'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
    pencolor: str.
        Color string name (e.g. 'black', 'white', etc) that is to be the pen color of this turtle.

    Returns:
    -----------
    The 'Turtle' object that you created.
    """
    d1 = turtle.Turtle()
    d1.shape(shape)
    d1.color(penColor, fillColor)
    d1.penup()
    return d1


def reset_turtle(turt, screen_width, screen_height):
    """Returns the turtle to a random position 
       on the top of the screen
    """
    turt.goto(random.randint(-screen_width/2, screen_width/2), screen_height/2)
    turt.setheading(270)
    turt.color(random.random(), random.random(), random.random())


def move_and_stamp(turt, distance):
    """Moves and stamps the turtle
    """
    turt.stamp()
    turt.forward(distance)


def writeNumStrides(turt, numStrides):
    """Replaces the turtle with a desired text
       in Arial, size 30, style normal
    """
    turt.clear()
    turt.write(numStrides, font=('Arial', 30, 'normal'))
    turt.hideturtle()


def main():
    """Puts several calls to functions above,
       creates 4 turtles which keep running from the top 
       to the bottom of the screen from different y cordinates
       to create a 'rain code'
    """
    screen = make_screen(500, 400, 'linnxinhhihi', 'salmon')
    turt1 = make_turtle('turtle', 'light blue', 'light pink')
    turt2 = make_turtle('square', 'slate gray', 'alice blue')
    turt3 = make_turtle('arrow', 'white', 'orange')
    turt4 = make_turtle('circle', 'white', 'white')
    turt1.speed(0)
    turt2.speed(0)
    turt3.speed(0)
    turt4.speed(0)
    turt1.goto(-200, 0)
    turt2.goto(-50, -50)
    turt3.goto(100, 100)
    turt4.goto(0, -200)
    reset_turtle(turt1, 500, 400)
    reset_turtle(turt2, 500, 400)
    reset_turtle(turt3, 500, 400)
    stride = 0
    while stride <= 1000:
        move_and_stamp(turt1, random.randint(40, 50))
        move_and_stamp(turt2, random.randint(30, 40))
        move_and_stamp(turt3, random.randint(20, 30))
        y1 = turt1.ycor()
        y2 = turt2.ycor()
        y3 = turt3.ycor()
        if y1 < -250:
            reset_turtle(turt1, 500, 400)
            stride += 1
            print("turts complete", stride, "strides.")
            writeNumStrides(turt4, stride)
        if y2 < -250:
            reset_turtle(turt2, 500, 400)
            stride += 1
            print("turts complete", stride, "strides.")
            writeNumStrides(turt4, stride)
        if y3 < -250:
            reset_turtle(turt3, 500, 400)
            stride += 1
            print("turts complete", stride, "strides.")
            writeNumStrides(turt4, stride)


if __name__ == '__main__':
    main()

s.exitonclick()