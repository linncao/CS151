"""Linn Cao Nguyen Phuong
   Oct 20, 2020
   Section A
   Lab 7: Animating Shape Objects
   CS151
"""

import graphicsPlus as gr
import time


def draw(shape_list, win):
    """Draws the shape in the shape list onto the screen
    """
	for shape in shape_list:
		shape.draw( win )
		

def undraw(shape_list, win):
    """Undraws the shape in the shape list from the screen
    """
	for shape in shape_list:
		shape.undraw( )
		

def move(shape_list, dx, dy):
    """Moves the shape in the shape list
       dx units in x direction and dy units in y direction
    """
	for shape in shape_list:
		shape.move( dx, dy )
		

def snowman_init(x, y, scale):
    """Draws a snowman at desired location and scale
    """
    shapes = []
    radius = 30
    eyeRadius = 3
    head = gr.Circle(gr.Point(x, y), radius)
    body = gr.Circle(gr.Point(x, y + 2*radius*scale), radius)
    bottom = gr.Circle(gr.Point(x, y + 4*radius*scale), radius)
    eye1 = gr.Circle(gr.Point(x - scale*radius/2, y), eyeRadius)
    eye2 = gr.Circle(gr.Point(x + scale*radius/2, y), eyeRadius)
    shapes.append(head)
    shapes.append(body)
    shapes.append(bottom)
    shapes.append(eye1)
    shapes.append(eye2)
    return shapes


def snowman_animate(shapes, frame, screen):
    """Animates the snowman, controls how it moves for each frame
    """
    if frame % 2 == 0:
        for shape in shapes:
            shape.move(10, 5)
    else:
        for shape in shapes:
            shape.move(-10, 5)


def snowman_test():
    """Tests the snow man animation
    """
    screen = gr.GraphWin('Snowman Test', width=600, height=600)
    snowman = snowman_init(300, 300, 1)
    for shapes in snowman:
        shapes.draw(screen)
    for i in range(20):
        snowman_animate(snowman, i, screen)
        time.sleep(0.5)
        if screen.checkMouse() is not None:
            break
    screen.getMouse()
    screen.close()


if __name__=='__main__':
    snowman_test()