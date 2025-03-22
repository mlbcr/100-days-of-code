from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 40
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.reset()
        self.setheading(90)

    def up(self):
        if self.ycor() <= 290:
            self.forward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)