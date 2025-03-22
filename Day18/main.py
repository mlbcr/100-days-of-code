from turtle import Turtle, Screen, colormode
from random import choice
t = Turtle()
screen = Screen()
screen.screensize(2000,1500)
screen.title("Hirst Painting Project")
colormode(255)

color_list = [(184, 165, 132), (229, 212, 90), (221, 78, 119), (94, 179, 214), (204, 222, 210), (153, 92, 49), (47, 86, 152), (234, 68, 43), (241, 212, 218), (201, 137, 172), (193, 210, 219), (173, 63, 116), (113, 188, 108), (41, 169, 83), (53, 30, 19), (201, 157, 44), (224, 176, 173), (44, 126, 75), (231, 169, 189), (94, 116, 183), (14, 87, 51), (238, 214, 13), (168, 202, 208), (172, 206, 181), (40, 24, 28), (70, 65, 52), (69, 52, 128), (172, 26, 63), (15, 76, 43), (172, 188, 217), (91, 54, 47), (29, 27, 32), (82, 145, 168), (19, 83, 108)]
t.hideturtle()
t.penup()
t.setpos(-200, -200)
t.speed(5)

def walk():
    t.dot(20, choice(color_list))
    t.fd(50)


def change_left():
    t.dot(20, choice(color_list))
    t.lt(90)
    t.fd(50)
    t.lt(90)


def change_right():
    t.dot(20, choice(color_list))
    t.rt(90)
    t.fd(50)
    t.rt(90)

for line in range(10):
    for _ in range(10):
        walk()
    if line % 2 == 0:
        change_left()
    else:
        change_right()


screen.exitonclick()
