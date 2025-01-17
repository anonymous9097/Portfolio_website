import os
import smtplib
import ssl
from dotenv import load_dotenv

load_dotenv()


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("USER_EMAIL")
    password = os.getenv("PASSWORD")

    receiver = os.getenv("USER_EMAIL")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

