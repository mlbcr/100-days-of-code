import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

game_is_on = True

states = pd.read_csv("50_states.csv")


def create_turtle(x_cor, y_cor, s_state):
    t = turtle.Turtle()
    t.shape("circle")
    t.shapesize(0.3)
    t.penup()
    t.goto(x_cor, y_cor)
    t.write(s_state)


answer_state = screen.textinput(title="Guess the state", prompt="What's the state?")
guessed_states = []

while len(guessed_states) < 50:
    if answer_state == "exit":
        missing_states = []
        for state in states["state"].to_list():
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        break
    for place in states["state"]:
        if answer_state.lower() == place.lower():
            guessed_states.append(place)
            specific_state = states[states["state"] == place]
            x = specific_state["x"].values[0]
            y = specific_state["y"].values[0]
            create_turtle(x, y, place)

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's the state?")


