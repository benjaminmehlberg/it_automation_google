#!/usr/bin/env python3
"""
A script to send e-mails
"""
import os
import mimetypes
import smtplib
import getpass
from email.message import EmailMessage

"""
smtpserver="smtp.gmail.com:587" # TLS port
"""
smtpserver="smtp.gmail.com:465" # SSL port

sender = "sender@example.com"
recipient = "recipient@example.com"
body = "Dear all,\nthis is an email.\nThank you for your attention.\n\nBest regards"

msg = EmailMessage()
msg["From"] = sender
msg["To"] = recipient
msg["Subject"] = f"Email from {sender} to {recipient}"

msg.set_content(body)

print(msg)

mail_server = smtplib.SMTP_SSL(smtpserver)

mail_pass = getpass.getpass('Password? ')

mail_server.login(sender, mail_pass)
mail_server.send_message(msg)
mail_server.quit()
