"""Linn Cao Nguyen Phuong
   Dec 1, 2020
   Section A
   Final Project
   CS151
"""

import lsystem as ls
import turtle_interpreter as ti

def tree2(terp, tstr2):
    """Draws tree
    """
    terp.place(-250, -280)
    terp.orient(90)
    terp.setColor((0.5, 0.4, 0.3))
    terp.drawString(tstr2, 11, 30)


def text(terp):
    """Writes info of tree
    """
    terp.place(50, -80)
    terp.setColor((0.7, 0.2, 0.3))
    terp.write('Tree Type 2\nPlanter/Founder: Linn Cao\nFound on Nov 10, 2020\nPlanted on Nov 26, 2020', 20)
    terp.place(-100, -325)
    terp.setColor((0.15, 0.5, 0.2))


def main():
    """Draws tree and info
    """
    terp = ti.TurtleInterpreter(1000, 700)
    terp.title('Greenhouse, Tree 2')
    terp.bgcolor('snow')
    tree = ls.Lsystem('tree.txt')
    tstr2 = tree.buildString(3)
    tree2(terp, tstr2)
    text(terp)
    # terp.hold()
    

# if __name__ == '__main__':
#     main()