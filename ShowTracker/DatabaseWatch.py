import schedule
import time
import requests
import smtplib
import os
from email.message import EmailMessage
from Show import Show 
from Database import Database
from datetime import date
from datetime import timedelta
from datetime import datetime

showApiKey = os.environ.get('SHOW_APIKEY')
EmailAddress = os.environ.get('EMAIL_USER')
EmailPassword = os.environ.get('EMAIL_PASS')

def checkDatabase(database):
    showsTommorrow = database.getShowsByDate(str(date.today() + timedelta(days = 1) )) 
    showsToday = database.getShowsByDate(str(date.today())) 
    showsYesterday = database.getShowsByDate(str(date.today() - timedelta(days = 1)))

    showsTodayMessage = "The following episodes air today: "  
    if len(showsToday) != 0:
        for show in showsToday: 
            showsTodayMessage += ('\nThe episode \"' + show[6] + '\" of ' + str(show[0]) + ' airs today')
    else: 
        showsTodayMessage = "No show you currently watch air today"

    if len(showsTommorrow) != 0:
        showsTommorrowMessage = "The following shows air tommorrow: " 
        for show in showsTommorrow: 
            showsTodayMessage += ('\nThe episode \"' + show[6] + '\" of ' + str(show[0]) + ' airs tommorrow')
    else: 
        showsTommorrowMessage = "No show you currently watch air tommorrow"

    sendShowReminder(EmailAddress, EmailPassword, 'Upcoming shows', showsTodayMessage, 'ninjagrofman@gmail.com')
    sendShowReminder(EmailAddress, EmailPassword, 'Upcoming shows', showsTommorrowMessage, 'ninjagrofman@gmail.com')

    showsToUpdate = []

    for currentShow in showsYesterday: 
        showsToUpdate.append(Show(currentShow[0], 'tv', showApiKey))

    for show in showsToUpdate: 
        database.updateShow(show)
    

def sendShowReminder(emailSender, emailPassword, subject, message, recipient, ):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = emailSender
    msg['To'] = recipient  
    msg.set_content(message)
    print(msg)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: 
        smtp.login(emailSender, emailPassword)
        smtp.send_message(msg)

    print('successfully sent the mail.')

def startWatch(filename, checkTime):

    showsDatabase = Database(filename)
    schedule.every().day.at(checkTime).do(checkDatabase, showsDatabase)

    while True:
        schedule.run_pending()
        time.sleep(10) # wait one minute