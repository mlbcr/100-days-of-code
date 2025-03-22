import turtle
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen_width = screen.window_width()
screen_height = screen.window_height()
screen.bgcolor("black")
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
winner = None

colors = ["red", "yellow", "blue", "green", "orange", "purple"]
turtles = []
x = (screen_width/2 - 100)*-1
y = (screen_height/2 - 300)*-1

is_race_on = False

for i in range(0, 6):
    turtle_i = Turtle(shape="turtle")
    turtle_i.color(colors[i])
    turtle_i.penup()
    turtles.append(turtle_i)
    turtle_i.goto(x, y + i * 50)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtle.speed(randint(1, 10))
        turtle.fd(randint(10, 20))
        if turtle.xcor() > screen_width - 30:
            winner = turtle.color()[0]
            is_race_on = False

if winner != bet:
    print(f"You lost! Winner: {winner}")
else:
    print(f"You won! Winner: {winner}")
screen.exitonclick()
