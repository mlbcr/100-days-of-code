from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]
        self.add_parts()

    def create_snake(self):
        for i in range(3):
            new_part = Turtle("square")
            new_part.penup()
            new_part.color("green")
            new_part.goto(-20 * i, 0)
            self.parts.append(new_part)

    def add_parts(self):
        new_part = Turtle("square")
        new_part.penup()
        new_part.color("green")
        new_part.goto(self.parts[-1].xcor(), self.parts[-1].ycor())
        self.parts.append(new_part)

    def move(self):
        for i in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[i - 1].xcor()
            new_y = self.parts[i - 1].ycor()
            self.parts[i].goto(new_x, new_y)
        self.head.forward(20)

    def reset(self):
        for p in self.parts:
            p.goto(1000, 1000)
        self.parts.clear()
        self.create_snake()
        self.head = self.parts[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)