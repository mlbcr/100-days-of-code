from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscores.txt", "r") as high_score:
            self.high_score = int(high_score.read().strip())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscores.txt", "w") as high_score:
                high_score.write(f"{self.score}")

        self.score = 0
        self.update_score()
