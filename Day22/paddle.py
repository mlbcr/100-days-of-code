from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddle()
        self.pontuacao = 0

    def create_paddle(self):
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.setheading(90)

    def up(self):
        if self.ycor() <= 290:
            self.forward(40)

    def down(self):
        if self.ycor() >= -290:
            self.backward(40)
