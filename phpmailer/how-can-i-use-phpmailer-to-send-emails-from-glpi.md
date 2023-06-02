# How can I use PHPMailer to send emails from GLPI?
// plain

PHPMailer is a library for sending emails from PHP applications. It can be used with GLPI to send emails from the application. Here is an example code block for sending an email with PHPMailer:

```
<?php
require 'PHPMailer/PHPMailerAutoload.php';

$mail = new PHPMailer;

//Server settings
$mail->isSMTP();                                      // Set mailer to use SMTP
$mail->Host = 'smtp1.example.com;smtp2.example.com';  // Specify main and backup SMTP servers
$mail->SMTPAuth = true;                               // Enable SMTP authentication
$mail->Username = 'user@example.com';                 // SMTP username
$mail->Password = 'secret';                           // SMTP password
$mail->SMTPSecure = 'tls';                            // Enable TLS encryption, `ssl` also accepted
$mail->Port = 587;                                    // TCP port to connect to

//Recipients
$mail->setFrom('from@example.com', 'Mailer');
$mail->addAddress('joe@example.net', 'Joe User');     // Add a recipient

//Content
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

The code above will send an email with the subject "Here is the subject" to the recipient "Joe User". The body of the email will be a HTML message.

The code consists of the following parts:

1. Require the PHPMailer library: `require 'PHPMailer/PHPMailerAutoload.php';`
2. Create a new instance of PHPMailer: `$mail = new PHPMailer;`
3. Configure the server settings: `$mail->isSMTP();`, `$mail->Host`, `$mail->SMTPAuth`, `$mail->Username`, `$mail->Password`, `$mail->SMTPSecure`, `$mail->Port`
4. Set the recipient: `$mail->setFrom()`, `$mail->addAddress()`
5. Configure the content of the email: `$mail->isHTML()`, `$mail->Subject`, `$mail->Body`, `$mail->AltBody`
6. Send the email: `$mail->send()`
7. Check if the email was sent successfully: `if(!$mail->send())`

For more information about using PHPMailer with GLPI, please refer to the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/blob/master/docs/GLPI.md).

onelinerhub: [How can I use PHPMailer to send emails from GLPI?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-to-send-emails-from-glpi)