"""Linn Cao Nguyen Phuong
   Dec 1, 2020
   Section A
   Final Project
   CS151
"""

import lsystem as ls
import turtle_interpreter as ti

def tree1(terp, tstr1):
    """Draws tree
    """
    terp.place(-310, -280)
    terp.orient(90)
    terp.setColor((0.5, 0.4, 0.3))
    terp.drawString(tstr1, 22, 30)


def text(terp):
    """Writes info of tree
    """
    terp.place(0, -80)
    terp.setColor((0.7, 0.2, 0.3))
    terp.write('Tree Type 1\nFounder: The Algorithmic Beauty of Plants\nPlanter: Linn Cao\nFound on Nov 10, 2020\nPlanted on Nov 26, 2020', 17)
    terp.place(-100, -330)
    terp.setColor((0.15, 0.5, 0.2))


def main():
    """Draws tree and info
    """
    terp = ti.TurtleInterpreter(1000, 700)
    terp.title('Greenhouse, Tree 1')
    terp.bgcolor('snow')
    tree = ls.Lsystem('systemCL.txt')
    tstr1 = tree.buildString(3)
    tree1(terp, tstr1)
    text(terp)
    # terp.hold()
    

# if __name__ == '__main__':
#     main()
#     terp.hold()