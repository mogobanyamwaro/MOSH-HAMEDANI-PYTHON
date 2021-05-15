from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from pathlib import Path
from string import Template


template = Template(Path("templates.html").read_text())



message =MIMEMultipart()
message['from'] = 'douglas mogoba'
message['to'] = 'douglasnyamwaro289@gmail.com'
message['subject'] = 'this is a test'

body = template.substitute({"name":"John"})


message.attach(MIMEText(body,'html'))
message.attach(MIMEImage(Path('hello.jpg').read_bytes()))

with smtplib.SMTP(host='smtp.gmail.com',port =587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("mogobanyamwaro@gmail.com","0790542041")
    smtp.send_message(message)
    print('sent....')