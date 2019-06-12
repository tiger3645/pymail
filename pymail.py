from urllib.request import urlopen
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def mail():
    ADDRESS = ''
    PASSWORD = ''
    RECIPIENT = ''
    SUBJECT = ''
    MESSAGGE = ''
    HOST = ''
    PORT = 000

    messagge = MIMEMultipart('alternative')
    messagge.set_charset('utf8')
    messagge['FROM'] = ADDRESS
    messagge['To'] = RECIPIENT
    messagge['Subject'] = SUBJECT

    BODY = MIMEText(MESSAGGE.encode('utf-8'), 'html', 'UTF-8')

    messagge.attach(BODY)

    mail =smtplib.SMTP(HOST, PORT)
    mail.ehlo()
    mail.starttls()
    mail.login(ADDRESS, PASSWORD)
    
    mail.sendmail(ADDRESS, ADDRESS, messagge.as_string())
    mail.close

def main():
    while True:
        if urlopen('https://www.google.com/', timeout=10):
            break
    mail()


if __name__ == "__main__":
    main()
