import smtplib

ADDRESS = ''
PASSWORD = ''
RECIPIENT = ''
MESSAGGE = ''
HOST = ''
PORT = 000

content= MESSAGGE
mail=smtplib.SMTP(HOST, PORT)
mail.ehlo()
mail.starttls()
mail.login(ADDRESS, PASSWORD)

header='To:' + RECIPIENT + '\nFrom:' + ADDRESS + '\n' + 'Subject:' + '' + '\n'
content=header+content

mail.sendmail(ADDRESS, ADDRESS, content)
mail.close
