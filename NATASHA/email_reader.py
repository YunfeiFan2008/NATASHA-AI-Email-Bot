import imaplib
import smtplib
import email
from email.message import EmailMessage

# Introduction
print("Hi, my name is NATASHA, also known as No Awesome Time Actually Studying (to) Harvest A*s")

# Email credentials
email_address = "natashaai2025@gmail.com"
password = "zcio itce byrb wsnj" # Securely input password

# Set up SMTP for sending emails
smtp_server = "smtp.gmail.com"
server = smtplib.SMTP(smtp_server, 587)
server.starttls()
server.login(email_address, password)

# Set up IMAP for reading emails
imap_server = "imap.gmail.com"
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)
imap.select("Inbox")

# Search for UNSEEN emails
_, msgnums = imap.search(None, 'UNSEEN')

keyword = "TEST"
response_subject = "Keyword Found"
response_body = "We found your keyword (TEST)."

for msgnum in msgnums[0].split():
    _, data = imap.fetch(msgnum, "(RFC822)")
    msg = email.message_from_bytes(data[0][1])  # Renamed `message` to `msg` to avoid conflicts

    sender_email = email.utils.parseaddr(msg.get("From"))[1]  # Extract sender's email
    subject = msg.get("Subject", "(No Subject)")
    
    print(f"From: {sender_email}")
    print(f"Subject: {subject}")

    # Extract email body
    body = ""
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True).decode(errors="ignore")
            print("Content:")
            print(body)

            # If keyword is found, send response
            if "-help" in body.lower():
                print("Help command detected. Sending Response...")

                reply = EmailMessage()
                reply["From"] = email_address
                reply["To"] = sender_email
                reply["Subject"] = "Re: " + subject
                response_body = "Hello! Nice to meet you. My name is NATASHA."
                reply.set_content(response_body)

                server.send_message(reply)
                print("Response sent!")

# Close connections
imap.close()
imap.logout()
server.quit()