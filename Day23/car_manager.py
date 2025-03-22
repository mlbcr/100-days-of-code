from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(random.randint(300, 400), random.randint(-250, 250))

    def move(self, level):
        self.bk(STARTING_MOVE_DISTANCE + 10 * level)



