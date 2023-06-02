# How do I use PHPMailer to send emails from an Xserver?
// plain

Using the PHPMailer library, you can send emails from an Xserver. Here is an example code block:
```
<?php
require 'PHPMailerAutoload.php';

$mail = new PHPMailer;

//Server settings
$mail->Host = 'smtp.example.com';  // Specify main and backup SMTP servers
$mail->SMTPAuth = true;                               // Enable SMTP authentication
$mail->Username = 'username';                 // SMTP username
$mail->Password = 'password';                 // SMTP password
$mail->SMTPSecure = 'tls';                            // Enable TLS encryption, `ssl` also accepted
$mail->Port = 587;                                    // TCP port to connect to

//Recipients
$mail->setFrom('from@example.com', 'Mailer');
$mail->addAddress('joe@example.net', 'Joe User');     // Add a recipient

//Content
$mail->isHTML(true);                                  // Set email format to HTML
$mail->Subject = 'Here is the subject';
$mail->Body    = 'This is the HTML message body <b>in bold!</b>';

if(!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
```

The output of this code block is: `Message has been sent`.

## Code explanation


1. `require 'PHPMailerAutoload.php';` - This line includes the PHPMailer library, which is necessary for sending emails.
2. `$mail->Host = 'smtp.example.com';` - This line sets the hostname of the SMTP server.
3. `$mail->SMTPAuth = true;` - This line enables SMTP authentication.
4. `$mail->Username = 'username';` - This line sets the username for SMTP authentication.
5. `$mail->Password = 'password';` - This line sets the password for SMTP authentication.
6. `$mail->SMTPSecure = 'tls';` - This line sets the encryption type to TLS.
7. `$mail->Port = 587;` - This line sets the port number to 587.
8. `$mail->setFrom('from@example.com', 'Mailer');` - This line sets the sender address and sender name.
9. `$mail->addAddress('joe@example.net', 'Joe User');` - This line sets the recipient address and recipient name.
10. `$mail->isHTML(true);` - This line sets the message format to HTML.
11. `$mail->Subject = 'Here is the subject';` - This line sets the subject of the email.
12. `$mail->Body    = 'This is the HTML message body <b>in bold!</b>';` - This line sets the body of the email.
13. `if(!$mail->send()) {` - This line checks if the email was sent successfully.
14. `echo 'Message has been sent';` - This line prints a message if the email was sent successfully.
15. `echo 'Message could not be sent.';` - This line prints a message if the email was not sent successfully.

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [How to Send Email using PHP](https://www.w3schools.com/php/func_mail_mail.asp)

onelinerhub: [How do I use PHPMailer to send emails from an Xserver?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-send-emails-from-an-xserver)