import smtplib
import datetime as dt
import random

my_gmail = "johanneskarl50@gmail.com"
password = "ampl nlkf oygp fbgf"

now = dt.datetime.now()
dayweek = now.weekday()
if dayweek == 0:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls() # ini supaya pesan kita terenkripsi dan aman
        connection.login(user=my_gmail, password=password)
        with open("./18. Birthday Wisher (SMTP+DT)/quotes.txt") as quotes:
            listquotes = quotes.readlines()
            connection.sendmail(
                from_addr=my_gmail,
                to_addrs="johanneskarl50@gmail.com", 
                msg=f"Subject:Hey it's Monday here is your quotes \n\n{random.choice(listquotes)}"
        )
    
