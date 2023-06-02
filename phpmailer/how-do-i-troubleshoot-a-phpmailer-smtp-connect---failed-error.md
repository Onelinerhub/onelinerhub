# How do I troubleshoot a PHPMailer SMTP connect() failed error?
// plain

To troubleshoot a PHPMailer SMTP connect() failed error, first check the SMTP credentials you are using to connect. Make sure the username, password, host, and port are all correct. Additionally, check your server's firewall settings to make sure port 25 (or whatever port you are using) is open.

Next, try using the `SMTPDebug` option to get more information about the connection. You can set it to `2` and then run the code to see the output.

```
$mail->SMTPDebug = 2;
$mail->send();
```

## Output example

```
SMTP -> ERROR: Failed to connect to server: Connection timed out (110)
SMTP Error: Could not connect to SMTP host.
```

The output above indicates that the connection timed out, so there may be an issue with the server's connection to the internet.

If all else fails, you can try using an SMTP service like Gmail or SendGrid.

Parts of the code:
- `$mail->SMTPDebug = 2;`: This sets the SMTPDebug option to 2, which will output more information about the connection.
- `$mail->send();`: This sends the email.

## Helpful links
- [PHPMailer Troubleshooting](https://github.com/PHPMailer/PHPMailer/wiki/Troubleshooting)
- [SMTP Error Codes](https://en.wikipedia.org/wiki/List_of_SMTP_server_return_codes)

onelinerhub: [How do I troubleshoot a PHPMailer SMTP connect() failed error?](https://onelinerhub.com/phpmailer/how-do-i-troubleshoot-a-phpmailer-smtp-connect---failed-error)