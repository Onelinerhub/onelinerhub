# How can I use PHPMailer with Mailtrap?
// plain

PHPMailer is a library for sending emails from PHP applications. It can be used with Mailtrap, a fake SMTP server, to test email sending without actually sending emails.

Here is an example of how to use PHPMailer with Mailtrap:

```
<?php
require 'vendor/autoload.php';

$mail = new PHPMailer;

$mail->isSMTP();
$mail->Host = 'smtp.mailtrap.io';
$mail->SMTPAuth = true;
$mail->Username = 'YOUR_MAILTRAP_USERNAME';
$mail->Password = 'YOUR_MAILTRAP_PASSWORD';
$mail->SMTPSecure = 'tls';
$mail->Port = 2525;

$mail->setFrom('from@example.com', 'Mailtrap');
$mail->addAddress('to@example.net', 'John Doe');

$mail->Subject = 'PHPMailer with Mailtrap';
$mail->Body    = 'This is a test email sent with PHPMailer and Mailtrap';

if(!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
```

The output of this code should be `Message has been sent`.

## Code explanation


1. `require 'vendor/autoload.php';`: This loads the PHPMailer library.
2. `$mail->isSMTP();`: This sets the mailer to use SMTP.
3. `$mail->Host = 'smtp.mailtrap.io';`: This sets the SMTP host to Mailtrap.
4. `$mail->SMTPAuth = true;`: This enables SMTP authentication.
5. `$mail->Username = 'YOUR_MAILTRAP_USERNAME';`: This sets the Mailtrap username.
6. `$mail->Password = 'YOUR_MAILTRAP_PASSWORD';`: This sets the Mailtrap password.
7. `$mail->SMTPSecure = 'tls';`: This sets the encryption system.
8. `$mail->Port = 2525;`: This sets the SMTP port.
9. `$mail->setFrom('from@example.com', 'Mailtrap');`: This sets the sender's address.
10. `$mail->addAddress('to@example.net', 'John Doe');`: This sets the recipient's address.
11. `$mail->Subject = 'PHPMailer with Mailtrap';`: This sets the email subject.
12. `$mail->Body = 'This is a test email sent with PHPMailer and Mailtrap';`: This sets the email body.
13. `if(!$mail->send()) {...}`: This sends the email and checks for errors.

## Helpful links

- [PHPMailer](https://github.com/PHPMailer/PHPMailer)
- [Mailtrap](https://mailtrap.io/)

onelinerhub: [How can I use PHPMailer with Mailtrap?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-with-mailtrap)