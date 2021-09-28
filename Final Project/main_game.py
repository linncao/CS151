"""Linn Cao Nguyen Phuong
   Dec 1, 2020
   Section A
   Final Project
   CS151
"""

import scene1 as s1
import scene2 as s2
import scene3 as s3
import scene3a as s3a
import scene3b as s3b
import scene3c as s3c
import scene4 as s4
import scene4a as s4a
import scene4b as s4b
import scene4c as s4c
import scene5 as s5
import scene6 as s6
import scene6a as s6a
import scene6b as s6b
import scene6c as s6c
import turtle

s = turtle.Screen()

def gallery1():
    """Draws Greenhouse and each tree's info
    """
    def left():
        """Draws 1st tree and info
        """
        s.clearscreen()
        s.tracer(False)
        s3a.main()                                  
        return s.textinput('Greenhouse, Tree 1', 'Which other type of tree do you want to see? (Center/Right)\nDo you want to exit to the map? (Exit)')


    def center():
        """Draws 2nd tree and info
        """
        s.clearscreen()
        s.tracer(False)
        s3b.main()                                 
        return s.textinput('Greenhouse, Tree 2', 'Which other type of tree do you want to see? (Left/Right)\nDo you want to exit to the map? (Exit)')


    def right():
        """Draws 3rd tree and info
        """
        s.clearscreen()
        s.tracer(False)
        s3c.main()                                   
        return s.textinput('Greenhouse, Tree 3', 'Which other type of tree do you want to see? (Left/Center)\nDo you want to exit to the map? (Exit)')


    s.clearscreen()
    s3.main()                                   
    scene3 = s.textinput('Greenhouse', 'Which type of tree do you want to see? (Left/Center/Right)\nDo you want to exit to the map? (Exit)')
    while scene3 != 'Exit': 
        if scene3 == 'Left':
            scene3 = left()
        elif scene3 == 'Center':
            scene3 = center()
        elif scene3 == 'Right':
            scene3 = right()


def gallery2():
    """Draws Sculpture Gallery and each sculpture's info
    """
    def left():
        """Draws 1st Sculpture and info
        """
        s.clearscreen()
        s.tracer(False)
        s4a.main()                              
        return s.textinput('Sculpture Gallery, Sculpture 1', 'Which other sculpture do you want to see? (Center/Right)\nDo you want to exit to the map? (Exit)')


    def center():
        """Draws 2nd Sculpture and info
        """
        s.clearscreen()
        s.tracer(False)
        s4b.main()                                 
        return s.textinput('Sculpture Gallery, Sculpture 2', 'Which other sculpture do you want to see? (Left/Right)\nDo you want to exit to the map? (Exit)')


    def right():
        """Draws 3rd Sculpture and info
        """
        s.clearscreen()
        s.tracer(False)
        s4c.main()                                
        return s.textinput('Sculpture Gallery, Sculpture 3', 'Which other sculpture do you want to see? (Left/Center)\nDo you want to exit to the map? (Exit)')


    s.clearscreen()
    s4.main()                             
    scene4 = s.textinput('Sculpture', 'Which sculpture do you want to see? (Left/Center/Right)\nDo you want to exit to the map? (Exit)')
    while scene4 != 'Exit': 
        if scene4 == 'Left':
            scene4 = left()
        elif scene4 == 'Center':
            scene4 = center()
        elif scene4 == 'Right':
            scene4 = right()


def gallery3():
    """Draws Futuristic Gallery
    """
    s.clearscreen()
    s5.main()
    scene5 = s.textinput('Futuristic Gallery', 'Do you want to replay or exit to the map? (Replay/Exit)')
    while scene5 != 'Exit':
        s.clearscreen()
        s5.main()
        scene5 = s.textinput('Futuristic Gallery', 'Do you want to replay or exit to the map? (Replay/Exit)')


def gallery4():
    """Draws Painting Gallery and each painting's info
    """
    def left():
        """Draws 1st Artwork and info
        """
        s.clearscreen()
        s.tracer(False)
        s6a.main()                            
        return s.textinput('Painting Gallery, Artwork 1', 'Which other painting do you want to see? (Center/Right)\nDo you want to exit to the map? (Exit)')


    def center():
        """Draws 2nd Artwork and info
        """
        s.clearscreen()
        s.tracer(False)
        s6b.main()                               
        return s.textinput('Painting Gallery, Artwork 2', 'Which other painting do you want to see? (Left/Right)\nDo you want to exit to the map? (Exit)')


    def right():
        """Draws 3rd Artwork and info
        """
        s.clearscreen()
        s.tracer(False)
        s6c.main()                            
        return s.textinput('Painting Gallery, Artwork 3', 'Which other painting do you want to see? (Left/Center)\nDo you want to exit to the map? (Exit)')


    s.clearscreen()
    s6.main()                        
    scene6 = s.textinput('Painting Gallery', 'Which painting do you want to see? (Left/Center/Right)\nDo you want to exit to the map? (Exit)')
    while scene6 != 'Exit': 
        if scene6 == 'Left':
            scene6 = left()
        elif scene6 == 'Center':
            scene6 = center()
        elif scene6 == 'Right':
            scene6 = right()

                
def main():
    """The main game
    """
    s1.main(True)                                      
    scene1 = s.textinput('Begin game', 'Do you want to enter the museum? (Yes/No)')
    while scene1 == 'Yes':
        s.clearscreen()
        s2.main()                                      
        scene2 = s.textinput('Museum Map', 'Which gallery do you want to visit? (1/2/3/4)\nDo you want to exit the museum? (Exit)')
        while scene2 != 'Exit':
            if scene2 == '1':
                gallery1()
            elif scene2 == '2':
                gallery2()
            elif scene2 == '3':
                gallery3()
            elif scene2 == '4':
                gallery4()
            s.clearscreen()
            s2.main()
            scene2 = s.textinput('Museum Map', 'Which gallery do you want to visit? (1/2/3/4)\nDo you want to exit the museum? (Exit)')
        s.clearscreen()  
        s1.main(False)                                   
        s.exitonclick()
    s.clearscreen()  
    s1.main(False)                                   
    s.exitonclick()


if __name__ == '__main__':
    main()