# email

How do I use PHPMailer to send an email?
// plain

PHPMailer is a popular open source library for sending emails from PHP applications. To use PHPMailer to send an email, you will need to include the PHPMailer library in your project, create a PHPMailer instance, and configure the instance with the necessary information such as the SMTP host, port, and authentication credentials.

Example code to send an email using PHPMailer:
```
<?php
// Include PHPMailer library
require 'PHPMailer/PHPMailerAutoload.php';

// Create PHPMailer instance
$mail = new PHPMailer();

// Configure SMTP settings
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->Port = 587;
$mail->SMTPAuth = true;
$mail->Username = 'username@example.com';
$mail->Password = 'password';

// Set email content
$mail->setFrom('from@example.com', 'Sender Name');
$mail->addAddress('to@example.com', 'Receiver Name');
$mail->Subject = 'Email Subject';
$mail->Body = 'This is the body of the email';

// Send email
if($mail->send()) {
    echo 'Message has been sent';
} else {
    echo 'Message could not be sent';
}
```

## Output example
 `Message has been sent`

## Code explanation

- `require 'PHPMailer/PHPMailerAutoload.php';`: This line includes the PHPMailer library.
- `$mail = new PHPMailer();`: This line creates a new instance of the PHPMailer class.
- `$mail->isSMTP();`: This line sets the mailer to use SMTP.
- `$mail->Host = 'smtp.example.com';`: This line sets the SMTP host.
- `$mail->Port = 587;`: This line sets the SMTP port.
- `$mail->SMTPAuth = true;`: This line enables SMTP authentication.
- `$mail->Username = 'username@example.com';`: This line sets the SMTP username.
- `$mail->Password = 'password';`: This line sets the SMTP password.
- `$mail->setFrom('from@example.com', 'Sender Name');`: This line sets the sender of the email.
- `$mail->addAddress('to@example.com', 'Receiver Name');`: This line sets the recipient of the email.
- `$mail->Subject = 'Email Subject';`: This line sets the subject of the email.
- `$mail->Body = 'This is the body of the email';`: This line sets the body of the email.
- `if($mail->send())`: This line sends the email.

## Helpful links
- [PHPMailer](https://github.com/PHPMailer/PHPMailer)
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)

onelinerhub: [email

How do I use PHPMailer to send an email?](https://onelinerhub.com/phpmailer/email--how-do-i-use-phpmailer-to-send-an-email)