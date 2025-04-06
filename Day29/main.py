from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from pyperclip import copy

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 18))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    copy(password)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        empty_field = messagebox.showinfo(title="Oops! Missing information", message="At least one of the fields "
                                                                                     "in blank.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            template = f"{website} | {email} | {password}\n"
            with open(f"data.txt", "a") as data_file:
                data_file.write(template)
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
locker_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=locker_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(
    text="Website",
    font=("Arial", 14),
    padx=10,
    pady=5,
)
website_label.grid(row=1, column=0)

email_user_label = Label(
    text="Email/Username",
    font=("Arial", 14),
    padx=10,
    pady=5,
)
email_user_label.grid(row=2, column=0)

password_label = Label(
    text="Password",
    font=("Arial", 14),
    padx=10,
    pady=5,
)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(
    font=("Arial", 14),
    width=35
)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
website_entry.config(relief="solid", borderwidth=1)

email_user_entry = Entry(
    font=("Arial", 14),
    width=35
)
email_user_entry.grid(row=2, column=1, columnspan=2)
email_user_entry.config(relief="solid", borderwidth=1)
email_user_entry.insert(0, "email@gmail.com")

password_entry = Entry(
    font=("Arial", 14),
    width=19,
)
password_entry.grid(row=3, column=1)
password_entry.config(relief="solid", borderwidth=1)

btn_generate_pass = Button(
    text="Generate Password",
    highlightthickness=0,
    bg="#A52A2A",
    fg="white",
    font=("Courier", 12, "bold"),
    relief=RAISED,
    activebackground="#800020",
    activeforeground="white",
    borderwidth=0,
    pady=5,
    command=generate_password
)
btn_generate_pass.grid(row=3, column=2)

btn_add = Button(
    text="Add",
    highlightthickness=0,
    bg="#191919",
    fg="white",
    font=("Courier", 12),
    relief=RAISED,
    activebackground="#000000",
    activeforeground="white",
    borderwidth=0,
    width=40,
    pady=5,
    command=add
)
btn_add.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()