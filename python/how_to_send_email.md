# How to send email

```python
import smtplib
sender_email = "sender@gmail.com"
rec_email = "receiver@gmail.com"
password = input(str("Please enter your password : "))
message = input(str("Please enter the message : "))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, rec_email, message)

```      

- `smtplib` - this module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon.
- `sender_email`, `rec_email` - variable for sender and receiver email respectively.
- `password` - it is going to be the password of sender email.
- `message` - it is the message which sender is going to send.
- `SMTP` - SMTP stands for Simple Mail Transfer Protocol.
- `server` - to have connection with gmail we have to intialize a server with server address and port number.
- `'smtp.gmail.com'` - server address.
- `587` - port number.
- `starttls()` - start connection with gmail and smtp server.
- `login` - to login into the smtp server.
- `sendemail` - to send message to the receiver email from sender email.

#### Note: You have to enable Less Secure Sign-In in your google account (sender email) before running the above scrpit example.
