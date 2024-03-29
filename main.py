from fizz import rooms_available as fizz_available
from ilive import rooms_available as ilive_available

import os
import time
import logging
import smtplib
import markdown2
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv


URL_FIZZ  = "https://www.the-fizz.com/search/?searchcriteria=BUILDING:THE_FIZZ_HAMBURG_STUDENTS;AREA:HAMBURG" 
URL_ILIVE = "https://www.urban-living-hamburg.de/mieten"
TIME = 600
LOG_PATH = "main.log"


def send_mail(text, sender_email, recipient_email):
    html_text = markdown2.markdown(text)

    msg = MIMEMultipart('alternative')
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = f"Wohnheimsinformationen {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    msg.attach(MIMEText(html_text, 'html'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, msg.as_string())



if __name__ == "__main__":
    logging.basicConfig(filename=LOG_PATH,
                        filemode="w",
                        format='%(asctime)s %(filename)s %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    load_dotenv()
    sender_email = os.getenv("SENDER")
    password = os.getenv("APP_PASSWORD")
    recipient_email = os.getenv("RECEIVER")


    while True: 
        logger.info("get fizz data")
        fizz_data = fizz_available(URL_FIZZ)
        logger.info(f"room {" " if fizz_data[0] else "not "}available")
        logger.info("get ilive data")
        ilive_data = ilive_available(URL_ILIVE)
        logger.info(f"room {" " if ilive_data[0] else "not "}available")


        text = f"""
## FIZZ Apartment

[website]({URL_FIZZ}), room {"" if fizz_data[0] else "not "}available

`{fizz_data[1]}`


## Urban-Living Apartment

[website]({URL_ILIVE}), room {"" if ilive_data[0] else "not "} available

`{ilive_data[1]}`
"""
        logger.info("sending message")
        send_mail(text, sender_email, recipient_email)
        logger.info(f"sent, waiting for {TIME} seconds")
        time.sleep(TIME)