import os
import smtplib

from langchain.tools import tool
from email.mime.text import MIMEText


@tool
def send_email(to: str, subject: str, message: str) -> str:
    """
    Send an email using Gmail SMTP.
    """

    email_user = os.getenv("EMAIL_USER")
    email_pass = os.getenv("EMAIL_PASS")

    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = email_user
        msg["To"] = to

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_user, email_pass)
        server.send_message(msg)
        server.quit()

        return "Email sent successfully."

    except Exception as e:
        return f"Error sending email: {str(e)}"
