# How do I use a HTML file in the body of a PHPMailer message?
// plain

To use a HTML file in the body of a PHPMailer message, you can use the `msgHTML()` method. This method takes an HTML string, an external HTML file, or an array of attachments.

The following example code shows how to use the `msgHTML()` method to send an HTML file as the message body:
```php
<?php
require 'PHPMailerAutoload.php';

$mail = new PHPMailer;

// Set up SMTP
$mail->IsSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'username';
$mail->Password = 'password';

// Set recipients
$mail->addAddress('recipient@example.com');

// Set the subject
$mail->Subject = 'Message Subject';

// Set the body
$mail->msgHTML(file_get_contents('message.html'));

// Send the email
$mail->send();
```

This code will send an email with the contents of the `message.html` file as the body of the message.

## Code explanation

- `require 'PHPMailerAutoload.php';`: This line includes the PHPMailer library.
- `$mail = new PHPMailer;`: This line creates a new PHPMailer object.
- `$mail->IsSMTP();`: This line sets the mailer to use SMTP for delivery.
- `$mail->Host = 'smtp.example.com';`: This line sets the SMTP host.
- `$mail->SMTPAuth = true;`: This line sets SMTP authentication to true.
- `$mail->Username = 'username';`: This line sets the SMTP username.
- `$mail->Password = 'password';`: This line sets the SMTP password.
- `$mail->addAddress('recipient@example.com');`: This line sets the recipient address.
- `$mail->Subject = 'Message Subject';`: This line sets the message subject.
- `$mail->msgHTML(file_get_contents('message.html'));`: This line sets the message body to the contents of the `message.html` file.
- `$mail->send();`: This line sends the message.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [PHPMailer Quick Start Guide](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial)

onelinerhub: [How do I use a HTML file in the body of a PHPMailer message?](https://onelinerhub.com/phpmailer/how-do-i-use-a-html-file-in-the-body-of-a-phpmailer-message)