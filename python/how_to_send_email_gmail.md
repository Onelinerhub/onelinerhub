# How to send email using gmail

You have to enable Less Secure Sign-In in your google account (sender email) before running the above scrpit example.

```python
import smtplib

to = 'someone@yahoo.com'
subject = 'Hi!'
body = 'Hi again!'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % ('my@gmail.com', ", ".to, subject, body)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login('my@gmail.com', 'pwd')
server.sendmail('my@gmail.com', to, email_text)
server.close()
```      

- import smtplib - library to work with SMTP servers
- my@gmail.com - gmail login (and sender address)
- 'pwd' - gmail password
- someone@yahoo.com - receiver address
- email_text - formatted email message to send through SMTP
- smtplib.SMTP_SSL( - connects to gmail SMTP
- server.ehlo() - handshake with SMTP
- server.login( - authenticate our gmail account
- server.sendmail( - sends email
- server.close() - closes connection to SMTP server
