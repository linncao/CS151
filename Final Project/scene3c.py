"""Linn Cao Nguyen Phuong
   Dec 1, 2020
   Section A
   Final Project
   CS151
"""

import lsystem as ls
import turtle_interpreter as ti

def tree3(terp, tstr3):
    """Draws tree
    """
    terp.place(-310, -280)
    terp.orient(90)
    terp.setColor((0.5, 0.4, 0.3))
    terp.drawString(tstr3, 10, 20)


def text(terp):
    """Writes info of tree
    """
    terp.place(-10, -90)
    terp.setColor((0.7, 0.2, 0.3))
    terp.write('Tree Type 3\nFounder: The Algorithmic Beauty of Plants\nPlanter: Linn Cao\nFound on Nov 10, 2020\nPlanted on Nov 26, 2020', 17)
    terp.place(-100, -330)
    terp.setColor((0.15, 0.5, 0.2))


def main():
    """Draws tree and info
    """
    terp = ti.TurtleInterpreter(1000, 700)
    terp.title('Greenhouse, Tree 3')
    terp.bgcolor('snow')
    tree = ls.Lsystem('systemFL.txt')
    tstr3 = tree.buildString(5)
    tree3(terp, tstr3)
    text(terp)
    # terp.hold()
    

# if __name__ == '__main__':
#     main()