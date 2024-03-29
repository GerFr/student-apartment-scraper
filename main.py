from fizz import rooms_available as fizz_available
from ilive import rooms_available as ilive_available

import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import markdown2
from datetime import datetime

URL_FIZZ  = "https://www.the-fizz.com/search/?searchcriteria=BUILDING:THE_FIZZ_HAMBURG_STUDENTS;AREA:HAMBURG" 
URL_ILIVE = "https://www.urban-living-hamburg.de/mieten"

fizz_data = fizz_available(URL_FIZZ)
ilive_data = ilive_available(URL_ILIVE)

load_dotenv()
sender_email = os.getenv("SENDER")
password = os.getenv("APP_PASSWORD")
recipient_email = os.getenv("RECEIVER")

text = f"""
## FIZZ Apartment

[website]({URL_FIZZ}), room {"" if fizz_data[0] else "not "}available

### data

`{fizz_data[1]}`


## Urban-Living Apartment

[website]({URL_ILIVE}), room {"" if ilive_data[0] else "not "} available

### data

`{ilive_data[1]}`
"""

html_text = markdown2.markdown(text)

msg = MIMEMultipart('alternative')
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = f"Wohnheimsinformationen {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html_text, 'html')
msg.attach(part1)
msg.attach(part2)

with smtplib.SMTP('smtp.gmail.com', 587) as server:
  server.starttls()  
  server.login(sender_email, password)
  server.sendmail(sender_email, recipient_email, msg.as_string())
