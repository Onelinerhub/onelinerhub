# How can I use PHPMailer to send emails with PHP?
// plain

PHPMailer is a popular open source library for sending emails with PHP. It allows you to easily send emails using SMTP, send HTML emails, and also supports attachments. Using PHPMailer is relatively simple and straightforward. Here is an example of how to use PHPMailer to send an email:

```php
<?php
require 'PHPMailer/PHPMailerAutoload.php';

$mail = new PHPMailer;

//$mail->SMTPDebug = 3;                               // Enable verbose debug output

$mail->isSMTP();                                      // Set mailer to use SMTP
$mail->Host = 'smtp1.example.com;smtp2.example.com';  // Specify main and backup SMTP servers
$mail->SMTPAuth = true;                               // Enable SMTP authentication
$mail->Username = 'user@example.com';                 // SMTP username
$mail->Password = 'secret';                           // SMTP password
$mail->SMTPSecure = 'tls';                            // Enable TLS encryption, `ssl` also accepted
$mail->Port = 587;                                    // TCP port to connect to

$mail->setFrom('from@example.com', 'Mailer');
$mail->addAddress('joe@example.net', 'Joe User');     // Add a recipient
$mail->addAddress('ellen@example.com');               // Name is optional
$mail->addReplyTo('info@example.com', 'Information');
$mail->addCC('cc@example.com');
$mail->addBCC('bcc@example.com');

$mail->addAttachment('/var/tmp/file.tar.gz');         // Add attachments
$mail->addAttachment('/tmp/image.jpg', 'new.jpg');    // Optional name
$mail->isHTML(true);                                  // Set email format to HTML

$mail->Subject = 'Here is the subject';
$mail->Body    = 'This is the HTML message body <b>in bold!</b>';
$mail->AltBody = 'This is the body in plain text for non-HTML mail clients';

if(!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
```

The code above will send an email using the PHPMailer library. It will set up the SMTP server connection, set the sender and recipient information, add any attachments, set the email content to HTML format, set the subject and body of the email, and then send the email. If the email is successfully sent, it will output `Message has been sent`.

## Code explanation


1. `require 'PHPMailer/PHPMailerAutoload.php';` - This loads the PHPMailer library.
2. `$mail = new PHPMailer;` - This creates a new PHPMailer object.
3. `$mail->isSMTP();` - This sets the mailer to use SMTP.
4. `$mail->Host = 'smtp1.example.com;smtp2.example.com';` - This sets the SMTP server host.
5. `$mail->SMTPAuth = true;` - This enables SMTP authentication.
6. `$mail->Username = 'user@example.com';` - This sets the SMTP username.
7. `$mail->Password = 'secret';` - This sets the SMTP password.
8. `$mail->SMTPSecure = 'tls';` - This enables TLS encryption.
9. `$mail->Port = 587;` - This sets the SMTP port.
10. `$mail->setFrom('from@example.com', 'Mailer');` - This sets the sender of the email.
11. `$mail->addAddress('joe@example.net', 'Joe User');` - This adds a recipient to the email.
12. `$mail->addReplyTo('info@example.com', 'Information');` - This sets the reply-to address of the email.
13. `$mail->addCC('cc@example.com');` - This adds a CC recipient to the email.
14. `$mail->addBCC('bcc@example.com');` - This adds a BCC recipient to the email.
15. `$mail->addAttachment('/var/tmp/file.tar.gz');` - This adds an attachment to the email.
16. `$mail->isHTML(true);` - This sets the email content to HTML format.
17. `$mail->Subject = 'Here is the subject';` - This sets the email subject.
18. `$mail->Body    = 'This is the HTML message body <b>in bold!</b>';` - This sets the email body.
19. `$mail->AltBody = 'This is the body in plain text for non-HTML mail clients';` - This sets the alternative body for non-HTML mail clients.
20. `if(!$mail->send()) {` - This attempts to send the email.
21. `echo 'Message could not be sent.';` - This outputs an error message if the email is not sent.
22. `echo 'Message has been sent';` - This outputs a success message if the email is sent.

For more information, see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer).

onelinerhub: [How can I use PHPMailer to send emails with PHP?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-to-send-emails-with-php)