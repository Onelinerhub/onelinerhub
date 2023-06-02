# How can I use PHPMailer to send emails in PHP 8.0?
// plain

PHPMailer is a library for sending emails in PHP 8.0. It's easy to use and supports a wide range of features. To use it, you'll need to download and include the PHPMailer library in your project.

Here's an example of how to use PHPMailer to send an email:

```
<?php

require 'PHPMailer/PHPMailerAutoload.php';

$mail = new PHPMailer;

// Set up SMTP
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'username';
$mail->Password = 'password';

// Set up email
$mail->From = 'from@example.com';
$mail->FromName = 'From Name';
$mail->addAddress('to@example.com', 'To Name');
$mail->Subject = 'Subject';
$mail->Body = 'This is the body of the message.';

// Send the email
$mail->send();

```

This code does the following:
1. Includes the PHPMailer library
2. Sets up SMTP authentication
3. Sets up the email details (from, to, subject, body)
4. Sends the email

For more information, see the official [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer).

onelinerhub: [How can I use PHPMailer to send emails in PHP 8.0?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-to-send-emails-in-php----)