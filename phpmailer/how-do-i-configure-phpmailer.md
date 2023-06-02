# How do I configure PHPMailer?
// plain

PHPMailer is a popular open-source library for sending emails from PHP. To configure PHPMailer, you need to include the PHPMailer library in your code and set up the necessary parameters.

## Example code

```php
require 'PHPMailerAutoload.php';

$mail = new PHPMailer;

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

## Output example
 `Message has been sent`

## Code explanation


1. `require 'PHPMailerAutoload.php';` - This line includes the PHPMailer library in the code.
2. `$mail = new PHPMailer;` - This initializes a new PHPMailer instance.
3. `$mail->isSMTP();` - This sets the mailer to use SMTP protocol.
4. `$mail->Host = 'smtp1.example.com;smtp2.example.com';` - This sets the SMTP server address.
5. `$mail->SMTPAuth = true;` - This enables SMTP authentication.
6. `$mail->Username = 'user@example.com';` - This sets the SMTP username.
7. `$mail->Password = 'secret';` - This sets the SMTP password.
8. `$mail->SMTPSecure = 'tls';` - This sets the encryption type to use.
9. `$mail->Port = 587;` - This sets the SMTP port to use.
10. `$mail->setFrom('from@example.com', 'Mailer');` - This sets the sender's address.
11. `$mail->addAddress('joe@example.net', 'Joe User');` - This adds a recipient's address.
12. `$mail->addReplyTo('info@example.com', 'Information');` - This sets the reply-to address.
13. `$mail->addCC('cc@example.com');` - This adds a CC recipient's address.
14. `$mail->addBCC('bcc@example.com');` - This adds a BCC recipient's address.
15. `$mail->addAttachment('/var/tmp/file.tar.gz');` - This adds an attachment to the email.
16. `$mail->isHTML(true);` - This sets the email format to HTML.
17. `$mail->Subject = 'Here is the subject';` - This sets the subject of the email.
18. `$mail->Body    = 'This is the HTML message body <b>in bold!</b>';` - This sets the body of the email.
19. `$mail->AltBody = 'This is the body in plain text for non-HTML mail clients';` - This sets the plain text body of the email.
20. `if(!$mail->send()) {` - This checks if the email was sent successfully.
21. `echo 'Message could not be sent.';` - This prints an error message if the email was not sent successfully.
22. `echo 'Message has been sent';` - This prints a success message if the email was sent successfully.

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [PHPMailer Tutorial](https://www.smashingmagazine.com/2018/07/phpmailer-php-email-sending-library/)

onelinerhub: [How do I configure PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-configure-phpmailer)