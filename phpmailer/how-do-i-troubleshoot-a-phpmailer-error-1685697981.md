# How do I troubleshoot a PHPMailer error?
// plain

1. First, identify the exact error message. This will help to narrow down the possible causes of the issue.
2. Check that all the PHPMailer configuration settings are correct. For example, the `SMTP` host, `Port`, `Username`, `Password`, etc. should all be set correctly.
3. Check that the `SMTP` server is reachable from the server where the code is running. This can be done by using the `ping` command.
4. Check that the `SMTP` server is not blocking the connection. This can be done by running the following code:
```
$mail = new PHPMailer;
$mail->isSMTP();
$mail->SMTPDebug = 2;
$mail->Debugoutput = 'html';
$mail->Host = 'smtp.example.com';
$mail->Port = 587;
$mail->SMTPAuth = true;
$mail->Username = 'user@example.com';
$mail->Password = 'secret';
$mail->SMTPSecure = 'tls';
$mail->From = 'from@example.com';
$mail->FromName = 'From Name';
$mail->addAddress('to@example.com', 'To Name');
$mail->Subject = 'PHPMailer Test Subject';
$mail->Body = 'This is a test message using PHPMailer.';

if (!$mail->send()) {
    echo "Mailer Error: " . $mail->ErrorInfo;
} else {
    echo "Message sent!";
}
```
## Output example

```
SMTP -> FROM SERVER:220 smtp.example.com ESMTP
SMTP -> FROM SERVER: 250-smtp.example.com Hello [127.0.0.1]
250-SIZE 35882577
250-8BITMIME
250-STARTTLS
250-ENHANCEDSTATUSCODES
250-PIPELINING
250-CHUNKING
250 SMTPUTF8
SMTP -> FROM SERVER:220 Ready to start TLS
SMTP -> FROM SERVER: 250-smtp.example.com Hello [127.0.0.1]
250-SIZE 35882577
250-8BITMIME
250-AUTH LOGIN PLAIN XOAUTH2 PLAIN-CLIENTTOKEN OAUTHBEARER XOAUTH
250-ENHANCEDSTATUSCODES
250-PIPELINING
250-CHUNKING
250 SMTPUTF8
Message sent!
```
5. Check the log files of the `SMTP` server for more information about the error.
6. Check the `PHPMailer` documentation for more information about the error.
7. If all else fails, try using a different `SMTP` server.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [Troubleshooting PHPMailer](https://github.com/PHPMailer/PHPMailer/wiki/Troubleshooting)

onelinerhub: [How do I troubleshoot a PHPMailer error?](https://onelinerhub.com/phpmailer/how-do-i-troubleshoot-a-phpmailer-error-1685697981)