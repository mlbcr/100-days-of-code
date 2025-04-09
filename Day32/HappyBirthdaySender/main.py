import smtplib
import datetime as dt
from random import choice
import pandas as pd

letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

my_email = 'mlbcr123@gmail.com'
password = 'zuanlxmnthawfztd'

now = dt.datetime.now()
date = (now.month, now.day)

birthdays_csv = pd.read_csv('birthdays.csv')
birthdays = {
    (row['month'], row['day']): (row['name'], row['email'])
    for _, row in birthdays_csv.iterrows()
}

if date in birthdays:
    random_letter = choice(letters)
    name = birthdays[date][0]
    email = birthdays[date][1]

    with open(f"letter_templates/{random_letter}", "r") as letter_file:
        letter_template = letter_file.read()
        final_letter = letter_template.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f'{email}',
            msg=f"Subject:Happy Birthday!!\n\n{final_letter}"
        )
