import time
from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(key="Up", fun=player.up)

cars = []

scoreboard = Scoreboard()

game_is_on = True
level = 1

while game_is_on:
    screen.update()

    if random.randint(1, max(8 - level, 2)) == 1:
        cars.append(Car())

    for car in cars:
        car.move(level)
        if 20 > car.xcor() > -20 and abs(player.ycor() - car.ycor()) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 290:
        player.reset()
        scoreboard.increase_level()
        level += 1

    time.sleep(0.1)
screen.exitonclick()