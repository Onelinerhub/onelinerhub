# How do I use PHPMailer with WAMP?
// plain

Using PHPMailer with WAMP is quite easy. Here is an example code block that will send a basic email:

```
<?php
require 'PHPMailerAutoload.php';

$mail = new PHPMailer;

$mail->isSMTP();
$mail->Host = 'smtp.gmail.com';
$mail->SMTPAuth = true;
$mail->Username = 'youremail@gmail.com';
$mail->Password = 'yourpassword';
$mail->SMTPSecure = 'tls';
$mail->Port = 587;

$mail->From = 'youremail@gmail.com';
$mail->FromName = 'Your Name';
$mail->addAddress('recipient@example.com', 'Recipient Name');

$mail->addReplyTo('youremail@gmail.com', 'Your Name');

$mail->WordWrap = 50;
$mail->isHTML(true);

$mail->Subject = 'Using PHPMailer';
$mail->Body    = 'This is a test email using PHPMailer.';

if(!$mail->send()) {
   echo 'Message could not be sent.';
   echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
   echo 'Message has been sent';
}
```

## Output example

```
Message has been sent
```

## Code explanation


1. `require 'PHPMailerAutoload.php';` - This includes the PHPMailer library.
2. `$mail = new PHPMailer;` - This creates a new PHPMailer instance.
3. `$mail->isSMTP();` - This sets the mailer to use SMTP protocol.
4. `$mail->Host = 'smtp.gmail.com';` - This sets the SMTP host.
5. `$mail->SMTPAuth = true;` - This enables SMTP authentication.
6. `$mail->Username = 'youremail@gmail.com';` - This sets the SMTP username.
7. `$mail->Password = 'yourpassword';` - This sets the SMTP password.
8. `$mail->SMTPSecure = 'tls';` - This sets the SMTP security protocol.
9. `$mail->Port = 587;` - This sets the SMTP port.
10. `$mail->From = 'youremail@gmail.com';` - This sets the sender's email address.
11. `$mail->FromName = 'Your Name';` - This sets the sender's name.
12. `$mail->addAddress('recipient@example.com', 'Recipient Name');` - This sets the recipient's email address and name.
13. `$mail->addReplyTo('youremail@gmail.com', 'Your Name');` - This sets the reply-to address and name.
14. `$mail->WordWrap = 50;` - This sets the word wrap.
15. `$mail->isHTML(true);` - This sets the email format to HTML.
16. `$mail->Subject = 'Using PHPMailer';` - This sets the email subject.
17. `$mail->Body    = 'This is a test email using PHPMailer.';` - This sets the email body.
18. `if(!$mail->send()) {` - This checks if the email was sent successfully.
19. `echo 'Message could not be sent.';` - This prints an error message.
20. `echo 'Mailer Error: ' . $mail->ErrorInfo;` - This prints the error details.
21. `} else {` - This runs if the email was sent successfully.
22. `echo 'Message has been sent';` - This prints a success message.

## Helpful links

- [PHPMailer](https://github.com/PHPMailer/PHPMailer)
- [WAMP](http://www.wampserver.com/en/)

onelinerhub: [How do I use PHPMailer with WAMP?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-with-wamp)