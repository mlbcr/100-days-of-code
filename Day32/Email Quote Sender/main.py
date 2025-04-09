import smtplib
import datetime as dt
from random import choice

my_email = 'mlbcr123@gmail.com'
password = 'zuanlxmnthawfztd'

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 2:
    with open('quotes.txt', 'r') as file:
        lines = file.readlines()
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs='azulnebulosa15@gmail.com',
                msg=f"Subject:Phrase Of The Day\n\n{choice(lines)}"
            )