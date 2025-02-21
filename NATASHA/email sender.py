import smtplib

print("Hi, my name is NATASHA, also known as No Awesome Time Actually Studying (to) Harvest A*s")
email = "natashaai2025@gmail.com"
receiver_email = input("RECEIVER EMAIL: ")
subject = input("SUBJECT:")
message = input("MESSAGE: ")


text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(email, "zcio itce byrb wsnj")

server.sendmail(email, receiver_email, text)

print("Email has been sent.")
