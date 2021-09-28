"""Linn Cao Nguyen Phuong
   Nov 10th, 2020
   Section A
   Project 9: L-systems in Nature
   CS151
"""

import lsystem as ls
import turtle_interpreter as ti

def main():
   """Draws 3 trees from Lsystem in tree.txt 
      with 1, 2, 3 iterations from left to right
   """
   tree = ls.Lsystem('tree.txt')
   terp = ti.TurtleInterpreter(1200, 800)
   tstr1 = tree.buildString(1)
   terp.setWidth(1.5)
   terp.setColor((0.5, 0.4, 0.3))
   terp.place(-460, -350, 90)
   terp.drawString(tstr1, 60, 30)
   tstr2 = tree.buildString(2)
   terp.place(-135, -350, 90)
   terp.drawString(tstr2, 30, 30)
   tstr3 = tree.buildString(3)
   terp.place(320, -350, 90)
   terp.drawString(tstr3, 13, 30)
   terp.hold()


if __name__ == '__main__':
   main()