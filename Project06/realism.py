"""Linn Cao Nguyen Phuong
   Oct 6, 2020
   Section A
   Lab 4: Unique turtles
   CS151
"""


import graphicsPlus as gr
import complex_shape as cs 
import sys


def main(r = 255, g = 255, b = 240):
    """Draws the Social Realism scene.
       Requires a command-line argument to change the color of the background. 
       The following changes the background's color into RGB(255, 255, 240): python realism.py 255 255 240
       The following changes the background's color into RGB(135, 206, 235): python realism.py 135 206 235
    """
    win = gr.GraphWin('Vietnam\'s street mural', 620, 700)
    win.setBackground(gr.color_rgb(r = int(r), g = int(g), b = int(b)))
    human1 = cs.human1_init(30, 10, 1)
    human2 = cs.human2_init(-100, -110, 1)
    human3 = cs.human3_init(30, -210, 1)
    human4 = cs.human4_init(-100, -310, 1)
    sun = cs.sun_init(0, 0, 1)
    haystack1 = cs.haystack_init(0, 0, 1)
    haystack2 = cs.haystack_init(-610, 120, 0.8)
    scene = []
    scene.append(sun)
    scene.append(human4)
    scene.append(human3)
    scene.append(human2)
    scene.append(haystack1)
    scene.append(haystack2)
    scene.append(human1)
    for complex_shape in scene:
        for shape in complex_shape:
            cs.draw(shape, win)
    win.update()
    win.getMouse()
    win.close()


if __name__ == '__main__':
    color = sys.argv[1]
    main(color)