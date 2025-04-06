from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer = None
number_work = 0
time_remaining = 0
is_running = False


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global number_work, time_remaining, is_running
    window.after_cancel(timer)
    number_work = 0
    time_remaining = 0
    is_running = False
    label_timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    btn_start.config(text="Start", fg="white", command=start_time)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global number_work, is_running, time_remaining
    is_running = True
    btn_start.config(bg="#d0b12b", text="Stop", command=stop_time)

    if time_remaining == 0:
        number_work += 1
        if number_work % 8 == 0:
            label_timer.config(text="Break", fg=RED, font=(FONT_NAME, 40, "bold"))
            count_down(LONG_BREAK_MIN * 60)
        elif number_work % 2 == 0:
            label_timer.config(text="Break", fg=PINK, font=(FONT_NAME, 40, "bold"))
            count_down(SHORT_BREAK_MIN * 60)
        else:
            label_timer.config(text="Working", fg=GREEN, font=(FONT_NAME, 40, "bold"))
            count_down(WORK_MIN * 60)
    else:
        count_down(time_remaining)

    check_marks.config(text="")


def stop_time():
    global is_running, time_remaining
    if is_running:
        window.after_cancel(timer)
        is_running = False
        btn_start.config(text="Resume", bg="#ffd700", fg="white", command=start_time)
    else:
        start_time()
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer, time_remaining
    time_remaining = count

    count_min = count // 60
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_time()
        if number_work % 2 == 0:
            check_marks["text"] = "🗸"
    # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_timer = Label(
    text="Timer",
    font=(FONT_NAME, 40),
    fg=GREEN,
    bg=YELLOW
)
label_timer.pack()

canvas = Canvas(width=220, height=250, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(115, 112, image=tomato_img)
timer_text = canvas.create_text(
    113,
    130,
    text="00:00", fill="white",
    font=(FONT_NAME, 35, "bold"),
)
canvas.pack()

btn_start = Button(
    text="Start",
    highlightthickness=0,
    bg="#ffd700",
    fg="white",
    relief=RAISED,
    font=(FONT_NAME, 12, "bold"),
    activebackground="#fde910",
    activeforeground="white",
    borderwidth=0,
    padx=10,
    pady=5,
    command=start_time
)
btn_start.pack(side=LEFT)

btn_reset = Button(
    text="Reset",
    highlightthickness=0,
    bg="#ffd700",
    fg="white",
    font=(FONT_NAME, 12, "bold"),
    relief=RAISED,
    activebackground="#fde910",
    activeforeground="white",
    borderwidth=0,
    padx=10,
    pady=5,
    command=reset_timer
)
btn_reset.pack(side=RIGHT)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
check_marks.pack()

window.mainloop()
