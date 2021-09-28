"""Linn Cao Nguyen Phuong
   Dec 1, 2020
   Section A
   Final Project
   CS151
"""

import graphics as gr
import complex_shape as cs 
import time

def frame_init(x, y, scale):
    """Draws the frame
    """
    shapes = []
    frame = gr.Rectangle(gr.Point(x, y), gr.Point(x + 372*scale, y + 420*scale))
    frame.setOutline(gr.color_rgb(165, 42, 42))
    frame.setWidth(scale*50)
    shapes.append(frame)
    return shapes


def frame_test(x, y, scale):
    """Tests the frame
    """
    screen = gr.GraphWin('Painting Gallery, Artwork 2', width=1000, height=700)
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


def text_init(x, y, scale):
    """Writes info of painting
    """
    shapes = []
    message1 = gr.Text(gr.Point(x, y), 'Artwork: Vietnam Socialism\nArtist: Linn Cao\nCreated on Oct 6, 2020')
    message1.setFace('arial')
    message1.setSize(20)
    message1.setStyle('bold')
    message1.setTextColor(gr.color_rgb(128, 0, 0))
    message2 = gr.Text(gr.Point(x - 280*scale, y + 320*scale), 'Double click onto the screen to see the next direction')
    message2.setFace('arial')
    message2.setSize(12)
    message2.setStyle('bold')
    message2.setTextColor(gr.color_rgb(205, 92, 92))
    shapes.append(message1)
    shapes.append(message2)
    return shapes


def text_test(x, y, scale):
    """Tests the text
    """
    screen = gr.GraphWin('Painting Gallery, Artwork 2', width=1000, height=700)
    screen.setBackground(gr.color_rgb(255, 250, 250))
    shapes = []
    text1 = text_init(0, 0, 1)
    text2 = text_init(100, 100, 2)
    text3 = text_init(600, 300, 1.5)
    shapes.append(text1)
    shapes.append(text2)
    shapes.append(text3)
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
    wall1 = gr.Rectangle(gr.Point(x, y), gr.Point(x + 100*scale, y + 700*scale))
    wall1.setFill(gr.color_rgb(255, 250, 250))
    wall1.setOutline(gr.color_rgb(255, 250, 250))
    wall2 = gr.Rectangle(gr.Point(x + 100*scale, y + 570*scale), gr.Point(x + 1000*scale, y + 700*scale))
    wall2.setFill(gr.color_rgb(255, 250, 250))
    wall2.setOutline(gr.color_rgb(255, 250, 250))
    wall3 = gr.Rectangle(gr.Point(x, y), gr.Point(x + 1000*scale, y + 150*scale))
    wall3.setFill(gr.color_rgb(255, 250, 250))
    wall3.setOutline(gr.color_rgb(255, 250, 250))
    wall4 = gr.Rectangle(gr.Point(x + 480*scale, y), gr.Point(x + 1000*scale, y + 700*scale))
    wall4.setFill(gr.color_rgb(255, 250, 250))
    wall4.setOutline(gr.color_rgb(255, 250, 250))
    shapes.append(wall1)
    shapes.append(wall2)
    shapes.append(wall3)
    shapes.append(wall4)
    return shapes


def wall_test(x, y, scale):
    """Tests the walls
    """
    screen = gr.GraphWin('Painting Gallery, Artwork 2', width=1000, height=700)
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


def main():
    """Draws painting and info
    """
    screen = gr.GraphWin('Painting Gallery, Artwork 2', width=1000, height=700)
    screen.setBackground(gr.color_rgb(255, 250, 250))
    shapes = []
    frame = frame_init(100, 150, 1)
    text = text_init(750, 350, 1)
    human1 = cs.human1_init(184, 208, 0.48)
    human2 = cs.human2_init(80, 144, 0.48)
    human3 = cs.human3_init(184, 88, 0.48)
    human4 = cs.human4_init(80, 40, 0.48)
    sun = cs.sun_init(160, 160, 0.48)
    haystack1 = cs.haystack_init(80, 200, 0.48)
    haystack2 = cs.haystack_init(-328, 200, 0.512)
    wall = wall_init(0, 0, 1)
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
    shapes.append(text)
    for shape in shapes:
        for i in shape:
            i.draw(screen)
    screen.update()
    screen.getMouse()
    screen.close()


if __name__ == '__main__':
    main()