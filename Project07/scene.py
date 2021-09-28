"""Linn Cao Nguyen Phuong
   Oct 20, 2020
   Section A
   Project 7: Animation Scene
   CS151
"""

import graphics as gr
import compound_shapes as cs 
import time
import sys
		

def scene(screen, speed):
    """Places the bird, pipes, background
       at desired locations and scales.
       Puts them into motion using an animation loop
    """
    bird = cs.bird_init(100, 400, 4.5)
    pipes = cs.pipes_init(290, -10, 1)
    background = cs.background_init(-10, 700, 2.5)
    shapes = []
    for bg in background:
        for b in bg:
            shapes.append(b)
    shapes.append(bird)
    for pipe in pipes:
        shapes.append(pipe)
    for shape in shapes:
        for i in shape:
            i.draw(screen)
    for i in range(175):
        cs.background_animate(background, i, screen)
        cs.pipes_animate(pipes, i, screen)
        cs.bird_animate(bird, i, screen)
        time.sleep(float(speed))
        if screen.checkMouse() is not None:
            break
    for shape in shapes:
        for i in shape:
            i.undraw( )


def main(title, speed):
    """Draws the scene onto the screen.
       Requires a command-line argument to change the speed and name of the scene. 
       The following changes the scene's speed into 0.01 and name into Flappy Bird: python scene.py 0.01 Flappy Bird
       The following changes the scene's speed into 0.1 and name into Flappy Bird Slower: python scene.py 0.1 Flappy Bird Slower
    """
    screen = gr.GraphWin(title, width=1100, height=800)
    screen.setBackground(gr.color_rgb(135, 206, 250))
    for i in range(1000):
        scene(screen, speed)
    screen.update()
    screen.getMouse()
    screen.close()


if __name__ == '__main__':
    speed = sys.argv[1]
    title = ' '.join(map(str, sys.argv[2:]))
    main(title, speed)