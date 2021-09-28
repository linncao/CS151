"""Linn Cao Nguyen Phuong
   Dec 1, 2020
   Section A
   Final Project
   CS151
"""

import graphics as gr
import compound_shapes as cs 
import time
import complex_shape as csh

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


def background_init(x, y, scale):
   """Draws the background
   """
   shapes = []
   ground = gr.Rectangle(gr.Point(x, y + 480*scale), gr.Point(x + 1000*scale, y + 700*scale))
   ground.setFill(gr.color_rgb(188, 143, 143))
   ground.setOutline(gr.color_rgb(188, 143, 143))
   wall3 = gr.Rectangle(gr.Point(x + 300*scale, y), gr.Point(x + 1000*scale, y + 480*scale))
   wall3.setFill(gr.color_rgb(255, 250, 250))
   wall3.setOutline(gr.color_rgb(255, 250, 250))
   wall4 = gr.Rectangle(gr.Point(x, y + 290*scale), gr.Point(x + 1000*scale, y + 480*scale))
   wall4.setFill(gr.color_rgb(255, 250, 250))
   wall4.setOutline(gr.color_rgb(255, 250, 250))
   shapes.append(ground)
   shapes.append(wall3)
   shapes.append(wall4)
   return shapes


def background_test(x, y, scale):
   """Tests the background
   """
   screen = gr.GraphWin('Painting Gallery', width=1000, height=700)
   screen.setBackground(gr.color_rgb(255, 250, 250))
   shapes = []
   background1 = background_init(0, 0, 1)
   background2 = background_init(100, 100, 2)
   background3 = background_init(600, 300, 1.5)
   shapes.append(background1)
   shapes.append(background2)
   shapes.append(background3)
   for shape in shapes:
      for i in shape:
         i.draw(screen)
   screen.update()
   screen.getMouse()
   screen.close()


def wall_init(x, y, scale):
   """Draws the walls
   """
   shapes = []
   wall1 = gr.Rectangle(gr.Point(x, y), gr.Point(x + 100*scale, y + 480*scale))
   wall1.setFill(gr.color_rgb(255, 250, 250))
   wall1.setOutline(gr.color_rgb(255, 250, 250))
   wall2 = gr.Rectangle(gr.Point(x, y), gr.Point(x + 300*scale, y + 150*scale))
   wall2.setFill(gr.color_rgb(255, 250, 250))
   wall2.setOutline(gr.color_rgb(255, 250, 250))
   wall3 = gr.Rectangle(gr.Point(x + 300*scale, y), gr.Point(x + 420*scale, y + 480*scale))
   wall3.setFill(gr.color_rgb(255, 250, 250))
   wall3.setOutline(gr.color_rgb(255, 250, 250))
   wall4 = gr.Rectangle(gr.Point(x, y + 290*scale), gr.Point(x + 420*scale, y + 480*scale))
   wall4.setFill(gr.color_rgb(255, 250, 250))
   wall4.setOutline(gr.color_rgb(255, 250, 250))
   wall5 = gr.Rectangle(gr.Point(x + 300*scale, y), gr.Point(x + 1000*scale, y + 110*scale))
   wall5.setFill(gr.color_rgb(255, 250, 250))
   wall5.setOutline(gr.color_rgb(255, 250, 250))
   wall6 = gr.Rectangle(gr.Point(x + 420*scale, y + 320*scale), gr.Point(x + 1000*scale, y + 480*scale))
   wall6.setFill(gr.color_rgb(255, 250, 250))
   wall6.setOutline(gr.color_rgb(255, 250, 250))
   wall7 = gr.Rectangle(gr.Point(x + 606*scale, y), gr.Point(x + 750*scale, y + 480*scale))
   wall7.setFill(gr.color_rgb(255, 250, 250))
   wall7.setOutline(gr.color_rgb(255, 250, 250))
   shapes.append(wall1)
   shapes.append(wall2)
   shapes.append(wall3)
   shapes.append(wall4)
   shapes.append(wall5)
   shapes.append(wall6)
   shapes.append(wall7)
   return shapes


def wall_test(x, y, scale):
   """Tests the walls
   """
   screen = gr.GraphWin('Painting Gallery', width=1000, height=700)
   screen.setBackground(gr.color_rgb(255, 250, 250))
   shapes = []
   wall1 = wall_init(0, 0, 1)
   wall2 = wall_init(100, 100, 2)
   wall3 = wall_init(600, 300, 1.5)
   shapes.append(wall1)
   shapes.append(wall2)
   shapes.append(wall3)
   for shape in shapes:
      for i in shape:
         i.draw(screen)
   screen.update()
   screen.getMouse()
   screen.close()


def frame_init(x, y, scale):
   """Draws the frames
   """
   shapes = []
   frame1 = gr.Rectangle(gr.Point(x, y), gr.Point(x + 200*scale, y + 140*scale))
   frame1.setOutline(gr.color_rgb(165, 42, 42))
   frame1.setWidth(scale*25)
   frame2 = gr.Rectangle(gr.Point(x + 320*scale, y - 40*scale), gr.Point(x + 506*scale, y + 170*scale))
   frame2.setOutline(gr.color_rgb(165, 42, 42))
   frame2.setWidth(scale*25)
   frame3 = gr.Rectangle(gr.Point(x + 626*scale, y), gr.Point(x + 826*scale, y + 140*scale))
   frame3.setOutline(gr.color_rgb(165, 42, 42))
   frame3.setFill(gr.color_rgb(176, 224, 230))
   frame3.setWidth(scale*25)
   shapes.append(frame1)
   shapes.append(frame2)
   shapes.append(frame3)
   return shapes


def frame_test(x, y, scale):
   """Tests the frame
   """
   screen = gr.GraphWin('Painting Gallery', width=1000, height=700)
   screen.setBackground(gr.color_rgb(255, 250, 250))
   shapes = []
   frame1 = frame_init(0, 0, 1)
   frame2 = frame_init(100, 100, 2)
   frame3 = frame_init(600, 300, 1.5)
   shapes.append(frame1)
   shapes.append(frame2)
   shapes.append(frame3)
   for shape in shapes:
      for i in shape:
         i.draw(screen)
   screen.update()
   screen.getMouse()
   screen.close()


def snowman_init(x, y, scale, radius, eyeRadius, pen):
   """Draws a snowman at desired location and scale
   """
   shapes = []
   head = gr.Circle(gr.Point(x, y), radius)
   head.setFill(gr.color_rgb(255, 255, 255))
   head.setOutline(gr.color_rgb(70, 130, 180))
   head.setWidth(pen)
   bottom = gr.Circle(gr.Point(x, y + 4.8*radius*scale), radius*1.4)
   bottom.setFill(gr.color_rgb(255, 255, 255))
   bottom.setOutline(gr.color_rgb(70, 130, 180))
   bottom.setWidth(pen)
   eye1 = gr.Circle(gr.Point(x - scale*radius/1.2, y), eyeRadius)
   eye1.setFill(gr.color_rgb(0, 0, 0))
   eye2 = gr.Circle(gr.Point(x + scale*radius/1.2, y), eyeRadius)
   eye2.setFill(gr.color_rgb(0, 0, 0))
   shapes.append(head)
   shapes.append(bottom)
   shapes.append(eye1)
   shapes.append(eye2)
   return shapes


def snowman_test(x, y, scale, radius, eyeRadius, pen):
   """Tests the snowman
   """
   screen = gr.GraphWin('Painting Gallery', width=1000, height=700)
   screen.setBackground(gr.color_rgb(255, 250, 250))
   shapes = []
   snowman1 = snowman_init(0, 0, 1, 18, 2, 2.5)
   snowman2 = snowman_init(100, 100, 2, 18, 2, 2.5)
   snowman3 = snowman_init(600, 300, 1.5, 18, 2, 2.5)
   shapes.append(snowman1)
   shapes.append(snowman2)
   shapes.append(snowman3)
   for shape in shapes:
      for i in shape:
         i.draw(screen)
   screen.update()
   screen.getMouse()
   screen.close()


def board_init(x, y, scale):
   """Draws the board
   """
   shapes = []
   board = gr.Rectangle(gr.Point(x, y), gr.Point(x + 300*scale, y + 150*scale))
   board.setWidth(15*scale)
   board.setOutline(gr.color_rgb(105, 105, 105))
   board.setFill(gr.color_rgb(245, 245, 245))
   leg1 = gr.Rectangle(gr.Point(x + 20*scale, y + 150*scale), gr.Point(x + 40*scale, y + 180*scale))
   leg1.setOutline(gr.color_rgb(105, 105, 105))
   leg1.setFill(gr.color_rgb(105, 105, 105))
   leg2 = gr.Rectangle(gr.Point(x + 260*scale, y + 150*scale), gr.Point(x + 280*scale, y + 180*scale))
   leg2.setOutline(gr.color_rgb(105, 105, 105))
   leg2.setFill(gr.color_rgb(105, 105, 105))
   message = gr.Text(gr.Point(x + 150*scale, y + 70*scale), 'Double click onto the screen\nfor more direction')
   message.setFace('arial')
   message.setSize(15)
   message.setStyle('bold')
   message.setTextColor(gr.color_rgb(128, 0, 0))
   shapes.append(board)
   shapes.append(leg1)
   shapes.append(leg2)
   shapes.append(message)
   return shapes


def board_test(x, y, scale):
   """Tests the board
   """
   screen = gr.GraphWin('Painting Gallery', width=1000, height=700)
   screen.setBackground(gr.color_rgb(255, 250, 250))
   shapes = []
   board1 = board_init(0, 0, 1)
   board2 = board_init(100, 100, 2)
   board3 = board_init(600, 300, 1.5)
   shapes.append(board1)
   shapes.append(board2)
   shapes.append(board3)
   for shape in shapes:
      for i in shape:
         i.draw(screen)
   screen.update()
   screen.getMouse()
   screen.close()


def main():
   """Draws the Painting Gallery
   """
   screen = gr.GraphWin('Painting Gallery', width=1000, height=700)
   screen.setBackground(gr.color_rgb(255, 250, 250))
   background = background_init(0, 0, 1)
   wall = wall_init(0, 0, 1)
   frame = frame_init(100, 150, 1)
   bird = cs.bird_init(120, 230, 0.9)
   pipes = cs.pipes_init(158, 148, 0.2)
   backgroundbird = cs.background_init(98, 270, 0.5)
   human1 = csh.human1_init(442.5, 127.5, 0.25)
   human2 = csh.human2_init(410, 97.5, 0.25)
   human3 = csh.human3_init(442.5, 72.5, 0.25)
   human4 = csh.human4_init(410, 47.5, 0.25)
   sun = csh.sun_init(435, 122.5, 0.25)
   haystack1 = csh.haystack_init(447.5, 150, 0.175)
   haystack2 = csh.haystack_init(287.5, 152.5, 0.2)
   snowman = snowman_init(825, 200, 0.5, 18, 2, 2.5)
   board = board_init(360, 450, 1)
   shapes = []
   for bg in backgroundbird:
      for b in bg:
         shapes.append(b)
   shapes.append(bird)
   for pipe in pipes:
      shapes.append(pipe)
   shapes.append(background)
   for s in sun:
      shapes.append(s)
   for h4 in human4:
      shapes.append(h4)
   for h3 in human3:
      shapes.append(h3)
   for h2 in human2:
      shapes.append(h2)
   for hs1 in haystack1:
      shapes.append(hs1)
   for hs2 in haystack2:
      shapes.append(hs2)
   for h1 in human1:
      shapes.append(h1)
   shapes.append(wall)
   shapes.append(frame)
   shapes.append(snowman)
   shapes.append(board)
   for shape in shapes:
      for i in shape:
         i.draw(screen)
   for i in range(36):
      cs.background_animate(backgroundbird, i, screen)
      cs.pipes_animate(pipes, i, screen)
      cs.bird_animate(bird, i, screen, 0.2)
      time.sleep(0.5)
      if screen.checkMouse() is not None:
         break
   screen.update()
   screen.getMouse()
   screen.close()


if __name__ == '__main__':
   main()