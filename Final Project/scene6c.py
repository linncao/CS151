"""Linn Cao Nguyen Phuong
   Dec 1, 2020
   Section A
   Final Project
   CS151
"""

import graphics as gr
import scene6 as s6

def frame_init(x, y, scale):
    """Draws the frame
    """
    shapes = []
    frame = gr.Rectangle(gr.Point(x, y), gr.Point(x + 400*scale, y + 280*scale))
    frame.setOutline(gr.color_rgb(165, 42, 42))
    frame.setFill(gr.color_rgb(176, 224, 230))
    frame.setWidth(scale*50)
    shapes.append(frame)
    return shapes


def frame_test(x, y, scale):
    """Tests the frame
    """
    screen = gr.GraphWin('Painting Gallery, Artwork 3', width=1000, height=700)
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
    message1 = gr.Text(gr.Point(x, y), 'Artwork: Snowman\nArtist: Linn Cao\nCreated on Nov 22, 2020')
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
    screen = gr.GraphWin('Painting Gallery, Artwork 3', width=1000, height=700)
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


def main():
    """Draws painting and info
    """
    screen = gr.GraphWin('Painting Gallery, Artwork 3', width=1000, height=700)
    screen.setBackground(gr.color_rgb(255, 250, 250))
    shapes = []
    frame = frame_init(100, 220, 1)
    text = text_init(780, 350, 1)
    snowman = s6.snowman_init(300, 310, 0.5, 40, 3, 5)
    shapes.append(frame)
    shapes.append(snowman)
    shapes.append(text)
    for shape in shapes:
        for i in shape:
            i.draw(screen)
    screen.update()
    screen.getMouse()
    screen.close()


if __name__ == '__main__':
    main()