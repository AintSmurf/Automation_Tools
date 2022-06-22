import requests
#http requests

import smtplib
#email body

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
#system data and time manuplation

from bs4 import BeautifulSoup
#web scraping

""" Note: if you wannna use ur personl info you will need to turn on in your google account "less secure app  access" 
through the security settings till 30/5"""

def extract_news(url):
    print("print Extracting Hacker New Stories ..")
    temp = ''
    temp += ('<b> Top Stories:<b>\n'+'<br>'+'-'*20+'<br>')
    response = requests.get(url)
    data = response.content
    soup = BeautifulSoup(data, 'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        temp += ((str(i+1)+ ' :: '+tag.text+'\n'+'<br>') if tag.text != 'More'else '')
    return temp

def main():

    content = ''
    now = datetime.datetime.now()

    #extracting the titles from the site through beautifulSoup with the Extract function line18
    cnt = extract_news('https://news.ycombinator.com/')
    content += cnt
    content += ('<br>-----<br>')
    content += ('<br><br>End of Message')

    #building the email and provide the parameters that needed
    print('Composing Email..')
    # update your email details
    SERVER = 'smtp.gmail.com'
    PORT = 587
    FROM = '' #Your Email
    TO = '' #The Person you wanna send to
    PASS = ''#Password to your Email

    msg = MIMEMultipart()
    msg['Subject'] = 'Top News Stories HN[Automated Email]'+' '+str(now.day)+'-'+str(now.month)+'-'+str(now.year)
    msg['From'] = FROM
    msg['TO'] = TO
    msg.attach(MIMEText(content, 'html'))

    #Authentiction through smtp
    print('Initiating Server ...')
    server =smtplib.SMTP(SERVER,PORT)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(FROM,PASS)
    server.sendmail(FROM,TO,msg.as_string())

    print('Email Sent..')
    server.quit()
if __name__ == '__main__':
    main()