import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration

sender_email = 'jvekeren@gmail.com'
sender_password = 'geeyjwvhagkfrabr'  # Replace with your Gmail password
recipient_email = 'johan@jvekeren.nl'
subject = 'Test Email'
message_text = 'This is a test email sent from Python using Gmail.'

# Create a MIME object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(message_text, 'plain'))

# Connect to the Gmail SMTP server and send the email
smtp_server = 'smtp.gmail.com'
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, sender_password)
server.sendmail(sender_email, recipient_email, msg.as_string())

server.quit()

print("Email sent successfully.")
