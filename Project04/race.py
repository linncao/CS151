"""Linn Cao Nguyen Phuong
   Sep 17, 2020
   Section A
   Lab 4: Unique turtles
   CS151
"""

import random
import turtle
import object_shapelib as os

s = turtle.Screen()

def make_turtle(shape = 'turtle', penColor = 'white', fillColor = 'black'):
    """Makes a 'Turtle' object
    """
    d1 = turtle.Turtle()
    d1.shape(shape)
    d1.color(penColor, fillColor)
    d1.penup()
    return d1


def writeNumRounds(turt, text, numRounds):
    """Replaces the turtle with a desired text
       in Times New Roman, size 20, style bold
    """
    turt.clear()
    turt.write(text + str(numRounds), font = ('Times New Roman', 20, 'bold'))
    turt.hideturtle()


def champion(turt, text):
    """Replaces the turtle with a desired text
       in Times New Roman, size 40, style bold
    """
    turt.clear()
    turt.write(text, font = ('Times New Roman', 40, 'bold'))
    turt.hideturtle()


def move_turtle(turt, radius, speed, turtDegreePassed):
    """Moves the 'Turtle' object 'turt' 'speed' units
    """
    if turtDegreePassed <= 90:
        if turtDegreePassed + speed <= 90:
            turt.circle(radius, speed)
        else:
            turt.circle(radius, 90 - turtDegreePassed)
            turt.circle(radius/2, speed - (90 - turtDegreePassed))
    elif turtDegreePassed > 90 and turtDegreePassed <= 180:
        if turtDegreePassed + speed <= 180:
            turt.circle(radius/2, speed)
        else:
            turt.circle(radius/2, 180 - turtDegreePassed)
            turt.circle(radius, speed - (180 - turtDegreePassed))
    elif turtDegreePassed > 180 and turtDegreePassed <= 270:
        if turtDegreePassed + speed <= 270:
            turt.circle(radius, speed)
        else:
            turt.circle(radius, 270 - turtDegreePassed)
            turt.circle(radius/2, speed - (270 - turtDegreePassed))
    elif turtDegreePassed > 270 and turtDegreePassed <= 360:
        if turtDegreePassed + speed <= 360:
            turt.circle(radius/2, speed)
        else:
            turt.circle(radius/2, 360 - turtDegreePassed)
            turt.circle(radius, speed - (360 - turtDegreePassed))


def main():
    """Puts several calls to functions from object_shapelib.py and above,
       creates 5 turtles, in which 2 race, 2 keep scores, 
       and 1 reports on the winner
    """
    os.make_screen(1000, 700, 'linnxinhhihi', 'salmon')
    os.draw_race_scene()
    turt1 = make_turtle('turtle', 'snow', 'dark slate blue')
    turt1.speed(0)
    turt1.goto(-125, -65)
    turt1.right(44)
    turt2 = make_turtle('square', 'indian red', 'misty rose')
    turt2.speed(0)
    turt2.goto(-170, -90)
    turt2.right(44)
    turt3 = make_turtle('circle', 'dark slate blue', 'dark slate blue')
    turt3.speed(0)
    turt3.goto(-470, 280)
    turt4 = make_turtle('circle', 'indian red', 'indian red')
    turt4.speed(0)
    turt4.goto(-470, 240)
    turt5 = make_turtle('arrow', 'black', 'light blue')
    turt5.speed(0)
    turt5.goto(-210, -20)
    round1 = 0
    writeNumRounds(turt3, 'Turtle 1: ', round1)
    round2 = 0
    writeNumRounds(turt4, 'Turtle 2: ', round2)
    turtDegreePassed1 = 0
    turtDegreePassed2 = 0
    while round1 <= 1000 and round2 <= 1000:
        x1 = turt1.xcor()
        speed = random.randint(3, 5)
        move_turtle(turt1, 180, speed, turtDegreePassed1)
        turtDegreePassed1 += speed
        y1 = turt1.ycor()
        if turtDegreePassed1 >= 360:
            round1 += 1
            turtDegreePassed1 %= 360
            print('turt1 completes', round1, 'rounds.')
            writeNumRounds(turt3, 'Turtle 1: ', round1)
        x2 = turt2.xcor()
        speed = random.randint(2, 6)
        move_turtle(turt2, 250, speed, turtDegreePassed2)
        turtDegreePassed2 += speed
        y2 = turt2.ycor()
        if turtDegreePassed2 >= 360:
            round2 += 1
            turtDegreePassed2 %= 360
            print('turt2 completes', round2, 'rounds.')
            writeNumRounds(turt4, 'Turtle 2: ', round2)
        if round1 == 5:
            champion(turt5, 'TURTLE 1 WINS.')
            break
        if round2 == 5:
            champion(turt5, 'TURTLE 2 WINS.')
            break


if __name__ == '__main__':
    main()


s.exitonclick()