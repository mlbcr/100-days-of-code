from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

# ----------------------------- SETUP INICIAL --------------------------------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(800, 700)

language_var = StringVar(value="korean")

# Language selection
label_choose_language = Label(
    window,
    text="Choose language:",
    bg=BACKGROUND_COLOR,
    font=(FONT_NAME, 14)
)
label_choose_language.pack()

language_frame = Frame(window, bg=BACKGROUND_COLOR)
language_frame.pack()

radio_korean = Radiobutton(
    language_frame,
    text="Korean",
    variable=language_var,
    value="korean",
    bg=BACKGROUND_COLOR
)
radio_korean.pack(side=LEFT)

radio_french = Radiobutton(
    language_frame,
    text="French",
    variable=language_var,
    value="french",
    bg=BACKGROUND_COLOR
)
radio_french.pack(side=LEFT)

start_button = Button(
    text="Start",
    font=(FONT_NAME, 14),
    command=lambda: start_flashcards()
)
start_button.pack(pady=20)

# Placeholders
canvas = None
button_right = None
button_wrong = None
text_language = None
text_word = None

# Data
current_translation = ""
words_df = None

# ----------------------------- FLASHCARDS --------------------------------------------

def start_flashcards():
    global words_df, canvas, button_right, button_wrong, text_language, text_word

    label_choose_language.pack_forget()
    language_frame.pack_forget()
    start_button.pack_forget()

    selected_language = language_var.get()
    file_path = f"data/{selected_language}_words.csv"
    words_df = pd.read_csv(file_path)

    canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    card_image = PhotoImage(file="images/card_front.png")
    canvas.create_image(400, 263, image=card_image)
    canvas.image = card_image

    text_language = canvas.create_text(400, 163, text="", fill="black", font=(FONT_NAME, 40))
    text_word = canvas.create_text(400, 263, text="", fill="black", font=(FONT_NAME, 60, "bold"))
    canvas.pack()
    right_image = PhotoImage(file="images/right.png")
    button_right = Button(image=right_image, highlightthickness=0, borderwidth=0, command=hit)
    button_right.image = right_image
    button_right.pack(side=RIGHT, padx=120)

    wrong_image = PhotoImage(file="images/wrong.png")
    button_wrong = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=miss)
    button_wrong.image = wrong_image
    button_wrong.pack(side=LEFT, padx=120)

    create_flashcard()


def create_flashcard():
    global current_translation
    row = words_df.sample().iloc[0]
    foreign_word = row.iloc[0]
    english_word = row.iloc[1]
    current_translation = english_word
    canvas.itemconfig(text_word, text=foreign_word)
    canvas.itemconfig(text_language, text="Korean" if language_var.get() == "korean" else "French")


def show_translation():
    canvas.itemconfig(text_word, text=current_translation)
    canvas.itemconfig(text_language, text="English")


def hit():
    show_translation()
    window.after(3000, create_flashcard)

def miss():
    create_flashcard()

# ----------------------------- MAINLOOP --------------------------------------------
window.mainloop()
