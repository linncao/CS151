"""Linn Cao Nguyen Phuong
   Nov 10th, 2020
   Section A
   Project 9: L-systems in Nature
   CS151
"""

import lsystem as ls
import turtle_interpreter as ti
import random

def main():
    """Arranges trees made from 3 Lsystem text files into a scene
       2 files contain Lsystem of 2+ rules
    """
    tree1 = ls.Lsystem('systemCL.txt')
    tree2 = ls.Lsystem('systemFL.txt')
    tree3 = ls.Lsystem('systemDL.txt')
    mountain = ls.Lsystem('mountain.txt')
    s = '<gFF---FF[----FF]F[--FF]FF---FF---FFFFF>'
    terp = ti.TurtleInterpreter(800, 600)
    tstr1 = tree1.buildString(3)
    tstr2 = tree2.buildString(3)
    tstr3 = tree3.buildString(4)
    tstr4 = mountain.buildString(1)
    terp.setWidth(2)
    for i in range(150):
        star = '<yH>'
        terp.place(random.gauss(-400, 400), random.gauss(150, 300), 90)
        terp.drawString(star, 10, 40)
    terp.setColor('saddle brown')
    terp.fill('tan')
    terp.place(-400, -15, 0)
    terp.drawString(tstr4, 250, 120)
    terp.place(-155, -15, 0)
    terp.drawString(tstr4, 300, 120)
    terp.place(140, -15, 0)
    terp.drawString(tstr4, 200, 120)
    terp.end()
    terp.setColor('yellow green')
    terp.fill('yellow green')
    terp.place(-400, -335, 90)
    terp.drawString(s, 160, 30)
    terp.end()
    terp.setColor('sienna')
    terp.place(-150, -100, 90)
    terp.drawString(tstr1, 10, 22.5)
    terp.place(150, -100, 90)
    terp.drawString(tstr1, 10, -22.5)
    terp.place(-320, -170, 90)
    terp.drawString(tstr2, 10, 2)
    terp.place(320, -170, 90)
    terp.drawString(tstr2, 10, -2)
    terp.place(-250, -250, 90)
    terp.drawString(tstr3, 3, 5)
    terp.place(250, -250, 90)
    terp.drawString(tstr3, 3, -5)
    for i in range(100):
        grass = '<g[-L][+L]>'
        terp.place(random.gauss(-370, 370), random.gauss(-280, 130), 60)
        terp.drawString(grass, 10, 40)
    terp.hold()


if __name__ == '__main__':
    main()