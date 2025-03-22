from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.name = None
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=("Arial", 40, "normal"))

    def win(self):
        self.goto(0, 0)
        self.write(f"{self.name} WINS", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()