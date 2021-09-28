#Linn Cao Nguyen Phuong_Sep 1_Section A_Project01: What is a shape_CS151
from turtle import *
def shapeA():
    #face
    penup()
    goto(-45,5)
    pendown()
    dot(20)
    penup()
    goto(-50,-20)
    pendown()
    circle(20)
    penup()
    goto(45,5)
    pendown()
    dot(20)
    penup()
    goto(50,-20)
    pendown()
    circle(20)
    penup()
    goto(-10,-20)
    pendown()
    goto(10,-20)
    goto(0,-30)
    goto(-10,-20)

    #body
    penup()
    goto(-45,70)
    pendown()
    goto(45,70)
    left(75)
    forward(60)
    for x in range(160):
        forward(0.2)
        right(1)
    forward(80)
    left(20)
    forward(100)
    for x in range(60):
        forward(2.7)
        right(1)
    right(15)
    for x in range(20):
        forward(3)
        right(1)
    right(10)
    forward(30)
    right(10)
    forward(80)
    penup()
    goto(-45,70)
    right(75)
    pendown()
    forward(60)
    for x in range(160):
        forward(0.2)
        left(1)
    forward(80)
    right(20)
    forward(100)
    for x in range(60):
        forward(2.7)
        left(1)
    left(15)
    for x in range(20):
        forward(3)
        left(1)
    left(10)
    forward(30)

    #tummy
    penup()
    goto(0,-60)
    pendown()
    left(190)
    for x in range(75):
        forward(2.5)
        left(1)
    penup()
    goto(0,-60)
    pendown()
    left(105)
    for x in range(75):
        forward(2.5)
        right(1)
    penup()
    goto(-29,-115)
    pendown()
    left(165)
    for x in range(180):
        forward(0.5)
        right(1)
    right(145)
    for x in range(115):
        forward(0.6)
        left(1)
    penup()
    goto(-95,-180)
    pendown()
    right(100)
    for x in range(180):
        forward(0.5)
        right(1)
    right(147)
    for x in range(115):
        forward(0.6)
        left(1)
    penup()
    goto(95,-180)
    pendown()
    left(115)
    for x in range(180):
        forward(0.5)
        left(1)
    left(147)
    for x in range(115):
        forward(0.6)
        right(1)
    penup()
    goto(47,-165)
    pendown()
    right(180)
    for x in range(180):
        forward(0.25)
        left(1)
    left(147)
    for x in range(115):
        forward(0.3)
        right(1)
    penup()
    goto(-47,-165)
    pendown()
    right(180)
    for x in range(180):
        forward(0.25)
        right(1)
    right(147)
    for x in range(115):
        forward(0.3)
        left(1)

    #whiskers
    penup()
    goto(85,-30)
    pendown()
    goto(150,-20)
    penup()
    goto(85,-45)
    pendown()
    goto(150,-55)
    penup()
    goto(-85,-30)
    pendown()
    goto(-150,-20)
    penup()
    goto(-85,-45)
    pendown()
    goto(-150,-55)

def shapeB():
    #umbrella
    penup()
    goto(200,-230)
    pendown()
    left(80)
    forward(200)
    for x in range(150):
        forward(4)
        left(1)
    right(180)
    for x in range(90):
        forward(2.2)
        right(1)
    for x in range(70):
        forward(1.5)
        left(1)
    for x in range(120):
        forward(0.5)
        left(1)
    right(150)
    for x in range(120):
        forward(0.5)
        left(1)
    left(10)
    for x in range(48):
        forward(1)
        left(1)
    right(10)
    for x in range(15):
        forward(3)
        left(1)
    for x in range(48):
        forward(4)
        left(1)
    penup()
    goto(220,-230)
    pendown()
    right(148)
    forward(200)
    for x in range(72):
        forward(4.15)
        left(1)

def shapeThree():
    shapeA()
    left(105)
    shapeB()

def nGon(distance,number):
    angle=(number-2)*180/number
    for i in range(number):
        forward(distance)
        left(180-angle)
        forward(distance)

def shapeC(distance):
    for i in range(3):
        nGon(distance,6)
        left(120)
    left(60)
    for i in range(3):
        nGon(distance,6)
        left(120)   
    dot(distance)

def shapeD():
    penup()
    left(130)
    forward(250)
    pendown()
    shapeC(5)
    penup()
    left(55)
    forward(240)
    pendown()
    shapeC(8)
    penup()
    left(50)
    forward(540)
    pendown()
    shapeC(20)

shapeD()
hideturtle()

exitonclick()