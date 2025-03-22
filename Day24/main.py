from turtle import Screen
from snake import Snake
from food import Food
from time import sleep
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.screensize(400, 500)

snake = Snake()
food = Food()
board = ScoreBoard()
board.update_score()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Down", fun=snake.down)

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        board.increase_score()
        snake.add_parts()
    # Detect collision with food
    if snake.head.xcor() > 450 or snake.head.xcor() < -450 or snake.head.ycor() < -450 or snake.head.ycor() > 450:
        board.reset()
        snake.reset()
    # Detect collision with tail
    for part in snake.parts[1:]:
        if snake.head.distance(part) < 10:
            board.reset()
            snake.reset()
screen.exitonclick()
