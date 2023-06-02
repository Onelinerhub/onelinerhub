# command line

How do I use PHPMailer from the command line?
// plain

PHPMailer is a powerful library for sending emails from the command line. It can be used to send emails from a PHP script or from the command line. To use PHPMailer from the command line, you need to install it using Composer. Once installed, you can use the following example code to send an email from the command line:

```
<?php
// Include PHPMailer library
require 'vendor/autoload.php';

// Create an instance of PHPMailer
$mail = new PHPMailer();

// Set mailer to use SMTP
$mail->isSMTP();

// Specify main and backup SMTP servers
$mail->Host = 'smtp.example.com';

// Enable SMTP authentication
$mail->SMTPAuth = true;

// SMTP username
$mail->Username = 'example@example.com';

// SMTP password
$mail->Password = 'password';

// Set email format to HTML
$mail->isHTML(true);

// Email subject
$mail->Subject = 'Test Email';

// Email body content
$mail->Body = '<h1>Test Email using PHPMailer</h1>';

// Send email
if(!$mail->send()){
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
}else{
    echo 'Message has been sent';
}
```

The output of the example code will be either "Message could not be sent. Mailer Error: [error message]" if the email was not sent successfully, or "Message has been sent" if the email was sent successfully.

## Code explanation


1. `require 'vendor/autoload.php';` - This line includes the PHPMailer library.
2. `$mail = new PHPMailer();` - This line creates an instance of PHPMailer.
3. `$mail->isSMTP();` - This line sets the mailer to use SMTP.
4. `$mail->Host = 'smtp.example.com';` - This line specifies the main and backup SMTP servers.
5. `$mail->SMTPAuth = true;` - This line enables SMTP authentication.
6. `$mail->Username = 'example@example.com';` - This line sets the SMTP username.
7. `$mail->Password = 'password';` - This line sets the SMTP password.
8. `$mail->isHTML(true);` - This line sets the email format to HTML.
9. `$mail->Subject = 'Test Email';` - This line sets the email subject.
10. `$mail->Body = '<h1>Test Email using PHPMailer</h1>';` - This line sets the email body content.
11. `if(!$mail->send()){` - This line checks if the email was sent successfully.
12. `echo 'Message has been sent';` - This line prints a success message if the email was sent successfully.

## Helpful links

- [PHPMailer GitHub Repository](https://github.com/PHPMailer/PHPMailer)
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial)

onelinerhub: [command line

How do I use PHPMailer from the command line?](https://onelinerhub.com/phpmailer/command-line--how-do-i-use-phpmailer-from-the-command-line)