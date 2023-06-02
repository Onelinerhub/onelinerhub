# host

How do I configure PHPMailer to use a localhost server?
// plain

To configure PHPMailer to use a localhost server, you will need to use the following code:
```
<?php
require 'PHPMailerAutoload.php';
$mail = new PHPMailer;
$mail->isSMTP();
$mail->Host = 'localhost';
$mail->SMTPAuth = false;
$mail->Port = 25;
$mail->SMTPSecure = false;
$mail->setFrom('example@example.com', 'Example');
$mail->addAddress('example2@example.com', 'Example 2');
$mail->Subject = 'PHPMailer Localhost Test';
$mail->Body = 'This is a test.';
if (!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
?>
```

This code will create a new instance of PHPMailer and configure it to use the localhost server. The `$mail->isSMTP()` method is used to tell PHPMailer to use SMTP protocol and the `$mail->Host` property is used to set the host to `localhost`. The `$mail->SMTPAuth` and `$mail->SMTPSecure` properties are set to `false` since authentication and encryption are not required for localhost. Then the `$mail->setFrom()` and `$mail->addAddress()` methods are used to set the sender and recipient. The `$mail->Subject` and `$mail->Body` properties are used to set the subject and body of the email. Finally, the `$mail->send()` method is used to send the email. If the email is successfully sent, the `Message has been sent` message will be displayed. If an error occurs, the `Message could not be sent` message and the `$mail->ErrorInfo` property will be displayed.

## Code explanation

- `$mail->isSMTP()`: This method is used to tell PHPMailer to use SMTP protocol.
- `$mail->Host`: This property is used to set the host to `localhost`.
- `$mail->SMTPAuth` and `$mail->SMTPSecure`: These properties are set to `false` since authentication and encryption are not required for localhost.
- `$mail->setFrom()` and `$mail->addAddress()`: These methods are used to set the sender and recipient.
- `$mail->Subject` and `$mail->Body`: These properties are used to set the subject and body of the email.
- `$mail->send()`: This method is used to send the email.

#### ## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)

onelinerhub: [host

How do I configure PHPMailer to use a localhost server?](https://onelinerhub.com/phpmailer/host--how-do-i-configure-phpmailer-to-use-a-localhost-server)