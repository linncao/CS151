"""Linn Cao Nguyen Phuong
   Sep 17, 2020
   Section A
   Project 3: Scenes within scenes
   CS151
"""

import turtle
import random
import sys
import better_shapelib as bsl


def museum(edgeColor = 'dim gray', fillColor = 'gray'):
    """Draws an interior museum scene.
       Requires a command-line argument to change the color of the statue's lower part. 
       The following makes the edge color gray and fill color black: python museum.py gray black
       The following makes the edge color red and fill color blue: python museum.py red blue
    """
    # put several calls to functions from better_shapelib
    bsl.myScene(-112.5, -130, 1.5)
    bsl.parallelogram_mondrian(-320, -85, 0.6, True, numParallelograms = 150)
    bsl.parallelogram_mondrian(200, -85, 0.6, False, numParallelograms = 150)
    bsl.mondrian(-100, -140, 0.5, numRectangles = 80)
    bsl.circular_mondrian(-15, 70, 1, numRectangles = 80)
    bsl.statue(-2, -270, 1.2, edgeColor = edgeColor, fillColor = fillColor)

# main code
if __name__=='__main__':
    edgeColor = sys.argv[1]
    fillColor = sys.argv[2]
    museum(edgeColor, fillColor)

turtle.hideturtle()
turtle.exitonclick()