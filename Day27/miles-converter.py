from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(bg="#3C0061", padx=50, pady=50)

# Labels
title = Label(
    text="Miles To Km",
    font=("Times New Roman", 22, "bold"),
    bg="#3C0061",
    fg="white"
)
title.grid(column=1, row=0, columnspan=3, pady=50)

label_miles = Label(
    text="miles",
    font=("Arial", 14),
    bg="#3C0061",
    fg="white"
)
label_miles.grid(column=2, row=1)

label_equal = Label(
    text="is equal to",
    font=("Arial", 14),
    bg="#3C0061",
    fg="white"
)
label_equal.grid(column=0, row=2)

label_km = Label(
    text="km",
    font=("Arial", 14),
    bg="#3C0061",
    fg="white"
)
label_km.grid(column=2, row=2)

# Values
miles_value = Entry(fg="white", bg="black", font=("Arial", 16), width=10)
miles_value.grid(column=1, row=1)
miles_value.config(relief="solid", borderwidth=2)

km_value = Label(
    text="0",
    font=("Arial", 16),
    fg="white",
    bg="#3C0061"
)
km_value.config(pady=10, padx=10, bg="#6E00B3", font=("Arial", 18, "bold"))
km_value.grid(column=1, row=2, pady=20)


def button_clicked():
    if miles_value.get() != "":
        km_value["text"] = float(miles_value.get()) * 1.609


button = Button(
    text="Convert",
    command=button_clicked,
    relief="raised",
    borderwidth=1,
    font=("Arial", 14, "bold"),
    bg="#9D00FF",
    fg="white"
)
button.grid(column=1, row=4, pady=20)
button.config(borderwidth=3, activebackground="#6E00B3")


window.mainloop()