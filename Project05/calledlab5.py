"""Linn Cao Nguyen Phuong
   Sep 17, 2020
   Section A
   Lab 4: Unique turtles
   CS151
"""

import random
import turtle

s = turtle.Screen()

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


def writeTrial(turt, text, numTrials):
	"""Replaces the turtle with a desired text with counter variable
	   in Arial, size 20, style normal
	"""
	turt.clear()
	turt.write(text + str(numTrials), font=('Arial', 20, 'normal'))
	turt.hideturtle()


def writeResult(turt, text):
	"""Replaces the turtle with a desired text
	   in Arial, size 20, style normal
	"""
	turt.clear()
	turt.write(text, font=('Arial', 20, 'normal'))
	turt.hideturtle()

# Return True if win, False if lose
def game(numTrials, gravity, speed):
	"""Writes the game's properties
	"""
	s.clearscreen()
	window = make_window('Soaring Thunderbird - A CS151 original!', 'light sky blue', 800, 600)
	window.bgpic('sky.gif')  # you can set the background to a gif image
	# airport
	airport = make_turtle('square', 'dark gray', 1, 5, 0, -295)
	window.addshape('glider_image_left.gif')
	window.addshape('glider_image_right.gif')
	window.addshape('bird1.gif')
	result1 = make_turtle('circle', 'black', 0.1, 0.1, -60, 250)
	result2 = make_turtle('circle', 'black', 0.1, 0.1, -85, 215)
	result3 = make_turtle('circle', 'black', 0.1, 0.1, -85, 180)
	bird1 = make_turtle('bird1.gif', 'black', 0.1, 0.1, -400, 50)
	bird2 = make_turtle('bird1.gif', 'black', 0.1, 0.1, -400, -50)
	bird1.setheading(0)
	bird2.setheading(0)
	# glider
	glider = make_turtle('glider_image_right.gif', 'white', 0.51, 0.51, 0, 300)
	def go_left():
		glider.setheading(180)
		glider.left(gravity)
		glider.shape('glider_image_left.gif')
	def go_right():
		glider.setheading(0)
		glider.right(gravity)
		glider.shape('glider_image_right.gif')
	window.onkeypress(go_left, 'Left')
	window.onkeypress(go_right, 'Right')
	writeTrial(result1, 'Trial: ', numTrials)
	writeTrial(result2, 'Gravity: ', gravity)
	writeTrial(result3, 'Speed: ', speed)
	window.tracer(False)
	window.listen()
	while True:
		window.update()
		glider.forward(speed)
		bird1.forward(0.05)
		bird2.forward(0.1)
		xb1 = bird1.xcor()
		yb1 = bird1.ycor()
		xb2 = bird2.xcor()
		yb2 = bird2.ycor()
		xgl = glider.xcor()
		ygl = glider.ycor()
		if xb1 > 400:
			bird1.goto(-400, 50)
		if xb2 > 400:
			bird2.goto(-400, -50)
		if xgl < -400 or xgl > 400 or ygl < -300 or xgl <= xb1+15 and ygl <= yb1+15 and xgl >= xb1-15 and ygl >= yb1-15 or xgl <= xb2+15 and ygl <= yb2+15 and xgl >= xb2-15 and ygl >= yb2-15:
			return False
		if xgl > -50 and xgl < 50 and ygl <= -273:
			return True


def main():
	"""Writes the game's win and lose scenarios
	"""
	numTrials = 1
	gravity = 10
	speed = 0.1
	while True:
		result = game(numTrials, gravity, speed)
		if result == False:
			restart = s.textinput("Game result", "You lose :( \nDo you want to restart ? (Yes/No)")
			if restart == "Yes":
				numTrials += 1
				gravity += 5
				speed += 0.1
				continue
			else:
				break
		if result == True:
			restart = s.textinput("Game result", "You win :) \nDo you want to restart ? (Yes/No)")
			if restart == "Yes":
				main()
			else:
				break


if __name__ == "__main__":
	main()