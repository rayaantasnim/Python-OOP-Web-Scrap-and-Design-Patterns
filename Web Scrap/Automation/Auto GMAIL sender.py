import smtplib
from email.message import EmailMessage

sender = "instructor076@gmail.com"
app_password = "mkql fzpp wauk gxph"
receiver = "rayaantasnim@gmail.com"

msg = EmailMessage()
msg['Subject'] = "This is a test email"
msg['From'] = sender
msg['To'] = receiver
msg.set_content("This is the body of the email, This email is sent using Python's smtplib library")

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender, app_password)
server.send_message(msg)
server.quit()
print("Email sent successfully")