#Linn Cao Nguyen Phuong_Sep 1_Section A_Project01: What is a shape_CS151
from turtle import *
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
hideturtle()
exitonclick()