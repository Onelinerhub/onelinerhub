# How can I use PHPMailer in PHP 8?
// plain

PHPMailer is a library for sending emails from PHP. It supports PHP 8 and can be used to send emails from a web application.

Using PHPMailer with PHP 8 is easy. First, you need to install the library using Composer, the PHP package manager.

```
composer require phpmailer/phpmailer
```

Then, you can use the library in your code. Here's an example of sending a simple email using PHPMailer:

```
<?php

require 'vendor/autoload.php';

$mail = new PHPMailer\PHPMailer\PHPMailer();
$mail->setFrom('from@example.com', 'Your Name');
$mail->addAddress('to@example.com', 'Recipient Name');
$mail->Subject = 'PHPMailer Test Subject';
$mail->Body = 'This is a test message using PHPMailer.';

if(!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
```

This example code creates a new PHPMailer object, sets the sender and recipient, sets the subject and body of the message, and then sends the message. If the message is sent successfully, it will print "Message has been sent".

## Code explanation


- `require 'vendor/autoload.php'` - This loads the PHPMailer library.
- `$mail = new PHPMailer\PHPMailer\PHPMailer()` - This creates a new PHPMailer object.
- `$mail->setFrom('from@example.com', 'Your Name')` - This sets the sender of the message.
- `$mail->addAddress('to@example.com', 'Recipient Name')` - This sets the recipient of the message.
- `$mail->Subject = 'PHPMailer Test Subject'` - This sets the subject of the message.
- `$mail->Body = 'This is a test message using PHPMailer.'` - This sets the body of the message.
- `$mail->send()` - This sends the message.

For more information, see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer).

onelinerhub: [How can I use PHPMailer in PHP 8?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-in-php--)