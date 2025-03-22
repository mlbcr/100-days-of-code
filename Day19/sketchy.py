from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forwards():
    t.fd(10)


def move_backwards():
    t.bk(10)


def move_up():
    t.sety(t.ycor() + 10)


def move_down():
    t.sety(t.ycor() - 10)


def rotate():
    t.rt(10)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(key="d", fun=move_forwards)
screen.onkey(key="a", fun=move_backwards)
screen.onkey(key="w", fun=move_up)
screen.onkey(key="s", fun=move_down)
screen.onkey(key="e", fun=rotate)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
