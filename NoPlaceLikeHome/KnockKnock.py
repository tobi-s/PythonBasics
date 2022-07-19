import datetime
import smtplib
import ssl
import urllib.request
import urllib.parse
from email.message import EmailMessage
from os import path

pathIPFile="./currentexternalip.txt"

def getExternalIP():
    url = 'https://api.ipify.org'
    gcontext = ssl.SSLContext()
    f = urllib.request.urlopen(url, context=gcontext)
    return f.read().decode('utf-8')

def getTime():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def notify(msgstr):
    msg = EmailMessage()
    msg.set_content(msgstr)

    msg['Subject'] = msgstr
    msg['From'] = 'protobi@gmail.com'
    msg['To'] = 'protobi@gmail.com'

    # Send the message via our own SMTP server.
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context())
    s.login('protobi@gmail.com','phjnkldjclbeeqpi')
    s.send_message(msg)
    s.quit()
    print(getTime(), "Mail sent to:", msg['To'])

def writeCurrentIP(ipstr):
    ip_file = open(pathIPFile, 'w')
    ip_file.write(ipstr)

def readCurrentIP():
    if path.exists(pathIPFile):
        ip_file = open(pathIPFile, 'r')
        return ip_file.read()
    else:
        return "127.0.0.1"

def runNockNock():
    currentip = readCurrentIP()
    print (getTime(), "Current IP: ", currentip)
    externalip = getExternalIP()

    if currentip != externalip:
        print(getTime(), "Change IP address: ", currentip, " -> ", externalip )
        writeCurrentIP(externalip)
        notify("Change IP address: " + currentip + " -> " + externalip )
        print(getTime(), "New Current IP: ", currentip)
    else:
        print(getTime(), "CurrentIP = ExternalIP")





