# Improving Password Manager
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from pyperclip import copy
import json

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


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
        return
    except json.JSONDecodeError:
        messagebox.showinfo(title="Error", message="Data file is empty or corrupted.")
        return

    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
    else:
        messagebox.showinfo(title="Not Found", message=f"No details for the website exists")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        empty_field = messagebox.showinfo(title="Oops! Missing information", message="At least one of the fields "
                                                                                     "in blank.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        data.update(new_data)

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# UI Setup
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
locker_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=locker_img)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
website_label = Label(text="Website:", font=("Arial", 14))
website_label.grid(row=1, column=0, sticky='E', pady=5)

email_user_label = Label(text="Email/Username:", font=("Arial", 14))
email_user_label.grid(row=2, column=0, sticky='E', pady=5)

password_label = Label(text="Password:", font=("Arial", 14))
password_label.grid(row=3, column=0, sticky='E', pady=5)

# Entries
website_entry = Entry(width=32, font=("Arial", 12))
website_entry.grid(row=1, column=1, sticky='W')
website_entry.focus()

btn_search = Button(
    text="Search",
    width=14,
    bg="#A52A2A",
    fg="white",
    relief=RAISED,
    activebackground="#800020",
    activeforeground="white",
    borderwidth=0,
    pady=5,
    command=find_password
)
btn_search.grid(row=1, column=2, padx=5)

email_user_entry = Entry(width=52, font=("Arial", 12))
email_user_entry.grid(row=2, column=1, columnspan=2, sticky='W')
email_user_entry.insert(0, "email@gmail.com")

password_entry = Entry(width=32, font=("Arial", 12))
password_entry.grid(row=3, column=1, sticky='W')

btn_generate_pass = Button(
    text="Generate Password",
    width=14,
    bg="#A52A2A",
    fg="white",
    relief=RAISED,
    activebackground="#800020",
    activeforeground="white",
    borderwidth=0,
    pady=5,
    command=generate_password
)
btn_generate_pass.grid(row=3, column=2, padx=5)

# Add Button
btn_add = Button(
    text="Add",
    width=44,
    bg="#191919",
    fg="white",
    font=("Courier", 12),
    relief=RAISED,
    command=add
)
btn_add.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()