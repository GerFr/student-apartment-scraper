from fizz import rooms_available as fizz_available
from ilive import rooms_available as ilive_available

import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

URL_FIZZ  = "https://www.the-fizz.com/search/?searchcriteria=BUILDING:THE_FIZZ_HAMBURG_STUDENTS;AREA:HAMBURG" 
URL_ILIVE = "https://www.urban-living-hamburg.de/mieten"

fizz_data = fizz_available(URL_FIZZ)
ilive_data = ilive_available(URL_ILIVE)

load_dotenv()
sender_email = os.getenv("SENDER")
password = os.getenv("PASSWORD")
recipient_email = os.getenv("RECEIVER")

text = f"{fizz_data[1], ilive_data[1]}"

msg = MIMEMultipart('alternative')
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = "Data"
msg.attach(MIMEText(text, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()  
server.login(sender_email, password)
server.sendmail(sender_email, recipient_email, msg.as_string())
server.quit()