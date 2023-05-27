import requests #http requests

from bs4 import BeautifulSoup #webscraping

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime
now = datetime.datetime.now()


content = '' # email content





def extract_news(url):
    print('Extracting news')
    temp_content = ''
    temp_content += ('<b> News:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content

    soup = BeautifulSoup(content, 'html.parser')
       
    for i, tag in enumerate(soup.find_all('a')):
        soup.find_all('//body/main//div//a', attrs={'class':'title'})
        temp_content += (str(i+1)+' :: '+tag.text + "\n" + '<br>')
    
    

    return(temp_content)

temp_content = extract_news('https://thehackernews.com/')
content += temp_content
content += ('<br>--------<br>')
content += ('<br><br>End of Message')

#send email

print('Composing Email...')

# update your email details

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = ''
TO = ''
PASS = ''

msg = MIMEMultipart()

msg['Subject'] = 'Hacker News ' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)

msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))

print('Initiating Server')

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent')

server.quit()