"""Linn Cao Nguyen Phuong
   Dec 1, 2020
   Section A
   Final Project
   CS151
"""

import turtle
import scene4 as s4

s = turtle.Screen()
turt = turtle.Turtle()

def write(turt, text, size):
	"""Replaces the turtle with a desired text
	   in Arial, size, style bold
	"""
	turt.clear()
	turt.write(text, font=('Arial', size, 'bold'))
	turt.hideturtle()


def main():
   """Draws sculpture and info
   """
   s.tracer(False)
   s4.make_window('Sculpture Gallery, Sculpture 1', 'alice blue', 1000, 700)
   turt.setheading(270)
   s4.anotherStatue(-100, 100, 3.5)
   info = s4.make_turtle('circle', 'dark slate blue', 0.1, 0.1, 30, -30)
   write(info, 'Sculpture 3\nArtist: Linn Cao\nCreated on Nov 26, 2020', 20)
   # s.exitonclick()


# if __name__ == '__main__':
#    main()