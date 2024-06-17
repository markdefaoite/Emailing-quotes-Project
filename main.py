import random
import smtplib
import datetime as dt

MY_EMAIL = "someone@gmail.com"
MY_PASSWORD = "################"
TO_ADDRESS = "somebody@somewhere.com"

now = dt.datetime.now()
weekday = now.weekday()

# check if it's Monday; 0 => Monday, 1=> Tuesday, 3 => Wednesday, etc.
if weekday == 0:
    with open("quotes.txt", "r") as file:
        quotes_list = file.readlines()
        quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_ADDRESS,
                            msg=f"Subject: Monday Motivation\n\nA little Monday Motivation for you:\n\n{quote}")
