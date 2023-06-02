# How do I troubleshoot a PHPmailer error?
// plain

1. First, check the `$mail->ErrorInfo` property of the `PHPMailer` object for more information about the error.

2. If the error is related to authentication, check the `$mail->Username` and `$mail->Password` properties to make sure they are correct.

3. If the error is related to sending the email, make sure the `$mail->Host` and `$mail->Port` properties are correct.

4. Check the `$mail->SMTPDebug` property to see if it is set to `2` or higher to get more detailed information about the error.

5. If the error is related to an SSL connection, make sure the `$mail->SMTPSecure` property is set to `'ssl'` or `'tls'` and that the `$mail->SMTPAutoTLS` property is set to `true`.

6. If the error is related to the email address, make sure the `$mail->From` and `$mail->addAddress()` properties are set correctly.

7. If the error persists, check the [PHPMailer GitHub page](https://github.com/PHPMailer/PHPMailer) for more troubleshooting tips and examples.

onelinerhub: [How do I troubleshoot a PHPmailer error?](https://onelinerhub.com/phpmailer/how-do-i-troubleshoot-a-phpmailer-error)