"""Linn Cao Nguyen Phuong
   Oct 20, 2020
   Section A
   Project 7: Animation Scene
   CS151
"""

import graphics as gr
import time

		
def draw(shape_list, win):
    """Draws the shape in the shape list onto the screen
    """
    for shape in shape_list:
        shape.draw(win)


def undraw(shape_list, win):
    """Undraws the shape in the shape list from the screen
    """
    for shape in shape_list:
        shape.undraw( )


def move(shape_list, dx, dy):
    """Moves the shape in the shape list
       dx units in x direction and dy units in y direction
    """
    for shape in shape_list:
        shape.move(dx, dy)


def bird_init(x, y, scale):
    """Draws a bird at desired location and scale
    """
    shapes = []
    body = gr.Oval(gr.Point(x, y), gr.Point(x + 20*scale, y + 15*scale))
    body.setFill(gr.color_rgb(255, 215, 0))
    body.setWidth(scale)
    wing = gr.Oval(gr.Point(x - 2.5*scale, y + 5*scale), gr.Point(x + 8*scale, y + 12.5*scale))
    wing.setFill(gr.color_rgb(255, 215, 0))
    wing.setWidth(scale)
    eye1 = gr.Circle(gr.Point(x + 15.25*scale, y + 4.2*scale), 3.1*scale)
    eye1.setFill(gr.color_rgb(255, 255, 240))
    eye1.setWidth(scale)
    eye2 = gr.Circle(gr.Point(x + 16.25*scale, y + 4.2*scale), 0.8*scale)
    eye2.setFill(gr.color_rgb(0, 0, 0))
    lip1 = gr.Oval(gr.Point(x + 13*scale, y + 8.2*scale), gr.Point(x + 22*scale, y + 10.4*scale))
    lip1.setFill(gr.color_rgb(255, 99, 0))
    lip1.setWidth(scale)
    lip2 = gr.Oval(gr.Point(x + 13*scale, y + 10.4*scale), gr.Point(x + 20.5*scale, y + 12.5*scale))
    lip2.setFill(gr.color_rgb(255, 99, 0))
    lip2.setWidth(scale)
    shapes.append(body)
    shapes.append(wing)
    shapes.append(eye1)
    shapes.append(eye2)
    shapes.append(lip1)
    shapes.append(lip2)
    return shapes


def bird_animate(shapes, frame, screen, scale):
    """Animates the bird, controls how it moves for each frame
    """
    if frame <= 40*scale:
        for shape in shapes:
            shape.move(0, 2)
    if 40*scale <= frame <= 90*scale:
        for shape in shapes:
            shape.move(0, -5)
    if 90*scale <= frame <= 175*scale:
        for shape in shapes:
            shape.move(0, 1.5)


def bird_test():
    """Tests the bird animation 
    """
    screen = gr.GraphWin('Flappy Bird', width=1100, height=800)
    screen.setBackground(gr.color_rgb(135, 206, 250))
    bird1 = bird_init(100, 400, 4.5)
    bird2 = bird_init(500, 300, 7)
    bird3 = bird_init(300, 600, 5)
    shapes = []
    shapes.append(bird1)
    shapes.append(bird2)
    shapes.append(bird3)
    for shape in shapes:
        for i in shape:
            i.draw(screen)
    for i in range(100):
        bird_animate(bird1, i, screen, 1)
        bird_animate(bird2, i, screen, 1)
        bird_animate(bird3, i, screen, 1)
        time.sleep(0.1)
        if screen.checkMouse() is not None:
            break
    screen.update()
    screen.getMouse()
    screen.close()



def pipe_init(x, y, scale):
    """Draws a pipe at desired location and scale
    """
    shapes = []
    rect1 = gr.Rectangle(gr.Point(x, y), gr.Point(x + 100*scale, y + 400*scale))
    rect1.setFill(gr.color_rgb(154, 205, 50))
    rect1.setWidth(5*scale)
    rect2 = gr.Rectangle(gr.Point(x - 15*scale, y + 400*scale), gr.Point(x + 115*scale, y + 450*scale))
    rect2.setFill(gr.color_rgb(154, 205, 50))
    rect2.setWidth(5*scale)
    rect3 = rect2.clone()
    rect3.move(0, 190*scale)
    rect4 = rect1.clone()
    rect4.move(0, 640*scale)
    shapes.append(rect1)
    shapes.append(rect2)
    shapes.append(rect3)
    shapes.append(rect4)
    return shapes


def pipes_init(x, y, scale):
    """Draws 3 pipes at desired location and scale
    """
    shapes = []
    pipe1 = pipe_init(x, y, scale)
    pipe2 = pipe_init(x + 350*scale, y - 225*scale, scale)
    pipe3 = pipe_init(x + 700*scale, y - 170*scale, scale)
    pipe4 = pipe_init(x + 1050*scale, y, scale)
    pipe5 = pipe_init(x + 1400*scale, y - 225*scale, scale)
    pipe6 = pipe_init(x + 1750*scale, y - 170*scale, scale)
    shapes.append(pipe1)
    shapes.append(pipe2)
    shapes.append(pipe3)
    shapes.append(pipe4)
    shapes.append(pipe5)
    shapes.append(pipe6)
    return shapes


def pipes_animate(shapes, frame, screen):
    """Animates the pipes, controls how the pipes move in each frame
    """
    for shape in shapes:
        for i in shape:
            i.move(-6, 0)


def pipes_test():
    """Tests the pipes animation
    """
    screen = gr.GraphWin('Flappy Bird', width=1100, height=800)
    screen.setBackground(gr.color_rgb(135, 206, 250))
    pipes1 = pipes_init(290, -10, 1)
    pipes2 = pipes_init(100, 20, 0.4)
    pipes3 = pipes_init(20, 500, 0.2)
    shapes = []
    for pipe1 in pipes1:
        shapes.append(pipe1)
    for pipe2 in pipes2:
        shapes.append(pipe2)
    for pipe3 in pipes3:
        shapes.append(pipe3)
    for shape in shapes:
        for i in shape:
            i.draw(screen)
    for i in range(1000):
        pipes_animate(pipes1, i, screen)
        pipes_animate(pipes2, i, screen)
        pipes_animate(pipes3, i, screen)
        time.sleep(0.1)
        if screen.checkMouse() is not None:
            break
    screen.update()
    screen.getMouse()
    screen.close()


def bush_init(x, y, scale):
    """Draws a bush at desired location and scale
    """
    shapes = []
    bush = gr.Oval(gr.Point(x, y), gr.Point(x + 70*scale, y + 55*scale))
    bush.setWidth(2*scale)
    bush.setFill(gr.color_rgb(150, 225, 150))
    bush.setOutline(gr.color_rgb(130, 225, 150))
    bush.setOutline(gr.color_rgb(90, 139, 100))
    shapes.append(bush)
    return shapes


def bushes_init(x, y, scale):
    """Draws some bushes at desired locations and scales
    """
    shapes = []
    bush1 = gr.Oval(gr.Point(x, y), gr.Point(x + 70*scale, y + 55*scale))
    bush1.setWidth(2*scale)
    bush1.setFill(gr.color_rgb(150, 225, 150))
    bush1.setOutline(gr.color_rgb(130, 225, 150))
    bush1.setOutline(gr.color_rgb(90, 139, 100))
    bush2 = bush1.clone()
    bush2.move(50*scale, -30*scale)
    bush3 = bush1.clone()
    bush3.move(100*scale, -20*scale)
    bush4 = bush1.clone()
    bush4.move(60*scale, 0)
    bush5 = bush3.clone()
    bush5.move(20*scale, 30*scale)
    shapes.append(bush5)
    shapes.append(bush1)
    shapes.append(bush2)
    shapes.append(bush3)
    shapes.append(bush4)
    return shapes


def buildings_init(x, y, scale):
    """Draws some buildings at desired locations and scales
    """
    shapes = []
    building1 = gr.Polygon(gr.Point(x, y), gr.Point(x + 8*scale, y), gr.Point(x + 8*scale, y + 10*scale), gr.Point(x + 25*scale, y + 10*scale), gr.Point(x + 25*scale, y + 100*scale), gr.Point(x, y + 100*scale))
    building1.setFill(gr.color_rgb(211, 211, 211))
    building1.setOutline(gr.color_rgb(169, 169, 169))
    building1.setWidth(scale)
    building2 = gr.Rectangle(gr.Point(x - 20*scale, y + 20*scale), gr.Point(x - 5*scale, y + 100*scale))
    building2.setFill(gr.color_rgb(211, 211, 211))
    building2.setOutline(gr.color_rgb(169, 169, 169))
    building2.setWidth(scale)
    building3 = gr.Rectangle(gr.Point(x + 30*scale, y + 15*scale), gr.Point(x + 45*scale, y + 100*scale))
    building3.setFill(gr.color_rgb(211, 211, 211))
    building3.setOutline(gr.color_rgb(169, 169, 169))
    building3.setWidth(scale)
    shapes.append(building1)
    shapes.append(building2)
    shapes.append(building3)
    return shapes


def bb_init(x, y, scale):
    """Combines and bushes and buildings
    """
    shapes = []
    bush = bushes_init(x, y, scale)
    building = buildings_init(x + 60*scale, y - 100*scale, scale*2)
    shapes.append(building)
    shapes.append(bush)
    return shapes


def background_init(x, y, scale):
    """Draws the background with the combined bushes and buildings
    """
    shapes = []
    bg1 = bb_init(x, y, scale)
    bg2 = bb_init(x + 160*scale, y, scale)
    bg3 = bb_init(x + 320*scale, y, scale)
    bg4 = bb_init(x + 480*scale, y, scale)
    shapes.append(bg1)
    shapes.append(bg2)
    shapes.append(bg3)
    shapes.append(bg4)
    return shapes


def background_animate(shapes, frame, screen):
    """Animates the background, controls how it moves in each frame
    """
    for shape in shapes:
        for i in shape:
            for s in i:
                s.move(-0.5, 0)


def background_test():
    """Tests the background animation
    """
    screen = gr.GraphWin('Flappy Bird', width=1100, height=800)
    screen.setBackground(gr.color_rgb(135, 206, 250))
    background1 = background_init(-10, 700, 2.5)
    background2 = background_init(100, 200, 1)
    background3 = background_init(350, 400, 0.5)
    shapes = []
    for bg1 in background1:
        for b1 in bg1:
            shapes.append(b1)
    for bg2 in background2:
        for b2 in bg2:
            shapes.append(b2)
    for bg3 in background3:
        for b3 in bg3:
            shapes.append(b3)
    for shape in shapes:
        for i in shape:
            i.draw(screen)
    for i in range(1000):
        background_animate(background1, i, screen)
        background_animate(background2, i, screen)
        background_animate(background3, i, screen)
        time.sleep(0.1)
        if screen.checkMouse() is not None:
            break
    screen.update()
    screen.getMouse()
    screen.close()