"""Linn Cao Nguyen Phuong
   Dec 1, 2020
   Section A
   Final Project
   CS151
"""

import lsystem as ls
import turtle_interpreter as ti

def ground(terp, s1, s3):
    """Draws the ground
    """
    terp.place(-500, -50)
    terp.setWidth(4)
    terp.setColor('silver')
    terp.fill()
    terp.drawString(s1, 100, 90)
    terp.end()
    terp.place(-250, -52)
    terp.orient(300)
    terp.setColor('yellow green')
    terp.fill()
    terp.drawString(s3, 70, 15)
    terp.end()
    terp.place(-500, -50)
    terp.orient(335)
    terp.setColor('yellow green')
    terp.fill()
    terp.drawString(s3, 120, -18)
    terp.end()
    terp.place(500, -50)
    terp.orient(205)
    terp.setColor('yellow green')
    terp.fill()
    terp.drawString(s3, 120, 18)
    terp.end()


def dome(terp, s2):
    """Draws the dome
    """
    terp.setWidth(5)
    terp.place(-125, 350)
    terp.orient(240)
    terp.drawString(s2, 70, 5)
    terp.place(125, 350)
    terp.orient(300)
    terp.drawString(s2, 70, -5)
    terp.place(-305, 350)
    terp.orient(220)
    terp.drawString(s2, 80, 6)
    terp.place(305, 350)
    terp.orient(320)
    terp.drawString(s2, 80, -6)


def treeCenter(terp, tstr1, tstr1a, tstr1b):
    """Draws the trees in the center
    """
    terp.place(0, -160)
    terp.orient(90)
    terp.setWidth(1)
    terp.setColor((0.5, 0.4, 0.3))
    terp.drawString(tstr1, 8, 30)
    terp.place(-180, -80)
    terp.orient(90)
    terp.drawString(tstr1a, 14, 30)
    terp.place(180, -80)
    terp.orient(90)
    terp.drawString(tstr1b, 34, 30)


def treeLeft(terp, tstr2, tstr2a, tstr2b):
    """Draws the trees on the left
    """
    terp.place(-355, -230)
    terp.orient(90)
    terp.drawString(tstr2, 12, 30)
    terp.place(-450, -290)
    terp.orient(90)
    terp.drawString(tstr2a, 16, 18)
    terp.place(-280, -330)
    terp.orient(90)
    terp.drawString(tstr2b, 30, 25)


def treeRight(terp, tstr3, tstr3a, tstr3b):
    """Draws the trees on the right
    """
    terp.place(355, -230)
    terp.orient(90)
    terp.drawString(tstr3, 12, -30)
    terp.place(450, -290)
    terp.orient(90)
    terp.drawString(tstr3a, 16, -18)
    terp.place(280, -330)
    terp.orient(90)
    terp.drawString(tstr3b, 30, -25)


def main():
    """Draws the greenhouse
    """
    terp = ti.TurtleInterpreter(1000, 700)
    terp.title('Greenhouse')
    terp.bgcolor('pale turquoise')
    tree1 = ls.Lsystem('tree.txt')
    tree2 = ls.Lsystem('systemCL.txt')
    tree3 = ls.Lsystem('systemFL.txt')
    tstr1 = tree1.buildString(3)
    tstr1a = tree1.buildString(2)
    tstr1b = tree1.buildString(1)
    tstr2 = tree2.buildString(3)
    tstr2a = tree2.buildString(2)
    tstr2b = tree2.buildString(1)
    tstr3 = tree3.buildString(4)
    tstr3a = tree3.buildString(3)
    tstr3b = tree3.buildString(2)
    s1 = '<gFFFFFFFFFF-FFF-FFFFFFFFFF-FFF>'
    s2 = '<bF+F+F+F+F+F>'
    s3 = '<gF+F+F+F+F+F+F+F+F>'
    ground(terp, s1, s3)
    dome(terp, s2)
    treeCenter(terp, tstr1, tstr1a, tstr1b)
    treeLeft(terp, tstr2, tstr2a, tstr2b)
    treeRight(terp, tstr3, tstr3a, tstr3b)
    # terp.hold()


# if __name__ == '__main__':
#     main()
#     terp.hold()