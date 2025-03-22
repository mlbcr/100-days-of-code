from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

def draw_center_line():
    line = ScoreBoard()
    line.score = " "
    line.update_score()
    line.color("white")
    line.penup()
    line.goto(0, 300)
    line.setheading(270)
    line.pensize(3)
    while line.ycor() > -300:
        line.pendown()
        line.forward(15)
        line.penup()
        line.forward(10)

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("pong")
screen.tracer(0)

paddle1 = Paddle()
paddle1.goto(350, 0)
paddle1.color("blue")

screen.listen()
screen.onkey(key="Up", fun=paddle1.up)
screen.onkey(key="Down", fun=paddle1.down)

paddle2 = Paddle()
paddle2.goto(-350, 0)
paddle2.color("red")

screen.listen()
screen.onkey(key="w", fun=paddle2.up)
screen.onkey(key="s", fun=paddle2.down)

ball = Ball()

board_left = ScoreBoard()
board_left.goto(-50, 200)
board_left.name = 'RED'
board_left.update_score()

board_right = ScoreBoard()
board_right.goto(50, 200)
board_left.name = 'BLUE'
board_right.update_score()

draw_center_line()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.xcor() > 330 and ball.distance(paddle1) < 50:
        ball.hit()

    if ball.xcor() < -330 and ball.distance(paddle2) < 50:
        ball.hit()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        board_left.increase_score()

    if ball.xcor() < -380:
        ball.reset_position()
        board_right.increase_score()

    if board_left.score == 3:
        board_left.win()
        game_is_on = False

    if board_right.score == 3:
        board_right.win()
        game_is_on = False
screen.exitonclick()